def main():
    text = "Python Programming"
    numbers = [10, 20, 30, 40, 50, 60]
    colors = ("red", "green", "blue", "yellow")

    print("Text first character:", text[0])
    print("Text last character:", text[-1])
    print("Text slice:", text[0:6])
    print("Text reversed:", text[::-1])
    print("List slice:", numbers[1:5:2])
    print("List last three:", numbers[-3:])
    print("Tuple slice:", colors[1:3])

    print("'Python' in text:", "Python" in text)
    print("25 in numbers:", 25 in numbers)
    print("'purple' not in colors:", "purple" not in colors)

    print("String concatenation:", "Hello, " + "Python!")
    print("List concatenation:", numbers[:2] + numbers[-2:])
    print("Tuple concatenation:", colors[:2] + colors[2:])
    print("String repetition:", "ha" * 3)
    print("List repetition:", [1, 2] * 3)
    print("Tuple repetition:", ("go",) * 4)

if __name__ == "__main__":
    main()
