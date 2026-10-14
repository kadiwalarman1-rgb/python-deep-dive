def calculate_rectangle(length, width):
    return length * width, 2 * (length + width)

def main():
    first, second = 17, 5
    print("=== ARITHMETIC ===")
    print("Addition:", first + second)
    print("Subtraction:", first - second)
    print("Multiplication:", first * second)
    print("Division:", first / second)
    print("Floor division:", first // second)
    print("Remainder:", first % second)
    print("Power:", second ** 2)

    print("\n=== COMPARISON ===")
    print(first > second, first == second, first != second)
    print(1 < second < 10)

    age = 22
    has_id = True
    is_eligible = age >= 18 and has_id
    is_student_discount = age < 25 or has_id is False
    print("\n=== LOGICAL OPERATORS ===")
    print("Eligible:", is_eligible)
    print("Student discount condition:", is_student_discount)
    print("Negated eligibility:", not is_eligible)

    area, perimeter = calculate_rectangle(8, 4)
    print("\n=== RECTANGLE ===")
    print("Area:", area)
    print("Perimeter:", perimeter)

if __name__ == "__main__":
    main()
