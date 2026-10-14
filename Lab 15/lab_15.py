def calculate(first, second, operator):
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        if second == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return first / second
    raise ValueError("Supported operators are +, -, *, and /")

def run_calculations(calculations):
    results = []
    for first, operator, second in calculations:
        try:
            result = calculate(first, second, operator)
            results.append({"expression": f"{first} {operator} {second}", "result": result, "status": "success"})
        except (ValueError, ZeroDivisionError) as error:
            results.append({"expression": f"{first} {operator} {second}", "result": None, "status": str(error)})
    return results

def main():
    examples = [(10, "+", 5), (12, "*", 3), (8, "/", 2), (4, "/", 0), (7, "%", 2)]
    for item in run_calculations(examples):
        print(item["expression"], "=>", item["result"], "[", item["status"], "]")

if __name__ == "__main__":
    main()
