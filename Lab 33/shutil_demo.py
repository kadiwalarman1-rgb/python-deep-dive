import os
import shutil
from pathlib import Path


def main():
    output_dir = Path("lab33_output")
    source_folder = output_dir / "sample_folder"
    backup_folder = output_dir / "sample_folder_backup"
    output_dir.mkdir(exist_ok=True)
    source_folder.mkdir(parents=True, exist_ok=True)

    source_file = source_folder / "file1.txt"
    if not source_file.exists():
        source_file.write_text("This is a sample file for shutil.", encoding="utf-8")

    copy_file = source_folder / "file1_copy.txt"
    shutil.copy2(source_file, copy_file)
    print("Copied file to:", copy_file)

    shutil.copytree(source_folder, backup_folder, dirs_exist_ok=True)
    print("Copied folder to:", backup_folder)

    moved_file = backup_folder / "file1_copy.txt"
    if moved_file.exists():
        moved_file.unlink()
    shutil.move(str(copy_file), str(moved_file))
    print("Moved copied file into:", backup_folder)
    print("Source contents:", sorted(os.listdir(source_folder)))
    print("Backup contents:", sorted(os.listdir(backup_folder)))

    shutil.rmtree(backup_folder)
    print("Removed generated backup folder:", backup_folder)
    print("Backup folder exists:", backup_folder.exists())


if __name__ == "__main__":
    main()
