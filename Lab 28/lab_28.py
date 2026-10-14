from pathlib import Path
from datetime import datetime

def write_log_entry(filename, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}\n"
    with open(filename, "a", encoding="utf-8") as file:
        file.write(entry)
    return entry.rstrip()

def demonstrate_context_manager(output_dir):
    filename = output_dir / "context_demo.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Hello, Context Manager!\n")
        file.write("This file closes automatically.\n")
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
    traditional = output_dir / "traditional_demo.txt"
    file = open(traditional, "w", encoding="utf-8")
    try:
        file.write("Traditional file handling needs explicit cleanup.\n")
    finally:
        file.close()
    with open(output_dir / "context_demo2.txt", "w", encoding="utf-8") as file:
        file.write("Context manager handles cleanup automatically.\n")

def read_and_process_file(input_filename, output_filename):
    total_words = 0
    processed_lines = 0
    with open(input_filename, "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()
    with open(output_filename, "w", encoding="utf-8") as output_file:
        for number, line in enumerate(lines, start=1):
            word_count = len(line.split())
            total_words += word_count
            processed_lines += 1
            output_file.write(f"Line {number:4d} ({word_count:2d} words): {line}")
    return {"lines": processed_lines, "words": total_words}

def copy_in_chunks(source, destination, chunk_size=4096):
    bytes_copied = 0
    with open(source, "rb") as source_file, open(destination, "wb") as destination_file:
        while True:
            chunk = source_file.read(chunk_size)
            if not chunk:
                break
            destination_file.write(chunk)
            bytes_copied += len(chunk)
    return bytes_copied

def count_lines_in_chunks(filename, chunk_size=4096):
    newline_count = 0
    last_byte = b""
    total_bytes = 0
    with open(filename, "rb") as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            total_bytes += len(chunk)
            newline_count += chunk.count(b"\n")
            last_byte = chunk[-1:]
    if total_bytes and last_byte != b"\n":
        newline_count += 1
    return total_bytes, newline_count

def safe_read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except PermissionError:
        print(f"Permission denied: {filename}")
    except OSError as error:
        print(f"File read error: {error}")
    return None

def safe_write_file(filename, content):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        return True
    except PermissionError:
        print(f"Permission denied: {filename}")
    except OSError as error:
        print(f"File write error: {error}")
    return False

def main():
    output_dir = Path("lab28_output")
    output_dir.mkdir(exist_ok=True)
    small_file = output_dir / "sample_small.txt"
    large_file = output_dir / "sample_large.txt"
    processed_file = output_dir / "processed_small.txt"
    copied_large = output_dir / "sample_large_copy.txt"
    log_file = output_dir / "operations.log"

    small_file.write_text("This is line 1\nThis is line 2\nThis is line 3\nSample data for testing\n", encoding="utf-8")
    with open(large_file, "w", encoding="utf-8") as file:
        for number in range(10000):
            file.write(f"Line {number + 1}: This is sample data for testing large file operations.\n")

    print("=== Context manager ===")
    demonstrate_context_manager(output_dir)
    print("=== Read and process ===")
    summary = read_and_process_file(small_file, processed_file)
    print("Small file summary:", summary)
    print("=== Large file chunks ===")
    copied = copy_in_chunks(large_file, copied_large, chunk_size=4096)
    size, lines = count_lines_in_chunks(copied_large, chunk_size=4096)
    print(f"Copied bytes: {copied}; verified bytes: {size}; lines: {lines}")
    print("=== Safe operations ===")
    safe_write_file(output_dir / "safe_write.txt", "Safe writing succeeded.\n")
    print("Read result:", safe_read_file(output_dir / "safe_write.txt").strip())
    safe_read_file(output_dir / "missing.txt")
    print(write_log_entry(log_file, f"Processed {summary['lines']} small-file lines and copied {lines} large-file lines"))

if __name__ == "__main__":
    main()
