# Lab 33: Exploring the Python Standard Library

## What You Will Learn

- Use the \`os\` module to inspect the current working directory and create, list, and delete files and folders.
- Use \`shutil\` to copy files, copy directories, move files, and remove generated backup folders.
- Inspect command-line arguments with \`sys.argv\` and check Python runtime details.
- Build a reusable backup script using \`os\` and \`shutil\`.
- Stop execution safely with \`sys.exit()\` when a required folder is missing.
- Handle generated files in a dedicated output directory so the examples can be run repeatedly.

## Files

- \`os_demo.py\` — working directory and basic file/folder management.
- \`shutil_demo.py\` — copy, move, copy-directory, and delete operations.
- \`sys_demo.py\` — command-line arguments and interpreter details.
- \`backup_script.py\` — backup regular files and subdirectories.
- \`exit_demo.py\` — validate a directory and use exit codes.

## Run

Run these commands from this folder:

\`\`\`bash
python3 os_demo.py
python3 shutil_demo.py
python3 sys_demo.py Arman
python3 backup_script.py
python3 exit_demo.py
\`\`\`

The scripts create their sample data inside \`lab33_output/\`. The \`shutil_demo.py\` script deletes only its own generated \`lab33_output/sample_folder_backup/\` directory as part of its demonstration.
