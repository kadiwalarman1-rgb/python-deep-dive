def main():
    fruits = {"apple", "banana", "orange", "apple"}
    print("Unique fruits:", fruits)
    fruits.add("mango")
    fruits.discard("banana")
    print("Updated fruits:", fruits)

    math_students = {"Amina", "Bilal", "Chen", "Dia"}
    science_students = {"Bilal", "Chen", "Eva"}
    english_students = {"Amina", "Chen", "Farah"}
    print("Math or science:", math_students | science_students)
    print("Math and science:", math_students & science_students)
    print("Math but not science:", math_students - science_students)
    print("Exactly one of math or science:", math_students ^ science_students)
    print("In all three subjects:", math_students & science_students & english_students)

    original = [1, 2, 2, 3, 3, 3, 4]
    unique = set(original)
    print("Original list:", original)
    print("Unique items:", unique)
    print("Common values:", set([2, 4, 6, 8]) & set([1, 2, 3, 4]))
    print("Has pineapple:", "pineapple" in fruits)

if __name__ == "__main__":
    main()
