import csv
from pathlib import Path

STUDENT_FIELDS = ["Name", "Age", "Grade", "Subject", "Score"]
PRODUCT_FIELDS = ["ProductID", "ProductName", "Category", "Price", "Stock"]

def write_sample_csv(path, headers, rows):
    with open(path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(rows)

def read_csv_basic(filename):
    try:
        with open(filename, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader, [])
            rows = list(reader)
        print("Header:", header)
        for index, row in enumerate(rows, start=1):
            print(f"Row {index}: {row}")
        print("Total rows:", len(rows))
        return rows
    except (OSError, csv.Error) as error:
        print(f"CSV read error: {error}")
        return []

def analyze_students(filename):
    students = []
    try:
        with open(filename, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    student = {
                        "Name": row["Name"].strip(),
                        "Age": int(row["Age"]),
                        "Grade": row["Grade"].strip(),
                        "Subject": row["Subject"].strip(),
                        "Score": float(row["Score"]),
                    }
                    students.append(student)
                except (KeyError, TypeError, ValueError) as error:
                    print(f"Skipping invalid student row: {error}")
    except (OSError, csv.Error) as error:
        print(f"CSV analysis error: {error}")
        return []

    average = sum(student["Score"] for student in students) / len(students) if students else 0
    top_student = max(students, key=lambda item: item["Score"], default=None)
    grades = {}
    for student in students:
        grades[student["Grade"]] = grades.get(student["Grade"], 0) + 1
    print(f"Total students: {len(students)}")
    print(f"Average score: {average:.2f}")
    print("Top student:", top_student["Name"] if top_student else "None")
    print("Grade distribution:", dict(sorted(grades.items())))
    print("Scores of at least 90:", [student["Name"] for student in students if student["Score"] >= 90])
    return students

def write_csv_rows(filename, headers, rows):
    try:
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)
        print(f"Wrote {len(rows)} rows to {filename}")
        return True
    except (OSError, csv.Error) as error:
        print(f"CSV write error: {error}")
        return False

def read_product_data(filename):
    try:
        with open(filename, "r", newline="", encoding="utf-8") as csvfile:
            return list(csv.DictReader(csvfile))
    except (OSError, csv.Error) as error:
        print(f"Product CSV read error: {error}")
        return []

def main():
    output_dir = Path("lab26_output")
    output_dir.mkdir(exist_ok=True)
    students_file = output_dir / "students.csv"
    products_file = output_dir / "products.csv"
    student_rows = [
        ["Alice Johnson", 20, "A", "Mathematics", 95],
        ["Bob Smith", 19, "B", "Physics", 87],
        ["Carol Davis", 21, "A", "Chemistry", 92],
        ["David Wilson", 20, "C", "Biology", 78],
        ["Emma Brown", 19, "A", "Mathematics", 89],
        ["Frank Miller", 22, "B", "Physics", 84],
        ["Grace Lee", 20, "A", "Chemistry", 96],
        ["Henry Taylor", 21, "B", "Biology", 81],
    ]
    product_rows = [
        [1001, "Laptop", "Electronics", 899.99, 25],
        [1002, "Desk Chair", "Furniture", 149.99, 50],
        [1003, "Coffee Maker", "Appliances", 79.99, 30],
        [1004, "Notebook", "Stationery", 2.99, 200],
        [1005, "Monitor", "Electronics", 299.99, 15],
    ]
    write_sample_csv(students_file, STUDENT_FIELDS, student_rows)
    write_sample_csv(products_file, PRODUCT_FIELDS, product_rows)
    print("=== Basic CSV reading ===")
    read_csv_basic(students_file)
    print("=== Dictionary CSV analysis ===")
    students = analyze_students(students_file)
    print("=== CSV writing ===")
    write_csv_rows(output_dir / "high_scores.csv", STUDENT_FIELDS, [student for student in students if student["Score"] >= 90])
    write_csv_rows(output_dir / "products_copy.csv", PRODUCT_FIELDS, read_product_data(products_file))
    print("Outputs written to", output_dir)

if __name__ == "__main__":
    main()
