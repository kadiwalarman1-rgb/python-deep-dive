import json
from datetime import date, datetime
from pathlib import Path

class DateTimeEncoder(json.JSONEncoder):
    def default(self, value):
        if isinstance(value, (date, datetime)):
            return value.isoformat()
        return super().default(value)

def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"JSON file not found: {path}")
    except json.JSONDecodeError as error:
        print(f"Invalid JSON in {path}: {error}")
    except OSError as error:
        print(f"JSON read error: {error}")
    return None

def save_json(path, data):
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False, cls=DateTimeEncoder)
        print(f"Saved JSON to {path}")
        return True
    except (OSError, TypeError, ValueError) as error:
        print(f"JSON write error: {error}")
        return False

def validate_student(student):
    required = {"id", "name", "age", "major", "gpa", "courses", "contact"}
    missing = required.difference(student)
    if missing:
        raise ValueError(f"Student is missing fields: {sorted(missing)}")
    if not isinstance(student["id"], int) or student["id"] <= 0:
        raise ValueError("Student id must be a positive integer")
    if not 0 <= float(student["gpa"]) <= 4:
        raise ValueError("GPA must be between 0 and 4")
    if not isinstance(student["courses"], list) or not isinstance(student["contact"], dict):
        raise ValueError("Courses must be a list and contact must be an object")

def main():
    output_dir = Path("lab27_output")
    output_dir.mkdir(exist_ok=True)
    input_path = output_dir / "students.json"
    output_path = output_dir / "students_updated.json"
    broken_path = output_dir / "broken.json"
    sample = {
        "students": [
            {"id": 1, "name": "Alice Johnson", "age": 20, "major": "Computer Science", "gpa": 3.8, "courses": ["Python Programming", "Data Structures", "Web Development"], "contact": {"email": "alice@example.com", "phone": "555-0123"}},
            {"id": 2, "name": "Bob Smith", "age": 22, "major": "Information Technology", "gpa": 3.6, "courses": ["Network Security", "Database Management"], "contact": {"email": "bob@example.com", "phone": "555-0456"}},
            {"id": 3, "name": "Carol Davis", "age": 19, "major": "Software Engineering", "gpa": 3.9, "courses": ["Algorithm Design", "Software Testing"], "contact": {"email": "carol@example.com", "phone": "555-0789"}}
        ],
        "university": "Tech University",
        "semester": "Fall 2026"
    }
    save_json(input_path, sample)
    data = load_json(input_path)
    if data is not None:
        print("University:", data.get("university", "Unknown"))
        print("Semester:", data.get("semester", "Unknown"))
        print("Student count:", len(data.get("students", [])))
        for student in data.get("students", []):
            print(f"{student['name']}: GPA {student['gpa']}; courses: {', '.join(student['courses'])}")
        high_gpa = [student for student in data["students"] if student["gpa"] >= 3.8]
        print("Students with GPA >= 3.8:", [student["name"] for student in high_gpa])
        new_student = {"id": 4, "name": "Dina Patel", "age": 21, "major": "Data Science", "gpa": 3.7, "courses": ["Statistics", "Python"], "contact": {"email": "dina@example.com", "phone": "555-0100"}}
        validate_student(new_student)
        data["students"].append(new_student)
        for student in data["students"]:
            if student["id"] == 2:
                student["gpa"] = 3.75
                student["contact"]["email"] = "bob.smith@example.com"
        data["students"] = [student for student in data["students"] if student["id"] != 1]
        data["last_updated"] = datetime.now()
        save_json(output_path, data)
        print("Updated student count:", len(data["students"]))
    broken_path.write_text('{"students": [}', encoding="utf-8")
    load_json(broken_path)
    try:
        validate_student({"id": -1, "gpa": 6})
    except ValueError as error:
        print("Validation handled:", error)

if __name__ == "__main__":
    main()
