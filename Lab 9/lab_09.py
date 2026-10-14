message_prefix = "Result"

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

def calculate(first, second, operation="add"):
    operations = {
        "add": lambda: first + second,
        "subtract": lambda: first - second,
        "multiply": lambda: first * second,
    }
    if operation == "divide":
        if second == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return first / second
    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")
    return operations[operation]()

def scope_demo():
    local_message = "I exist inside this function"
    return local_message, message_prefix

def average(*numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    print(greet("Arman"))
    print(greet("Python learner", "Welcome"))
    print("Addition:", calculate(10, 5))
    print("Multiplication:", calculate(10, 5, "multiply"))
    print("Division:", calculate(10, 4, "divide"))
    print("Average:", average(10, 20, 30, 40))
    local_value, global_value = scope_demo()
    print(local_value)
    print(global_value)

if __name__ == "__main__":
    main()
