def main():
    numbers = list(range(1, 11))
    squares = [number ** 2 for number in numbers]
    odd_numbers = [number for number in numbers if number % 2 != 0]
    large_odd_squares = [number ** 2 for number in numbers if number % 2 != 0 and number > 5]
    words = ["python", "list", "comprehension", "code", "practice"]
    long_words = [word for word in words if len(word) >= 5]
    capitalized = [word.title() for word in words]
    matrix = [[row * column for column in range(1, 4)] for row in range(1, 4)]
    flattened = [value for row in matrix for value in row]
    unique_initials = {word[0].upper() for word in words}
    word_lengths = {word: len(word) for word in words}

    print("Squares:", squares)
    print("Odd numbers:", odd_numbers)
    print("Large odd squares:", large_odd_squares)
    print("Long words:", long_words)
    print("Capitalized:", capitalized)
    print("Matrix:", matrix)
    print("Flattened:", flattened)
    print("Unique initials:", unique_initials)
    print("Word lengths:", word_lengths)

if __name__ == "__main__":
    main()
