def categorize_ages(ages):
    categories = {"child": [], "teen": [], "adult": []}
    for age in ages:
        if age < 13:
            categories["child"].append(age)
        elif age < 20:
            categories["teen"].append(age)
        else:
            categories["adult"].append(age)
    return categories

def find_primes(start, end):
    primes = []
    for number in range(max(2, start), end + 1):
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                break
        else:
            primes.append(number)
    return primes

def filtered_pairs(values):
    pairs = []
    for first in values:
        for second in values:
            if first == second:
                continue
            if first + second > 10:
                break
            pairs.append((first, second))
    return pairs

def main():
    print("Age categories:", categorize_ages([5, 12, 13, 17, 19, 25, 41]))
    print("Primes from 1 to 50:", find_primes(1, 50))
    print("Filtered pairs:", filtered_pairs([1, 2, 4, 7]))

if __name__ == "__main__":
    main()
