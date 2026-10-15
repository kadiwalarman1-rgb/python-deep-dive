import os
import shutil
from pathlib import Path


def main():
    output_dir = Path("lab33_output")
    source_folder = output_dir / "sample_folder"
    backup_folder = output_dir / "backup_script_backup"
    source_folder.mkdir(parents=True, exist_ok=True)

    if not any(source_folder.iterdir()):
        (source_folder / "notes.txt").write_text("Backup me!", encoding="utf-8")

    backup_folder.mkdir(parents=True, exist_ok=True)
    copied_count = 0

    for filename in os.listdir(source_folder):
        source_path = source_folder / filename
        destination_path = backup_folder / filename
        if source_path.is_file():
            shutil.copy2(source_path, destination_path)
            copied_count += 1
            print(f"Backed up: {filename}")
        elif source_path.is_dir():
            shutil.copytree(source_path, destination_path, dirs_exist_ok=True)
            copied_count += 1
            print(f"Backed up directory: {filename}")

    print(f"Backup complete: {copied_count} item(s) copied to {backup_folder}")
    print("Backup contents:", sorted(os.listdir(backup_folder)))


if __name__ == "__main__":
    main()
