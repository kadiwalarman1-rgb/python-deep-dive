"""Unit tests for the Lab 38 student classes and management system."""

import unittest

from advanced_student import AdvancedStudent
from student_manager import Student
from student_system import StudentManagementSystem


class StudentTests(unittest.TestCase):
    def test_average_and_grade_point(self) -> None:
        student = Student("Test Student", 16, "10th Grade")
        self.assertEqual(student.calculate_average_score(), 0.0)
        student.add_test_score(80)
        student.add_test_score(100)
        self.assertEqual(student.calculate_average_score(), 90.0)
        self.assertEqual(student.get_grade_point(), 4.0)

    def test_invalid_scores_and_attendance_are_rejected(self) -> None:
        student = Student("Test Student", 16, "10th Grade")
        self.assertFalse(student.add_test_score(101))
        self.assertFalse(student.add_test_score(-1))
        self.assertFalse(student.add_attendance(0))
        self.assertEqual(student.test_scores, [])
        self.assertEqual(student.attendance, 0)

    def test_attendance_limit(self) -> None:
        student = Student("Test Student", 16, "10th Grade")
        self.assertTrue(student.add_attendance(180))
        self.assertFalse(student.add_attendance(1))
        self.assertEqual(student.calculate_attendance_percentage(), 100.0)


class AdvancedStudentTests(unittest.TestCase):
    def test_gpa_ignores_subjects_without_scores(self) -> None:
        student = AdvancedStudent("Test Student", 16, "11th Grade", "ST001")
        student.enroll_in_subject("Math", "Teacher A")
        student.enroll_in_subject("History", "Teacher B")
        student.add_subject_score("Math", 95)
        self.assertEqual(student.calculate_overall_gpa(), 4.0)

    def test_attendance_statistics(self) -> None:
        student = AdvancedStudent("Test Student", 16, "11th Grade", "ST001")
        student.mark_attendance("2024-01-01", "Present")
        student.mark_attendance("2024-01-02", "Excused")
        student.mark_attendance("2024-01-03", "Absent")
        stats = student.get_attendance_statistics()
        self.assertEqual(stats["total_days"], 3)
        self.assertAlmostEqual(stats["percentage"], 200 / 3)

    def test_duplicate_attendance_date_is_rejected(self) -> None:
        student = AdvancedStudent("Test Student", 16, "11th Grade", "ST001")
        self.assertTrue(student.mark_attendance("2024-01-01", "Present"))
        self.assertFalse(student.mark_attendance("2024-01-01", "Absent"))
        self.assertEqual(len(student.attendance_record), 1)


class StudentManagementSystemTests(unittest.TestCase):
    def test_ids_and_lookup(self) -> None:
        system = StudentManagementSystem()
        first_id = system.add_student("Alice", 16, "11th Grade")
        second_id = system.add_student("Bob", 17, "12th Grade")
        self.assertEqual(first_id, "ST001")
        self.assertEqual(second_id, "ST002")
        self.assertEqual(system.get_student(first_id).name, "Alice")
        self.assertIsNone(system.get_student("ST999"))

    def test_top_performers_sorted_by_gpa(self) -> None:
        system = StudentManagementSystem()
        ids = [system.add_student(name, 16, "11th Grade") for name in ("Alice", "Bob")]
        alice = system.get_student(ids[0])
        bob = system.get_student(ids[1])
        alice.enroll_in_subject("Math", "Teacher")
        bob.enroll_in_subject("Math", "Teacher")
        alice.add_subject_score("Math", 80)
        bob.add_subject_score("Math", 95)
        top = system.find_top_performers(1)
        self.assertEqual(top[0][0], "Bob")


if __name__ == "__main__":
    unittest.main(verbosity=2)
