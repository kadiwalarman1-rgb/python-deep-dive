import sys


def main():
    print("Script name:", sys.argv[0])
    print("Arguments passed:", sys.argv[1:])

    if len(sys.argv) < 2:
        print("No name provided. Usage: python3 sys_demo.py <your_name>")
        return

    name = sys.argv[1]
    print(f"Hello, {name}! Welcome to the sys module demo.")
    print("Python version:", sys.version.split()[0])
    print("Platform:", sys.platform)


if __name__ == "__main__":
    main()
