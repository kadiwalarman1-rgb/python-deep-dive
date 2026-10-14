def safe_get(dictionary, key, default="Not available"):
    return dictionary.get(key, default)

def main():
    student = {
        "name": "Alice Johnson",
        "age": 21,
        "major": "Computer Science",
        "gpa": 3.8,
        "grades": {"Math": [88, 92, 95], "Science": [84, 89, 91]},
    }
    print("Student:", student)
    print("Name:", student["name"])
    print("GPA:", safe_get(student, "gpa"))
    print("Email:", safe_get(student, "email"))
    print("First math grade:", student["grades"]["Math"][0])

    for key in ["name", "email", "age"]:
        print(key, "exists:", key in student)

    student["email"] = "alice@example.com"
    student["phone"] = "555-0100"
    student.update({"age": 22, "status": "Active"})
    del student["phone"]
    removed_status = student.pop("status")
    print("Removed status:", removed_status)

    try:
        print(student["missing_key"])
    except KeyError as error:
        print("Missing key handled:", error)

    for key, value in student.items():
        print(f"{key}: {value}")
    city_populations = {"New York": 8419000, "Los Angeles": 3980000, "Chicago": 2716000}
    largest_city = max(city_populations, key=city_populations.get)
    print("Largest city in sample:", largest_city)

if __name__ == "__main__":
    main()
