import os
import sys
from pathlib import Path


def main():
    source_folder = Path("lab33_output") / "sample_folder"

    if not source_folder.exists():
        print(f"Error: '{source_folder}' does not exist. Exiting program.")
        sys.exit(1)

    if not source_folder.is_dir():
        print(f"Error: '{source_folder}' exists but is not a directory.")
        sys.exit(1)

    print(f"'{source_folder}' found. Continuing with the program...")
    print("Files inside:", sorted(os.listdir(source_folder)))
    sys.exit(0)


if __name__ == "__main__":
    main()
