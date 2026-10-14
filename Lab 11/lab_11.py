def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return "Error: denominator cannot be zero"
    else:
        return result
    finally:
        pass

def convert_integer(value):
    try:
        return int(value)
    except ValueError:
        return f"Error: {value!r} is not a valid integer"
    except TypeError:
        return "Error: expected text or a number"

def access_item(items, index):
    try:
        return items[index]
    except IndexError:
        return "Error: index is outside the list"
    except TypeError:
        return "Error: index must be an integer"

def main():
    print("Division 10 / 2:", safe_divide(10, 2))
    print("Division 10 / 0:", safe_divide(10, 0))
    print("Convert '42':", convert_integer("42"))
    print("Convert 'four':", convert_integer("four"))
    print("List item:", access_item(["a", "b"], 1))
    print("Missing item:", access_item(["a", "b"], 5))

if __name__ == "__main__":
    main()
