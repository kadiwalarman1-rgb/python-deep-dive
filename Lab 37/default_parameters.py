"""Employee constructor defaults, ratings, and project examples."""


class Employee:
    """Represent an employee with optional constructor parameters."""

    def __init__(self, name, employee_id, department="General", position="Staff",
                 salary=50000, hire_date=None, email=None):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Employee name cannot be empty")
        if not isinstance(employee_id, str) or not employee_id.strip():
            raise ValueError("Employee ID cannot be empty")
        if not isinstance(department, str) or not department.strip():
            raise ValueError("Department cannot be empty")
        if not isinstance(position, str) or not position.strip():
            raise ValueError("Position cannot be empty")
        if isinstance(salary, bool) or not isinstance(salary, (int, float)) or salary < 0:
            raise ValueError("Salary must be non-negative")
        self.name = name.strip()
        self.employee_id = employee_id.strip()
        self.department = department.strip()
        self.position = position.strip()
        self.salary = float(salary)
        self.hire_date = hire_date.strip() if isinstance(hire_date, str) and hire_date.strip() else "Not specified"
        self.email = email.strip() if isinstance(email, str) and email.strip() else (
            f"{self.name.lower().replace(' ', '.')}@company.com"
        )
        self.is_active = True
        self.performance_ratings = []
        self.projects = []

    def add_performance_rating(self, rating, review_period):
        """Record a performance rating between 1 and 5."""
        if isinstance(rating, bool) or not isinstance(rating, (int, float)) or not 1 <= rating <= 5:
            return "Rating must be between 1 and 5"
        if not isinstance(review_period, str) or not review_period.strip():
            return "Review period cannot be empty"
        self.performance_ratings.append({"rating": float(rating), "period": review_period.strip()})
        return f"Performance rating {rating}/5 added for {review_period.strip()}"

    def assign_project(self, project_name, start_date):
        """Assign a project to the employee."""
        if not isinstance(project_name, str) or not project_name.strip():
            return "Project name cannot be empty"
        if not isinstance(start_date, str) or not start_date.strip():
            return "Start date cannot be empty"
        project = {"name": project_name.strip(), "start_date": start_date.strip(), "status": "Active"}
        self.projects.append(project)
        return f"Project '{project['name']}' assigned to {self.name}"

    def calculate_average_rating(self):
        """Return average performance rating, or zero before the first review."""
        if not self.performance_ratings:
            return 0.0
        return sum(item["rating"] for item in self.performance_ratings) / len(self.performance_ratings)

    def set_active(self, active):
        """Set employee active status."""
        if not isinstance(active, bool):
            raise ValueError("Active status must be True or False")
        self.is_active = active
        return f"{self.name} is now {'active' if active else 'inactive'}"

    def complete_project(self, project_name):
        """Mark a project as completed if it exists."""
        for project in self.projects:
            if project["name"].casefold() == str(project_name).casefold():
                project["status"] = "Completed"
                return f"Project '{project['name']}' marked as completed"
        return f"Project '{project_name}' not found"

    def display_employee_info(self):
        """Display employee details, review score, and assigned projects."""
        print("=" * 55)
        print("EMPLOYEE INFORMATION")
        print("=" * 55)
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print(f"Position: {self.position}")
        print(f"Salary: USD {self.salary:,.2f}")
        print(f"Hire Date: {self.hire_date}")
        print(f"Email: {self.email}")
        print(f"Status: {'Active' if self.is_active else 'Inactive'}")
        print(f"Average Performance Rating: {self.calculate_average_rating():.2f}/5.00")
        if self.projects:
            print("\nPROJECTS:")
            for index, project in enumerate(self.projects, 1):
                print(f"{index}. {project['name']} — {project['status']} (Start: {project['start_date']})")
        else:
            print("\nNo projects assigned")
        print("=" * 55)


def demo_employees():
    """Demonstrate both default and explicitly supplied constructor values."""
    employees = [
        Employee("Alice Johnson", "EMP001"),
        Employee("Bob Smith", "EMP002", "Engineering", "Python Developer", 72000,
                 "2024-04-15", "bob.smith@example.com"),
        Employee("Carol Davis", "EMP003", department="Human Resources", position="HR Specialist"),
    ]
    employees[0].add_performance_rating(4, "2026 Q1")
    employees[0].add_performance_rating(5, "2026 Q2")
    employees[0].assign_project("Onboarding Portal", "2026-01-15")
    employees[0].complete_project("Onboarding Portal")
    employees[1].add_performance_rating(4.5, "2026 Mid-Year")
    employees[1].assign_project("Automation Toolkit", "2026-03-01")
    for employee in employees:
        employee.display_employee_info()
        print()


if __name__ == "__main__":
    demo_employees()
