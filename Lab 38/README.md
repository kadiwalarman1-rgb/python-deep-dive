# Lab 38: Methods and Functions — Defining and Calling Methods

## Objectives

- Define and call instance methods inside a Python class.
- Read and update object attributes through methods.
- Perform calculations using multiple attributes and return results.
- Call methods on multiple instances and compare their independent state.
- Combine several methods into a practical student-management example.

## Files

| File | Purpose |
|---|---|
| student_manager.py | Basic Student class, setters/getters, score and attendance calculations. |
| test_students.py | Demonstrates methods on multiple students and a sequence of method calls. |
| advanced_student.py | Subject-wise scores, GPA, attendance statistics, transcripts, achievements, and comparisons. |
| student_system.py | Stores students in a management system and generates class reports and top-performer lists. |
| test_student_management.py | Automated regression tests for core behaviors and validation rules. |

## Run the Lab

Run these commands from this directory using Python 3.10 or newer:

    python3 student_manager.py
    python3 test_students.py
    python3 advanced_student.py
    python3 student_system.py
    python3 -m unittest -v test_student_management.py

No third-party packages are required.

## Key Concepts

- self refers to the current object and gives a method access to its attributes.
- __init__() initializes each new instance with its own data.
- Methods such as set_age(), add_test_score(), and mark_attendance() validate input before changing state.
- Calculation methods such as calculate_average_score() and calculate_overall_gpa() return values that other methods can reuse.
- get_performance_summary() returns a dictionary, while generate_transcript() returns a formatted string.
- StudentManagementSystem composes these methods to create class-level reports.

## Calculation Rules Used in This Lab

- The basic Student class assumes 180 school days in a school year.
- Basic grade points use these thresholds: 90–100 → 4.0, 80–89.99 → 3.0, 70–79.99 → 2.0, 60–69.99 → 1.0, below 60 → 0.0.
- The advanced GPA is the unweighted average of grade points for subjects that have at least one recorded score.
- The advanced attendance percentage counts Present and Excused days as good attendance, matching the lab's stated rule.
- Student-management data is held in memory for the duration of the program; it is not saved to a database or file.

## Example Workflow

1. Create a student object.
2. Use methods to add attendance and scores.
3. Call calculation methods to retrieve averages, grade points, and summaries.
4. Enroll an AdvancedStudent in subjects and record attendance.
5. Use StudentManagementSystem to list students, generate a class report, and identify top performers.
