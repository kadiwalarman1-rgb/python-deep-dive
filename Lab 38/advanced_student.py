"""Advanced student model with subjects, attendance, and achievements."""

from datetime import date
from typing import Any


class AdvancedStudent:
    """Represent a student and their subject-wise academic record."""

    VALID_ATTENDANCE_STATUSES = {"Present", "Absent", "Late", "Excused"}

    def __init__(self, name: str, age: int, grade: str, student_id: str) -> None:
        if not name.strip():
            raise ValueError("Student name cannot be empty")
        if not isinstance(age, int) or isinstance(age, bool) or age <= 0:
            raise ValueError("Age must be a positive integer")
        if not grade.strip():
            raise ValueError("Grade cannot be empty")
        if not student_id.strip():
            raise ValueError("Student ID cannot be empty")

        self.name = name.strip()
        self.age = age
        self.grade = grade.strip()
        self.student_id = student_id.strip()
        self.enrollment_date = date.today()
        self.subjects: dict[str, dict[str, Any]] = {}
        self.attendance_record: list[dict[str, str]] = []
        self.achievements: list[dict[str, str]] = []
        self.disciplinary_actions: list[dict[str, str]] = []

    def enroll_in_subject(self, subject_name: str, teacher: str) -> bool:
        """Enroll this student in a subject once."""
        if not subject_name.strip() or not teacher.strip():
            print("Subject name and teacher are required")
            return False
        if subject_name in self.subjects:
            print(f"Student already enrolled in {subject_name}")
            return False
        self.subjects[subject_name] = {
            "teacher": teacher,
            "scores": [],
            "assignments_completed": 0,
            "total_assignments": 0,
        }
        print(f"Enrolled {self.name} in {subject_name} with teacher {teacher}")
        return True

    def add_subject_score(self, subject: str, score: float, assignment_type: str = "Test") -> bool:
        """Add a dated score to an enrolled subject."""
        if subject not in self.subjects:
            print(f"Student not enrolled in {subject}")
            return False
        if isinstance(score, bool) or not isinstance(score, (int, float)) or not 0 <= score <= 100:
            print("Score must be a number between 0 and 100")
            return False
        if not assignment_type.strip():
            print("Assignment type cannot be empty")
            return False
        self.subjects[subject]["scores"].append({
            "score": float(score),
            "type": assignment_type.strip(),
            "date": str(date.today()),
        })
        print(f"Added {assignment_type} score {score} for {subject}")
        return True

    def mark_attendance(self, attendance_date: str, status: str) -> bool:
        """Record a daily attendance status."""
        if status not in self.VALID_ATTENDANCE_STATUSES:
            print(f"Invalid status. Use: {', '.join(sorted(self.VALID_ATTENDANCE_STATUSES))}")
            return False
        try:
            date.fromisoformat(attendance_date)
        except (TypeError, ValueError):
            print("Date must use YYYY-MM-DD format")
            return False
        if any(record["date"] == attendance_date for record in self.attendance_record):
            print(f"Attendance already recorded for {attendance_date}")
            return False
        self.attendance_record.append({"date": attendance_date, "status": status})
        print(f"Attendance marked: {attendance_date} - {status}")
        return True

    def add_achievement(self, achievement: str, achievement_date: str | None = None) -> bool:
        """Add an achievement with today's date as the default."""
        if not achievement.strip():
            print("Achievement cannot be empty")
            return False
        achievement_date = achievement_date or str(date.today())
        try:
            date.fromisoformat(achievement_date)
        except (TypeError, ValueError):
            print("Achievement date must use YYYY-MM-DD format")
            return False
        self.achievements.append({"achievement": achievement.strip(), "date": achievement_date})
        print(f"Achievement added: {achievement.strip()}")
        return True

    def calculate_subject_average(self, subject: str) -> float:
        """Return a subject's mean score, or zero if it has no scores."""
        if subject not in self.subjects:
            return 0.0
        scores = self.subjects[subject]["scores"]
        if not scores:
            return 0.0
        return sum(item["score"] for item in scores) / len(scores)

    def calculate_overall_gpa(self) -> float:
        """Calculate an unweighted GPA using subjects with at least one score."""
        scored_subjects = [
            subject for subject, data in self.subjects.items() if data["scores"]
        ]
        if not scored_subjects:
            return 0.0

        points = []
        for subject in scored_subjects:
            average = self.calculate_subject_average(subject)
            if average >= 90:
                points.append(4.0)
            elif average >= 80:
                points.append(3.0)
            elif average >= 70:
                points.append(2.0)
            elif average >= 60:
                points.append(1.0)
            else:
                points.append(0.0)
        return sum(points) / len(points)

    def get_attendance_statistics(self) -> dict[str, int | float]:
        """Return attendance counts and the lab's attendance percentage."""
        stats: dict[str, int | float] = {
            "total_days": len(self.attendance_record),
            "present": 0,
            "absent": 0,
            "late": 0,
            "excused": 0,
            "percentage": 0.0,
        }
        for record in self.attendance_record:
            status_key = record["status"].lower()
            stats[status_key] += 1
        # Per the lab definition, Present and Excused count as good attendance.
        good_attendance = int(stats["present"]) + int(stats["excused"])
        total_days = int(stats["total_days"])
        stats["percentage"] = (good_attendance / total_days * 100) if total_days else 0.0
        return stats

    def generate_transcript(self) -> str:
        """Return a formatted transcript without printing it automatically."""
        lines = [
            "=" * 60,
            "STUDENT TRANSCRIPT",
            "=" * 60,
            f"Student ID: {self.student_id}",
            f"Name: {self.name}",
            f"Age: {self.age}",
            f"Grade: {self.grade}",
            f"Enrollment Date: {self.enrollment_date}",
            "",
            "ACADEMIC PERFORMANCE:",
            "-" * 30,
        ]
        if not self.subjects:
            lines.append("No subjects enrolled.")
        for subject, data in self.subjects.items():
            lines.extend([
                f"Subject: {subject}",
                f"  Teacher: {data['teacher']}",
                f"  Average Score: {self.calculate_subject_average(subject):.2f}",
                f"  Total Assessments: {len(data['scores'])}",
                "",
            ])

        lines.extend([f"Overall GPA: {self.calculate_overall_gpa():.2f}", ""])
        stats = self.get_attendance_statistics()
        lines.extend([
            "ATTENDANCE SUMMARY:",
            "-" * 30,
            f"Total Days: {stats['total_days']}",
            f"Present: {stats['present']}",
            f"Absent: {stats['absent']}",
            f"Late: {stats['late']}",
            f"Excused: {stats['excused']}",
            f"Attendance Percentage: {stats['percentage']:.2f}%",
        ])
        if self.achievements:
            lines.extend(["", "ACHIEVEMENTS:", "-" * 30])
            lines.extend(f"- {item['achievement']} ({item['date']})" for item in self.achievements)
        if self.disciplinary_actions:
            lines.extend(["", "DISCIPLINARY ACTIONS:", "-" * 30])
            lines.extend(f"- {item['action']} ({item['date']})" for item in self.disciplinary_actions)
        lines.append("=" * 60)
        return "\n".join(lines)

    def compare_with_student(self, other_student: "AdvancedStudent") -> None:
        """Print a GPA, attendance, and achievement comparison."""
        if not isinstance(other_student, AdvancedStudent):
            raise TypeError("other_student must be an AdvancedStudent")
        print(f"\nCOMPARISON: {self.name} vs {other_student.name}")
        print("=" * 50)
        stats = [
            (self, self.calculate_overall_gpa(), self.get_attendance_statistics()["percentage"]),
            (other_student, other_student.calculate_overall_gpa(), other_student.get_attendance_statistics()["percentage"]),
        ]
        for student, gpa, attendance in stats:
            print(f"{student.name}:")
            print(f"  GPA: {gpa:.2f}")
            print(f"  Attendance: {attendance:.2f}%")
            print(f"  Achievements: {len(student.achievements)}")
        print("\nComparison Results:")
        if stats[0][1] > stats[1][1]:
            print(f"  {self.name} has a higher GPA")
        elif stats[1][1] > stats[0][1]:
            print(f"  {other_student.name} has a higher GPA")
        else:
            print("  Both students have the same GPA")
        if stats[0][2] > stats[1][2]:
            print(f"  {self.name} has better attendance")
        elif stats[1][2] > stats[0][2]:
            print(f"  {other_student.name} has better attendance")
        else:
            print("  Both students have the same attendance rate")


def demo_advanced_students() -> None:
    """Run the advanced student examples from the lab."""
    student1 = AdvancedStudent("Emma Thompson", 16, "11th Grade", "ST001")
    student2 = AdvancedStudent("James Rodriguez", 16, "11th Grade", "ST002")

    for subject, teacher in [("Mathematics", "Dr. Smith"), ("Physics", "Prof. Johnson"), ("Chemistry", "Dr. Brown")]:
        student1.enroll_in_subject(subject, teacher)
    for subject, teacher in [("Mathematics", "Dr. Smith"), ("Physics", "Prof. Johnson"), ("English", "Ms. Davis")]:
        student2.enroll_in_subject(subject, teacher)

    for subject, score, kind in [
        ("Mathematics", 92, "Test"), ("Mathematics", 88, "Quiz"),
        ("Physics", 85, "Test"), ("Chemistry", 90, "Lab Report"),
    ]:
        student1.add_subject_score(subject, score, kind)
    for subject, score, kind in [
        ("Mathematics", 78, "Test"), ("Mathematics", 82, "Quiz"),
        ("Physics", 88, "Test"), ("English", 95, "Essay"),
    ]:
        student2.add_subject_score(subject, score, kind)

    dates = ["2024-01-15", "2024-01-16", "2024-01-17", "2024-01-18", "2024-01-19"]
    for attendance_date in dates:
        student1.mark_attendance(attendance_date, "Present")
        student2.mark_attendance(attendance_date, "Absent" if attendance_date == "2024-01-17" else "Present")
    student1.add_achievement("Honor Roll", "2024-01-20")
    student1.add_achievement("Science Fair Winner", "2024-01-25")
    student2.add_achievement("Math Competition Finalist", "2024-01-22")

    print("\n=== Generating Transcripts ===")
    print(student1.generate_transcript())
    print(student2.generate_transcript())
    print("\n=== Student Comparison ===")
    student1.compare_with_student(student2)


if __name__ == "__main__":
    demo_advanced_students()
