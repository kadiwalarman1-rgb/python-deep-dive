def analyze_text(text):
    words = {word.strip(".,!?;:").lower() for word in text.split()}
    return words

def main():
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7}
    print("Union:", set_a | set_b)
    print("Intersection:", set_a & set_b)
    print("Difference A-B:", set_a - set_b)
    print("Symmetric difference:", set_a ^ set_b)

    small = {1, 2}
    large = {1, 2, 3, 4}
    print("Subset:", small <= large)
    print("Proper subset:", small < large)
    print("Superset:", large >= small)
    print("Disjoint:", {1, 2}.isdisjoint({3, 4}))

    squares = {number ** 2 for number in range(1, 8)}
    multiples_of_three = {number for number in range(1, 21) if number % 3 == 0}
    print("Squares:", squares)
    print("Multiples of three:", multiples_of_three)

    text = "Python makes coding fun, and Python makes practice useful."
    print("Unique words:", analyze_text(text))
    duplicate_values = [4, 2, 4, 1, 2, 7, 7, 9]
    print("Deduplicated values:", sorted(set(duplicate_values)))

if __name__ == "__main__":
    main()
