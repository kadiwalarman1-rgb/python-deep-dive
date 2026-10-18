"""Student class demonstrating instance methods and calculated properties."""


class Student:
    """Store a student's details, scores, and attendance."""

    def __init__(self, name: str, age: int, grade: str) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name cannot be empty")
        if not isinstance(age, int) or isinstance(age, bool) or age <= 0:
            raise ValueError("Age must be a positive integer")
        if not isinstance(grade, str) or not grade.strip():
            raise ValueError("Grade cannot be empty")

        self.name = name.strip()
        self.age = age
        self.grade = grade.strip()
        self.attendance = 0
        self.test_scores: list[float] = []
        self.total_school_days = 180

    def display_info(self) -> None:
        """Print the student's current information."""
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
        print(f"Attendance: {self.attendance} days")
        print(f"Test Scores: {self.test_scores}")

    def get_name(self) -> str:
        """Return the student's name."""
        return self.name

    def get_age(self) -> int:
        """Return the student's age."""
        return self.age

    def set_name(self, new_name: str) -> bool:
        """Update the student's name; return False for invalid input."""
        if not isinstance(new_name, str) or not new_name.strip():
            print("Name cannot be empty")
            return False
        old_name = self.name
        self.name = new_name.strip()
        print(f"Name changed from '{old_name}' to '{self.name}'")
        return True

    def set_age(self, new_age: int) -> bool:
        """Update the student's age after validating it."""
        if not isinstance(new_age, int) or isinstance(new_age, bool) or new_age <= 0:
            print("Age must be a positive integer")
            return False
        old_age = self.age
        self.age = new_age
        print(f"Age updated from {old_age} to {new_age}")
        return True

    def add_attendance(self, days: int) -> bool:
        """Add attended school days without exceeding the school-year limit."""
        if not isinstance(days, int) or isinstance(days, bool) or days <= 0:
            print("Attendance days must be a positive integer")
            return False
        if self.attendance + days > self.total_school_days:
            print(f"Attendance cannot exceed {self.total_school_days} school days")
            return False
        self.attendance += days
        print(f"Added {days} attendance days. Total: {self.attendance}")
        return True

    def add_test_score(self, score: float) -> bool:
        """Add a test score in the inclusive range 0 to 100."""
        if isinstance(score, bool) or not isinstance(score, (int, float)) or not 0 <= score <= 100:
            print("Test score must be a number between 0 and 100")
            return False
        self.test_scores.append(float(score))
        print(f"Test score {score} added successfully")
        return True

    def calculate_average_score(self) -> float:
        """Return the mean test score, or zero when no scores exist."""
        if not self.test_scores:
            return 0.0
        return sum(self.test_scores) / len(self.test_scores)

    def calculate_attendance_percentage(self) -> float:
        """Return attendance as a percentage of total school days."""
        if self.total_school_days <= 0:
            return 0.0
        return (self.attendance / self.total_school_days) * 100

    def get_grade_point(self) -> float:
        """Convert the average score to the lab's 4.0 grade-point scale."""
        average = self.calculate_average_score()
        if average >= 90:
            return 4.0
        if average >= 80:
            return 3.0
        if average >= 70:
            return 2.0
        if average >= 60:
            return 1.0
        return 0.0

    def get_performance_summary(self) -> dict[str, float | int]:
        """Return a compact summary built from the student's stored data."""
        return {
            "average_score": round(self.calculate_average_score(), 2),
            "attendance_percentage": round(self.calculate_attendance_percentage(), 2),
            "grade_point": self.get_grade_point(),
            "total_tests": len(self.test_scores),
        }


if __name__ == "__main__":
    student1 = Student("Alice Johnson", 16, "10th Grade")

    print("=== Initial Student Information ===")
    student1.display_info()
    print(f"\nStudent's name: {student1.get_name()}")
    print(f"Student's age: {student1.get_age()}")

    print("\n=== Updating Student Information ===")
    student1.set_name("Alice Smith")
    student1.set_age(17)
    student1.add_attendance(15)
    student1.add_test_score(85)
    student1.add_test_score(92)

    print("\n=== Updated Student Information ===")
    student1.display_info()
    print(f"Average Score: {student1.calculate_average_score():.2f}")
    print(f"Attendance: {student1.calculate_attendance_percentage():.2f}%")
    print(f"Grade Point: {student1.get_grade_point():.1f}")
    print(f"Performance Summary: {student1.get_performance_summary()}")
