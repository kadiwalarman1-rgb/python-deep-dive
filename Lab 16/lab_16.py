def grade_report(scores):
    if not scores:
        return {"count": 0, "average": 0, "highest": None, "lowest": None, "passed": []}
    return {
        "count": len(scores),
        "average": sum(scores) / len(scores),
        "highest": max(scores),
        "lowest": min(scores),
        "passed": [score for score in scores if score >= 50],
    }

def main():
    mixed_values = ["Python", 42, 3.14, True]
    numbers = [8, 3, 10, 1, 6]
    print("Mixed list:", mixed_values)
    print("First item:", mixed_values[0])
    print("Slice:", numbers[1:4])
    numbers.append(12)
    numbers.insert(1, 5)
    numbers[0] = 9
    numbers.remove(10)
    removed = numbers.pop()
    print("Updated list:", numbers)
    print("Popped value:", removed)
    print("Sorted copy:", sorted(numbers))
    print("Descending:", sorted(numbers, reverse=True))
    for index, value in enumerate(numbers, start=1):
        print(f"Item {index}: {value}")
    print("Grade report:", grade_report([45, 72, 88, 39, 91, 50]))

if __name__ == "__main__":
    main()
