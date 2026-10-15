import os
from pathlib import Path


def main():
    output_dir = Path("lab33_output")
    sample_folder = output_dir / "sample_folder"
    output_dir.mkdir(exist_ok=True)
    sample_folder.mkdir(parents=True, exist_ok=True)

    print("Current directory:", os.getcwd())
    print("Platform:", os.name)
    print("Creating sample files...")

    (sample_folder / "file1.txt").write_text("This is file 1.", encoding="utf-8")
    (sample_folder / "file2.txt").write_text("This is file 2.", encoding="utf-8")
    print("Folder created:", sample_folder)
    print("Contents:", sorted(os.listdir(sample_folder)))

    file_to_delete = sample_folder / "file2.txt"
    if file_to_delete.exists():
        os.remove(file_to_delete)
        print("Deleted:", file_to_delete.name)
    print("Contents after deletion:", sorted(os.listdir(sample_folder)))


if __name__ == "__main__":
    main()
