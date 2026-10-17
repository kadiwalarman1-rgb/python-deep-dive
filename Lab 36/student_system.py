class Student:
    def __init__(self, student_id, name, age, major="Undeclared"):
        if not isinstance(student_id, str) or not student_id.strip():
            raise ValueError("Student ID cannot be empty")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name cannot be empty")
        if not isinstance(age, int) or isinstance(age, bool) or age < 0:
            raise ValueError("Age must be a non-negative integer")
        self.student_id = student_id.strip()
        self.name = name.strip()
        self.age = age
        self.major = major
        self.grades = {}
        self.enrolled_courses = []

    def display_profile(self):
        print("=== Student Profile ===")
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Major: {self.major}")
        print(f"Enrolled Courses: {len(self.enrolled_courses)}")
        if self.enrolled_courses:
            print(f"Courses: {', '.join(self.enrolled_courses)}")
        print(f"Subjects with Grades: {len(self.grades)}")
        print("=" * 25)

    def enroll_course(self, course_name):
        if not isinstance(course_name, str) or not course_name.strip():
            raise ValueError("Course name cannot be empty")
        course_name = course_name.strip()
        if course_name not in self.enrolled_courses:
            self.enrolled_courses.append(course_name)
            print(f"{self.name} enrolled in {course_name}")
            return True
        print(f"{self.name} is already enrolled in {course_name}")
        return False

    def add_grade(self, subject, grade):
        if not isinstance(subject, str) or not subject.strip():
            raise ValueError("Subject cannot be empty")
        if not isinstance(grade, (int, float)) or isinstance(grade, bool) or not 0 <= grade <= 100:
            print("Grade must be between 0 and 100")
            return False
        self.grades[subject.strip()] = float(grade)
        print(f"Grade {grade} added for {self.name} in {subject.strip()}")
        return True

    def calculate_gpa(self):
        if not self.grades:
            return 0.0
        total_points = 0.0
        for grade in self.grades.values():
            if grade >= 90:
                total_points += 4.0
            elif grade >= 80:
                total_points += 3.0
            elif grade >= 70:
                total_points += 2.0
            elif grade >= 60:
                total_points += 1.0
        return round(total_points / len(self.grades), 2)

    def display_grades(self):
        print(f"\n--- {self.name}'s Academic Record ---")
        if self.grades:
            for subject, grade in self.grades.items():
                print(f"{subject}: {grade:g}")
            print(f"GPA: {self.calculate_gpa():.2f}")
        else:
            print("No grades recorded yet.")
        print("-" * 30)

    def change_major(self, new_major):
        if not isinstance(new_major, str) or not new_major.strip():
            raise ValueError("Major cannot be empty")
        old_major = self.major
        self.major = new_major.strip()
        print(f"{self.name} changed major from {old_major} to {self.major}")

    def get_academic_status(self):
        gpa = self.calculate_gpa()
        if gpa >= 3.5:
            return "Dean's List"
        if gpa >= 3.0:
            return "Good Standing"
        if gpa >= 2.0:
            return "Satisfactory"
        return "Academic Probation"


if __name__ == "__main__":
    print("=== Student Management System Demo ===\n")
    student1 = Student("S001", "Alice Johnson", 20, "Computer Science")
    student2 = Student("S002", "Bob Smith", 19, "Mathematics")
    student3 = Student("S003", "Carol Davis", 21)

    print("Initial Student Profiles:")
    for student in (student1, student2, student3):
        student.display_profile()

    print("\n=== Course Enrollment ===")
    student1.enroll_course("Data Structures")
    student1.enroll_course("Algorithms")
    student1.enroll_course("Database Systems")
    student2.enroll_course("Calculus II")
    student2.enroll_course("Linear Algebra")
    student3.enroll_course("English Literature")
    student3.change_major("English")

    print("\n=== Adding Grades ===")
    student1.add_grade("Data Structures", 92)
    student1.add_grade("Algorithms", 88)
    student1.add_grade("Database Systems", 95)
    student2.add_grade("Calculus II", 85)
    student2.add_grade("Linear Algebra", 78)
    student3.add_grade("English Literature", 91)

    print("\n=== Academic Records ===")
    for student in (student1, student2, student3):
        student.display_grades()

    print("=== Academic Status ===")
    students = (student1, student2, student3)
    for student in students:
        print(f"{student.name}: {student.get_academic_status()} (GPA: {student.calculate_gpa():.2f})")

    print("\n=== Final Student Profiles ===")
    for student in students:
        student.display_profile()
