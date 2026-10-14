def rectangle_area(length, width):
    return length * width

def summarize_numbers(numbers):
    if not numbers:
        return {"count": 0, "total": 0, "average": 0, "minimum": None, "maximum": None}
    return {
        "count": len(numbers),
        "total": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "minimum": min(numbers),
        "maximum": max(numbers),
    }

def filter_passing(scores, pass_mark=50):
    return [score for score in scores if score >= pass_mark]

def main():
    area = rectangle_area(7, 4)
    print("Rectangle area:", area)
    scores = [45, 72, 88, 39, 91, 50]
    summary = summarize_numbers(scores)
    print("Summary:", summary)
    print("Passing scores:", filter_passing(scores))
    print("Empty list summary:", summarize_numbers([]))

if __name__ == "__main__":
    main()
