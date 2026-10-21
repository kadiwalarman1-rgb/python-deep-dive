#!/usr/bin/env python3
"""Simple daily lab progress tracker for Python Deep Dive."""
from __future__ import annotations
import json, subprocess
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path
from urllib.parse import quote, urlparse
ROOT=Path(__file__).resolve().parent
PROGRESS_DIR=ROOT/'progress'
LOG_FILE=PROGRESS_DIR/'work_log.json'
REPORT_FILE=PROGRESS_DIR/'PROOF_OF_COMPLETION.md'
REPO_URL='https://github.com/kadiwalarman1-rgb/python-deep-dive'

def load_entries():
    if not LOG_FILE.exists(): return []
    try:
        data=json.loads(LOG_FILE.read_text(encoding='utf-8'))
        return data if isinstance(data,list) else []
    except (json.JSONDecodeError,OSError) as exc: raise SystemExit(f'Could not read {LOG_FILE}: {exc}')

def save_entries(entries):
    PROGRESS_DIR.mkdir(parents=True,exist_ok=True)
    LOG_FILE.write_text(json.dumps(entries,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

def lab_link(lab):
    clean=lab.strip()
    if clean.lower().startswith('lab '): return f"{REPO_URL}/tree/main/{quote('Lab '+clean[4:].strip(),safe='')}"
    return REPO_URL

def latest_commit():
    def git(*args): return subprocess.run(['git','-C',str(ROOT),*args],capture_output=True,text=True,check=True).stdout.strip()
    try:
        sha=git('rev-parse','HEAD'); message=git('log','-1','--pretty=%s'); committed_at=git('log','-1','--pretty=%cI'); remote=git('remote','get-url','origin').removesuffix('.git')
    except (subprocess.CalledProcessError,FileNotFoundError): return {'sha':'','message':'','url':'','committed_at':''}
    if remote.startswith('git@github.com:'): url=f"https://github.com/{remote.removeprefix('git@github.com:')}/commit/{sha}"
    else:
        parsed=urlparse(remote); url=f'https://github.com{parsed.path}/commit/{sha}' if parsed.hostname=='github.com' else ''
    return {'sha':sha,'message':message,'url':url,'committed_at':committed_at}

def add_entry():
    print('\n=== Add Daily Lab Progress ===')
    work_date=input(f'Date [{date.today().isoformat()}]: ').strip() or date.today().isoformat()
    try: date.fromisoformat(work_date)
    except ValueError: print('Invalid date. Use YYYY-MM-DD.'); return
    lab=input('Lab name/number (e.g. Lab 40): ').strip()
    if not lab: print('Lab name is required.'); return
    entries=load_entries()
    if any(e.get('date')==work_date and e.get('lab','').casefold()==lab.casefold() for e in entries):
        print(f'{lab} is already recorded for {work_date}.'); return
    commit=latest_commit()
    if commit['sha']: print(f"Latest commit: {commit['sha'][:7]} — {commit['message']}")
    if input('Attach latest GitHub commit link if available? [Y/n]: ').strip().lower() in {'n','no'}: commit={'sha':'','message':'','url':'','committed_at':''}
    entries.append({'date':work_date,'recorded_at':datetime.now().astimezone().isoformat(timespec='seconds'),'lab':lab,'commit_sha':commit['sha'],'commit_message':commit['message'],'commit_url':commit['url'],'commit_date':commit['committed_at']})
    entries.sort(key=lambda e:(e.get('date',''),e.get('lab','').casefold())); save_entries(entries); write_report(entries)
    print(f'Added {lab} under {work_date}. Report: {REPORT_FILE.relative_to(ROOT)}')

def grouped_entries(entries):
    groups=defaultdict(list)
    for entry in entries: groups[entry.get('date','Unknown date')].append(entry)
    return dict(sorted(groups.items(),reverse=True))

def list_entries():
    groups=grouped_entries(load_entries())
    if not groups: print('No labs recorded. Run: python3 progress_tracker.py add'); return
    print('\n========== PROGRESS OF COMPLETION ==========')
    for day,items in groups.items():
        print(f"\n+{'-'*42}+"); print(f'| {day} — {len(items)} lab(s)'); print(f"+{'-'*42}+")
        for item in items:
            print(f"  • {item.get('lab','Lab')}  {lab_link(item.get('lab',''))}")
            if item.get('commit_url'): print(f"    Commit: {item['commit_url']}")

def write_report(entries):
    groups=grouped_entries(entries); lines=['# Proof of Completion','','Daily progress grouped into date blocks. Each lab name links to its folder in this repository.','']
    if not groups: lines.extend(['No labs recorded yet. Run python3 progress_tracker.py add.',''])
    for day,items in groups.items():
        lines.extend(['<details>',f'<summary>📅 {day} — {len(items)} lab(s)</summary>',''])
        seen=set()
        for item in items:
            lab=item.get('lab','Lab'); key=lab.casefold()
            if key in seen: continue
            seen.add(key); lines.append(f'- [{lab}]({lab_link(lab)})')
            if item.get('commit_url'): lines.append(f"  - [GitHub commit {item.get('commit_sha','')[:7] or 'View commit'}]({item['commit_url']})")
        lines.extend(['','</details>',''])
    PROGRESS_DIR.mkdir(parents=True,exist_ok=True); REPORT_FILE.write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8')

def main():
    import argparse
    parser=argparse.ArgumentParser(description='Track which labs were worked on each day.')
    parser.add_argument('command',choices=('add','list','report')); args=parser.parse_args()
    if args.command=='add': add_entry()
    else:
        entries=load_entries(); write_report(entries)
        if args.command=='list': list_entries()
        else: print(f'Report generated: {REPORT_FILE.relative_to(ROOT)}')
if __name__=='__main__': main()
