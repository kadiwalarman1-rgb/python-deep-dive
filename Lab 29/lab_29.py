import csv
import json
import logging
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path

FIELDS = ["employee_id", "name", "department", "salary", "hire_date", "email"]
SAMPLE_EMPLOYEES = [
    [101, "John Smith", "Engineering", 75000, "2020-01-15", "john.smith@company.com"],
    [102, "Sarah Johnson", "Marketing", 65000, "2019-03-22", "sarah.johnson@company.com"],
    [103, "Mike Davis", "Engineering", 80000, "2018-07-10", "mike.davis@company.com"],
    [104, "Lisa Wilson", "HR", 60000, "2021-02-28", "lisa.wilson@company.com"],
    [105, "David Brown", "Finance", 70000, "2019-11-05", "david.brown@company.com"],
    [106, "Emily Taylor", "Marketing", 68000, "2020-09-12", "emily.taylor@company.com"],
    [107, "James Anderson", "Engineering", 85000, "2017-04-18", "james.anderson@company.com"],
    [108, "Maria Garcia", "HR", 62000, "2021-06-30", "maria.garcia@company.com"],
    [109, "Robert Miller", "Finance", 72000, "2018-12-03", "robert.miller@company.com"],
    [110, "Jennifer Lee", "Marketing", 66000, "2020-05-20", "jennifer.lee@company.com"],
]

class EmployeeManager:
    def __init__(self):
        self.employees = {}
        self.departments = {}
        self.salary_ranges = []
        self.processed_data = []
        self.batch_size = 1000
        logging.basicConfig(filename="lab29_output/employee_manager.log", level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
        self.logger = logging.getLogger("EmployeeManager")

    def _process_employee_row(self, row):
        try:
            employee_id = int(row["employee_id"])
            name = row["name"].strip()
            department = row["department"].strip()
            salary = float(row["salary"])
            hire_date = row["hire_date"].strip()
            email = row["email"].strip().lower()
            datetime.strptime(hire_date, "%Y-%m-%d")
            if employee_id <= 0:
                raise ValueError("Employee ID must be positive")
            if not name or not department:
                raise ValueError("Name and department cannot be empty")
            if salary < 0:
                raise ValueError("Salary cannot be negative")
            if "@" not in email or "." not in email:
                raise ValueError("Invalid email format")
            return {"employee_id": employee_id, "name": name, "department": department, "salary": salary, "hire_date": hire_date, "email": email, "processed_date": datetime.now().isoformat()}
        except (ValueError, KeyError, TypeError) as error:
            raise ValueError(f"Invalid employee record: {error}") from error

    def _add_to_department(self, employee):
        employee_id = employee["employee_id"]
        department = employee["department"]
        self.departments.setdefault(department, [])
        if employee_id not in self.departments[department]:
            self.departments[department].append(employee_id)

    def read_csv_data(self, filename):
        self.employees.clear()
        self.departments.clear()
        try:
            with open(filename, "r", newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                if not reader.fieldnames or not all(field in reader.fieldnames for field in FIELDS):
                    raise ValueError("CSV file is missing required columns")
                valid_count = 0
                for row_number, row in enumerate(reader, start=2):
                    try:
                        employee = self._process_employee_row(row)
                        employee_id = employee["employee_id"]
                        if employee_id in self.employees:
                            raise ValueError(f"Duplicate employee ID {employee_id}")
                        self.employees[employee_id] = employee
                        self._add_to_department(employee)
                        valid_count += 1
                    except ValueError as error:
                        print(f"Skipping row {row_number}: {error}")
                print(f"Loaded {valid_count} employee records")
                return True
        except FileNotFoundError:
            print(f"File not found: {filename}")
        except PermissionError:
            print(f"Permission denied: {filename}")
        except (OSError, csv.Error, ValueError) as error:
            print(f"CSV read error: {error}")
        return False

    def add_employee(self, data):
        try:
            employee = self._process_employee_row(data)
            employee_id = employee["employee_id"]
            if employee_id in self.employees:
                print(f"Employee {employee_id} already exists")
                return False
            self.employees[employee_id] = employee
            self._add_to_department(employee)
            return True
        except (ValueError, TypeError) as error:
            print(f"Add employee error: {error}")
            return False

    def remove_employee(self, employee_id):
        employee = self.employees.pop(employee_id, None)
        if employee is None:
            print(f"Employee {employee_id} not found")
            return False
        department = employee["department"]
        self.departments[department].remove(employee_id)
        if not self.departments[department]:
            del self.departments[department]
        return True

    def update_employee(self, employee_id, updates):
        if employee_id not in self.employees:
            print(f"Employee {employee_id} not found")
            return False
        old = self.employees[employee_id]
        candidate = {key: old[key] for key in FIELDS}
        for field, value in updates.items():
            if field not in FIELDS or field == "employee_id":
                print(f"Ignoring unsupported field: {field}")
                continue
            candidate[field] = value
        try:
            updated = self._process_employee_row(candidate)
        except ValueError as error:
            print(f"Update employee error: {error}")
            return False
        if updated["department"] != old["department"]:
            old_department = old["department"]
            self.departments[old_department].remove(employee_id)
            if not self.departments[old_department]:
                del self.departments[old_department]
            self._add_to_department(updated)
        self.employees[employee_id] = updated
        return True

    def search_employees(self, criteria):
        results = []
        for employee in self.employees.values():
            matched = True
            for field, expected in criteria.items():
                if field not in employee:
                    matched = False
                    break
                actual = employee[field]
                if field in {"name", "department", "email"}:
                    matched = str(expected).lower() in str(actual).lower()
                elif field == "salary" and isinstance(expected, dict):
                    matched = expected.get("min", float("-inf")) <= actual <= expected.get("max", float("inf"))
                elif field == "salary":
                    matched = actual == float(expected)
                else:
                    matched = actual == expected
                if not matched:
                    break
            if matched:
                results.append(employee.copy())
        return results

    def analyze_salary_data(self):
        salaries = [employee["salary"] for employee in self.employees.values()]
        if not salaries:
            return {}
        range_counts = {
            "under_60k": sum(salary < 60000 for salary in salaries),
            "60k_to_80k": sum(60000 <= salary < 80000 for salary in salaries),
            "over_80k": sum(salary >= 80000 for salary in salaries),
        }
        department_averages = {}
        for department, employee_ids in self.departments.items():
            department_salaries = [self.employees[employee_id]["salary"] for employee_id in employee_ids]
            department_averages[department] = {"average": sum(department_salaries) / len(department_salaries), "count": len(department_salaries)}
        return {"total_employees": len(salaries), "average_salary": sum(salaries) / len(salaries), "min_salary": min(salaries), "max_salary": max(salaries), "salary_ranges": range_counts, "department_averages": department_averages}

    def write_to_json(self, filename, include_analysis=True):
        try:
            payload = {"metadata": {"export_date": datetime.now().isoformat(), "total_employees": len(self.employees), "departments": sorted(self.departments)}, "employees": self.employees, "departments": self.departments}
            if include_analysis:
                payload["salary_analysis"] = self.analyze_salary_data()
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(payload, file, indent=2, ensure_ascii=False)
            return True
        except (OSError, TypeError, ValueError) as error:
            print(f"JSON write error: {error}")
            return False

    def write_to_csv(self, filename, include_processed_date=False):
        fieldnames = FIELDS + (["processed_date"] if include_processed_date else [])
        try:
            with open(filename, "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for employee in self.employees.values():
                    writer.writerow({field: employee[field] for field in fieldnames if field in employee})
            return True
        except (OSError, csv.Error) as error:
            print(f"CSV write error: {error}")
            return False

    def write_to_text(self, filename, format_type="detailed"):
        if format_type not in {"detailed", "summary", "report"}:
            print(f"Unknown text report format: {format_type}")
            return False
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write("EMPLOYEE DATA REPORT\n")
                file.write(f"Generated: {datetime.now():%Y-%m-%d %H:%M:%S}\n")
                file.write(f"Total employees: {len(self.employees)}\n\n")
                if format_type == "detailed":
                    for employee_id, employee in sorted(self.employees.items()):
                        file.write(f"ID: {employee_id}\nName: {employee['name']}\nDepartment: {employee['department']}\nSalary: {employee['salary']:,.2f} USD\nHire date: {employee['hire_date']}\nEmail: {employee['email']}\n{'-' * 30}\n")
                else:
                    for department, employee_ids in sorted(self.departments.items()):
                        file.write(f"{department} ({len(employee_ids)} employees)\n")
                        for employee_id in sorted(employee_ids):
                            employee = self.employees[employee_id]
                            file.write(f"  {employee_id}: {employee['name']} - {employee['salary']:,.2f} USD\n")
                if format_type == "report":
                    analysis = self.analyze_salary_data()
                    file.write(f"\nAverage salary: {analysis.get('average_salary', 0):,.2f} USD\n")
                    file.write(f"Minimum salary: {analysis.get('min_salary', 0):,.2f} USD\n")
                    file.write(f"Maximum salary: {analysis.get('max_salary', 0):,.2f} USD\n")
                    file.write(f"Salary ranges: {analysis.get('salary_ranges', {})}\n")
            return True
        except OSError as error:
            print(f"Text report error: {error}")
            return False

    def export_all_formats(self, base_filename):
        return {
            "json": self.write_to_json(f"{base_filename}.json"),
            "csv": self.write_to_csv(f"{base_filename}_updated.csv", include_processed_date=True),
            "text_detailed": self.write_to_text(f"{base_filename}_detailed.txt", "detailed"),
            "text_summary": self.write_to_text(f"{base_filename}_summary.txt", "summary"),
            "text_report": self.write_to_text(f"{base_filename}_report.txt", "report"),
        }

    def read_large_csv_data(self, filename):
        total = 0
        errors = 0
        batch = []
        try:
            with open(filename, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                if not reader.fieldnames or not all(field in reader.fieldnames for field in FIELDS):
                    raise ValueError("CSV file is missing required columns")
                for row_number, row in enumerate(reader, start=2):
                    try:
                        batch.append(self._process_employee_row(row))
                    except ValueError as error:
                        errors += 1
                        self.logger.warning("Skipping row %s: %s", row_number, error)
                    if len(batch) >= self.batch_size:
                        self._process_batch(batch)
                        total += len(batch)
                        batch = []
                if batch:
                    self._process_batch(batch)
                    total += len(batch)
            print(f"Batch processing complete: {total} valid records; {errors} invalid records")
            return {"processed": total, "errors": errors}
        except (OSError, csv.Error, ValueError) as error:
            print(f"Large CSV processing error: {error}")
            return {"processed": total, "errors": errors + 1}

    def _process_batch(self, batch):
        self.processed_data.extend(batch)

@contextmanager
def safe_file_operation(filename, mode="r"):
    file = None
    try:
        if "b" in mode:
            file = open(filename, mode)
        else:
            file = open(filename, mode, newline="", encoding="utf-8")
        yield file
    finally:
        if file is not None:
            file.close()

def create_large_csv(filename, record_count):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        for index in range(record_count):
            writer.writerow({"employee_id": 1000 + index, "name": f"Employee {index}", "department": ["Engineering", "Marketing", "HR", "Finance"][index % 4], "salary": 45000 + index % 60000, "hire_date": "2022-01-15", "email": f"employee{index}@company.com"})

def main():
    output_dir = Path("lab29_output")
    output_dir.mkdir(exist_ok=True)
    csv_path = output_dir / "employees.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(FIELDS)
        writer.writerows(SAMPLE_EMPLOYEES)

    manager = EmployeeManager()
    if not manager.read_csv_data(csv_path):
        return
    manager.add_employee({"employee_id": 111, "name": "Alice Cooper", "department": "IT", "salary": 78000, "hire_date": "2022-01-15", "email": "alice.cooper@company.com"})
    manager.update_employee(111, {"salary": 82000, "department": "Engineering"})
    print("Engineering employees:", len(manager.search_employees({"department": "Engineering"})))
    print("Salary analysis:", json.dumps(manager.analyze_salary_data(), indent=2))
    manager.remove_employee(111)
    print("Employee count after removal:", len(manager.employees))
    results = manager.export_all_formats(output_dir / "employee_data_export")
    print("Export results:", results)

    large_csv = output_dir / "large_employees.csv"
    create_large_csv(large_csv, 2500)
    batch_manager = EmployeeManager()
    batch_manager.batch_size = 1000
    print("Large dataset result:", batch_manager.read_large_csv_data(large_csv))
    with safe_file_operation(output_dir / "safe_operation.txt", "w") as file:
        file.write("Safe file operation completed.\n")
    print("Safe file operation:", (output_dir / "safe_operation.txt").read_text(encoding="utf-8").strip())

if __name__ == "__main__":
    main()
