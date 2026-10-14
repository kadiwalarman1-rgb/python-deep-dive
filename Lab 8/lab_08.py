def categorize_number(number):
    if number < 0:
        return "negative"
    if number == 0:
        return "zero"
    if number % 2 == 0:
        return "positive even"
    return "positive odd"

def find_primes(limit):
    primes = []
    for number in range(2, limit + 1):
        is_prime = True
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return primes

def main():
    values = [-3, 0, 4, 7, 10, 13]
    print("=== CATEGORIZATION ===")
    for value in values:
        print(value, "is", categorize_number(value))

    print("\n=== CONTINUE AND BREAK ===")
    for value in range(1, 11):
        if value % 2 == 0:
            continue
        if value > 7:
            break
        print(value)

    countdown = 3
    while countdown > 0:
        print("Countdown:", countdown)
        countdown -= 1
    print("Go!")
    print("Primes through 30:", find_primes(30))

if __name__ == "__main__":
    main()
