def main():
    student_name = "Alex Johnson"
    student_age = 20
    gpa = 3.85
    is_enrolled = True
    print("=== STUDENT DATA ===")
    print(f"Name: {student_name} ({type(student_name).__name__})")
    print(f"Age: {student_age} ({type(student_age).__name__})")
    print(f"GPA: {gpa} ({type(gpa).__name__})")
    print(f"Enrolled: {is_enrolled} ({type(is_enrolled).__name__})")

    first_name = "Sarah"
    last_name = "Khan"
    full_name = first_name + " " + last_name
    print("\n=== STRING OPERATIONS ===")
    print("Full name:", full_name)
    print("Uppercase:", full_name.upper())
    print("Name length:", len(full_name))

    price = 19.99
    quantity = 3
    subtotal = price * quantity
    tax = subtotal * 0.05
    print("\n=== NUMERIC OPERATIONS ===")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Tax: {tax:.2f}")
    print(f"Total: {subtotal + tax:.2f}")

    print("\n=== TYPE CONVERSION ===")
    age_text = "21"
    score_text = "92.5"
    print("Age plus one:", int(age_text) + 1)
    print("Rounded score:", round(float(score_text)))
    print("Number to string:", str(student_age))
    try:
        int("twenty")
    except ValueError as error:
        print("Conversion handled:", error)

if __name__ == "__main__":
    main()
