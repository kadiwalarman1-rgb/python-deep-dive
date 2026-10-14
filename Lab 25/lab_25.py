from pathlib import Path

def read_file_basic(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
        print("File content:")
        print(content)
        return content
    except FileNotFoundError:
        print(f"Error: file not found: {path}")
    except OSError as error:
        print(f"File read error: {error}")
    return None

def demonstrate_read_modes(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            text = file.read()
        with open(path, "rb") as file:
            binary = file.read()
        print("Text mode type:", type(text).__name__)
        print("Binary mode type:", type(binary).__name__)
        print("First 20 bytes:", binary[:20])
    except OSError as error:
        print(f"Read mode error: {error}")

def write_student_information(path):
    student_data = "Student Information System\nName: John Doe\nAge: 20\nCourse: Computer Science\nGPA: 3.8\nStatus: Active\n"
    try:
        with open(path, "w", encoding="utf-8") as file:
            written = file.write(student_data)
        print(f"Wrote {written} characters to {path}")
    except OSError as error:
        print(f"File write error: {error}")

def process_lines(path):
    results = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                cleaned = line.rstrip("\n")
                result = {"line_number": line_number, "text": cleaned, "word_count": len(cleaned.split())}
                results.append(result)
                print(f"Line {line_number}: {cleaned} ({result['word_count']} words)")
    except OSError as error:
        print(f"Line processing error: {error}")
    return results

def append_entry(path, entry):
    try:
        with open(path, "a", encoding="utf-8") as file:
            file.write(entry.rstrip("\n") + "\n")
        return True
    except OSError as error:
        print(f"Append error: {error}")
        return False

def main():
    output_dir = Path("lab25_output")
    output_dir.mkdir(exist_ok=True)
    sample_path = output_dir / "sample.txt"
    append_path = output_dir / "append_test.txt"
    student_path = output_dir / "student_info.txt"
    sample_path.write_text("Welcome to File Operations Lab\nThis is line 2 of our sample file\nPython makes file handling easy\nLet's learn together!\n", encoding="utf-8")
    append_path.write_text("Initial content in append file\n", encoding="utf-8")

    print("=== Basic reading ===")
    read_file_basic(sample_path)
    print("=== Read modes ===")
    demonstrate_read_modes(sample_path)
    print("=== Writing ===")
    write_student_information(student_path)
    print("=== Line-by-line processing ===")
    line_data = process_lines(sample_path)
    print("Processed line count:", len(line_data))
    print("=== Appending ===")
    append_entry(append_path, "Second entry added without replacing the first")
    print(append_path.read_text(encoding="utf-8"))
    read_file_basic(output_dir / "missing.txt")

if __name__ == "__main__":
    main()
