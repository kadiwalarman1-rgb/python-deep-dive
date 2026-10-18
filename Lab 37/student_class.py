"""Student constructor and formatted-profile demonstrations."""


class Student:
    """Store a student's identity, major, courses, credits, and GPA."""

    def __init__(self, name, age, student_id, major="Undeclared"):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name cannot be empty")
        if not isinstance(age, int) or isinstance(age, bool) or age <= 0:
            raise ValueError("Age must be a positive integer")
        if not isinstance(student_id, str) or not student_id.strip():
            raise ValueError("Student ID cannot be empty")
        if not isinstance(major, str) or not major.strip():
            raise ValueError("Major cannot be empty")
        self.name = name.strip()
        self.age = age
        self.student_id = student_id.strip()
        self.major = major.strip()
        self.courses = []
        self.gpa = 0.0
        self.credits = 0

    def add_course(self, course_name, credits=3):
        """Enroll in a course and track credit hours."""
        if not isinstance(course_name, str) or not course_name.strip():
            raise ValueError("Course name cannot be empty")
        if not isinstance(credits, int) or isinstance(credits, bool) or credits <= 0:
            raise ValueError("Credits must be a positive integer")
        normalized_name = course_name.strip()
        if any(course["name"].casefold() == normalized_name.casefold() for course in self.courses):
            return False
        self.courses.append({"name": normalized_name, "credits": credits})
        self.credits += credits
        return True

    def get_info(self):
        """Return basic student information."""
        return f"Student: {self.name}, Age: {self.age}, ID: {self.student_id}"

    def display_basic_info(self):
        """Display core student attributes."""
        print("=" * 50)
        print("STUDENT INFORMATION")
        print("=" * 50)
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"Major: {self.major}")
        print(f"Total Credits: {self.credits}")
        print(f"GPA: {self.gpa:.2f}")

    def display_courses(self):
        """Display the enrolled course list."""
        print("\nENROLLED COURSES:")
        print("-" * 30)
        if not self.courses:
            print("No courses enrolled")
        else:
            for index, course in enumerate(self.courses, 1):
                print(f"{index}. {course['name']} ({course['credits']} credits)")

    def display_full_profile(self):
        """Display the full student profile."""
        self.display_basic_info()
        self.display_courses()
        print("=" * 50)

    def update_gpa(self, new_gpa):
        """Update GPA only when it is numeric and within 0 to 4."""
        if isinstance(new_gpa, bool) or not isinstance(new_gpa, (int, float)) or not 0 <= new_gpa <= 4:
            print("Invalid GPA. Must be between 0.0 and 4.0")
            return False
        self.gpa = float(new_gpa)
        print(f"GPA updated to {self.gpa:.2f}")
        return True


def create_multiple_students():
    """Create independent students with different constructor values."""
    students = [
        Student("Alice Johnson", 20, "STU001", "Computer Science"),
        Student("Bob Smith", 19, "STU002", "Physics"),
        Student("Carol Davis", 21, "STU003", "Biology"),
        Student("David Wilson", 18, "STU004"),
    ]
    students[0].add_course("Computer Science", 3)
    students[0].add_course("Mathematics", 4)
    students[1].add_course("Physics", 4)
    students[1].add_course("Chemistry", 3)
    students[2].add_course("Biology", 3)
    students[2].add_course("Statistics", 3)
    students[3].add_course("English Literature", 3)
    return students


def demo_students():
    """Run the Student class examples."""
    basic_student = Student("Alice Johnson", 20, "STU001")
    print(basic_student.get_info())
    print(f"Courses enrolled: {basic_student.courses}")
    print("\n=== Multiple Student Profiles ===")
    for number, student in enumerate(create_multiple_students(), 1):
        course_names = ", ".join(course["name"] for course in student.courses) or "None"
        print(f"{number}. {student.get_info()}")
        print(f"   Courses: {course_names}")
    print("\n=== Formatted Profiles ===")
    students = [
        Student("Emma Thompson", 20, "CS001", "Computer Science"),
        Student("Michael Chen", 19, "BIO002", "Biology"),
        Student("Sarah Williams", 21, "ENG003", "English Literature"),
    ]
    for course, credits in [("Data Structures", 4), ("Algorithms", 3), ("Database Systems", 3)]:
        students[0].add_course(course, credits)
    students[0].update_gpa(3.75)
    students[1].add_course("Organic Chemistry", 4)
    students[1].add_course("Molecular Biology", 3)
    students[1].update_gpa(3.60)
    students[2].add_course("Shakespeare Studies", 3)
    students[2].add_course("Modern Poetry", 3)
    students[2].add_course("Creative Writing", 2)
    students[2].update_gpa(3.85)
    for student in students:
        student.display_full_profile()
        print()


if __name__ == "__main__":
    demo_students()
