def is_even(number):
    return number % 2 == 0

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def factorial(number):
    if number < 0:
        raise ValueError("Factorial is undefined for negative integers")
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result

def process_scores(scores):
    if not scores:
        return {"count": 0, "average": 0, "highest": None, "lowest": None}
    return {
        "count": len(scores),
        "average": sum(scores) / len(scores),
        "highest": max(scores),
        "lowest": min(scores),
    }

def main():
    numbers = [3, 8, 11, 16, 20]
    print("Even/odd:", [(number, is_even(number)) for number in numbers])
    temperatures = [0, 20, 37, 100]
    print("Fahrenheit:", [celsius_to_fahrenheit(temp) for temp in temperatures])
    print("Factorials:", {number: factorial(number) for number in range(6)})
    print("Score report:", process_scores([78, 91, 64, 88]))

if __name__ == "__main__":
    main()
