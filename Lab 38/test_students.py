"""Demonstrations of methods called from several Student instances."""

from student_manager import Student


def test_multiple_students() -> None:
    """Create students and display their calculated performance."""
    students = [
        Student("Alice Johnson", 16, "10th Grade"),
        Student("Bob Smith", 17, "11th Grade"),
        Student("Carol Davis", 15, "9th Grade"),
    ]

    records = [
        (160, [85, 92, 78]),
        (140, [95, 88, 91, 87]),
        (170, [76, 82, 79]),
    ]
    print("=== Setting Up Student Data ===")
    for student, (attendance, scores) in zip(students, records):
        student.add_attendance(attendance)
        for score in scores:
            student.add_test_score(score)

    print("\n" + "=" * 55)
    print("STUDENT PERFORMANCE REPORT")
    print("=" * 55)
    for number, student in enumerate(students, start=1):
        print(f"\n--- Student {number} ---")
        student.display_info()
        average = student.calculate_average_score()
        attendance_pct = student.calculate_attendance_percentage()
        grade_point = student.get_grade_point()
        print(f"Average Score: {average:.2f}")
        print(f"Attendance: {attendance_pct:.2f}%")
        print(f"Grade Point: {grade_point:.1f}")

        if average >= 90:
            performance = "Excellent"
        elif average >= 80:
            performance = "Good"
        elif average >= 70:
            performance = "Satisfactory"
        else:
            performance = "Needs Improvement"
        print(f"Performance Level: {performance}")


def test_method_sequence() -> None:
    """Demonstrate calling several methods in sequence on one object."""
    print("\n" + "=" * 55)
    print("METHOD SEQUENCE DEMONSTRATION")
    print("=" * 55)

    student = Student("David Wilson", 16, "10th Grade")
    for score in (85, 90, 87):
        student.add_test_score(score)
    for days in (50, 75, 25):
        student.add_attendance(days)
    student.set_age(17)

    print("\nFinal student information:")
    student.display_info()
    print("\nPerformance Summary:")
    for key, value in student.get_performance_summary().items():
        print(f"  {key.replace('_', ' ').title()}: {value}")


if __name__ == "__main__":
    test_multiple_students()
    test_method_sequence()
