"""A small student management system using the AdvancedStudent class."""

from advanced_student import AdvancedStudent


class StudentManagementSystem:
    """Manage student records in memory and generate class reports."""

    def __init__(self) -> None:
        self.students: dict[str, AdvancedStudent] = {}
        self.next_id = 1

    def add_student(self, name: str, age: int, grade: str) -> str:
        """Create a student, assign a unique ID, and return that ID."""
        student_id = f"ST{self.next_id:03d}"
        student = AdvancedStudent(name, age, grade, student_id)
        self.students[student_id] = student
        self.next_id += 1
        print(f"Student {name} added with ID: {student_id}")
        return student_id

    def get_student(self, student_id: str) -> AdvancedStudent | None:
        """Return a student by ID, or None if not found."""
        return self.students.get(student_id)

    def list_all_students(self) -> None:
        """Print a list of registered students."""
        if not self.students:
            print("No students in the system")
            return
        print("\n=== ALL STUDENTS ===")
        for student_id, student in self.students.items():
            print(f"ID: {student_id} | Name: {student.name} | Grade: {student.grade}")

    def generate_class_report(self) -> None:
        """Print GPA and attendance summaries for all registered students."""
        if not self.students:
            print("No students to generate report")
            return
        print("\n" + "=" * 60)
        print("CLASS PERFORMANCE REPORT")
        print("=" * 60)

        gpas_with_scores: list[float] = []
        for student_id, student in self.students.items():
            gpa = student.calculate_overall_gpa()
            attendance = student.get_attendance_statistics()["percentage"]
            print(f"\nStudent: {student.name} (ID: {student_id})")
            print(f"  GPA: {gpa:.2f}")
            print(f"  Attendance: {attendance:.2f}%")
            print(f"  Subjects Enrolled: {len(student.subjects)}")
            print(f"  Achievements: {len(student.achievements)}")
            if any(data["scores"] for data in student.subjects.values()):
                gpas_with_scores.append(gpa)

        if gpas_with_scores:
            print("\n" + "=" * 60)
            print(f"CLASS AVERAGE GPA: {sum(gpas_with_scores) / len(gpas_with_scores):.2f}")
        print(f"TOTAL STUDENTS: {len(self.students)}")

    def find_top_performers(self, n: int = 3) -> list[tuple[str, float, str]]:
        """Print and return up to n students with the highest GPA."""
        if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
            raise ValueError("n must be a positive integer")
        scored_students = []
        for student_id, student in self.students.items():
            if any(data["scores"] for data in student.subjects.values()):
                scored_students.append((student.name, student.calculate_overall_gpa(), student_id))
        scored_students.sort(key=lambda item: (-item[1], item[0].casefold()))
        print(f"\n=== TOP {min(n, len(scored_students))} PERFORMERS ===")
        if not scored_students:
            print("No students have scored assessments yet")
        for rank, (name, gpa, student_id) in enumerate(scored_students[:n], start=1):
            print(f"{rank}. {name} (ID: {student_id}) - GPA: {gpa:.2f}")
        return scored_students[:n]


def demo_student_system() -> None:
    """Demonstrate adding students, recording grades, and reporting results."""
    sms = StudentManagementSystem()
    print("=== STUDENT MANAGEMENT SYSTEM DEMO ===")

    print("\n1. Adding Students...")
    alice_id = sms.add_student("Alice Johnson", 16, "11th Grade")
    bob_id = sms.add_student("Bob Smith", 17, "12th Grade")
    carol_id = sms.add_student("Carol Davis", 15, "10th Grade")
    david_id = sms.add_student("David Wilson", 16, "11th Grade")

    print("\n2. Setting Up Student Academic Data...")
    alice = sms.get_student(alice_id)
    bob = sms.get_student(bob_id)
    carol = sms.get_student(carol_id)
    david = sms.get_student(david_id)
    assert alice and bob and carol and david

    # Alice
    alice.enroll_in_subject("Mathematics", "Dr. Smith")
    alice.enroll_in_subject("Physics", "Prof. Johnson")
    alice.add_subject_score("Mathematics", 95, "Test")
    alice.add_subject_score("Mathematics", 92, "Quiz")
    alice.add_subject_score("Physics", 88, "Test")
    alice.add_achievement("Honor Roll")

    # Bob
    bob.enroll_in_subject("Chemistry", "Dr. Brown")
    bob.enroll_in_subject("English", "Ms. Davis")
    bob.add_subject_score("Chemistry", 85, "Test")
    bob.add_subject_score("English", 90, "Essay")
    bob.add_achievement("Science Fair Winner")

    # Carol
    carol.enroll_in_subject("Mathematics", "Dr. Smith")
    carol.enroll_in_subject("Art", "Mr. Garcia")
    carol.add_subject_score("Mathematics", 78, "Test")
    carol.add_subject_score("Art", 95, "Project")

    # David
    david.enroll_in_subject("Physics", "Prof. Johnson")
    david.enroll_in_subject("Computer Science", "Dr. Lee")
    david.add_subject_score("Physics", 92, "Test")
    david.add_subject_score("Computer Science", 98, "Programming Assignment")
    david.add_achievement("Coding Competition Winner")
    david.add_achievement("Math Olympiad Participant")

    sample_dates = ["2024-01-15", "2024-01-16", "2024-01-17", "2024-01-18", "2024-01-19"]
    for sample_date in sample_dates:
        for student in (alice, bob, carol, david):
            student.mark_attendance(sample_date, "Present")

    print("\n3. Listing Students...")
    sms.list_all_students()
    print("\n4. Generating Class Report...")
    sms.generate_class_report()
    print("\n5. Finding Top Performers...")
    sms.find_top_performers(3)
    print("\n6. Generating Alice's Transcript...")
    print(alice.generate_transcript())


if __name__ == "__main__":
    demo_student_system()
