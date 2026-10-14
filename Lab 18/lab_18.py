def describe_person(person):
    name, age, city = person
    return f"{name} is {age} years old and lives in {city}."

def main():
    student = ("Amina", 21, "Ahmedabad")
    mixed_tuple = ("Python", 3, 4.5, True)
    print("Student:", student)
    print("First element:", student[0])
    print("Last element:", student[-1])
    print("Slice:", mixed_tuple[1:3])
    print(describe_person(student))

    try:
        student[1] = 22
    except TypeError as error:
        print("Tuple immutability handled:", error)

    for item in mixed_tuple:
        print("Value:", item)
    for index, item in enumerate(mixed_tuple):
        print(index, item)

    names = ["Amina", "Rahul", "Sara"]
    names_tuple = tuple(names)
    restored_list = list(names_tuple)
    print("Tuple from list:", names_tuple)
    print("List from tuple:", restored_list)
    coordinates = (10, 20)
    x, y = coordinates
    print("Coordinates:", x, y)
    combined = student + ("Python",)
    print("Combined tuple:", combined)

if __name__ == "__main__":
    main()
