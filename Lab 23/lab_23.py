def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    normalized = "".join(character.lower() for character in text if character.isalnum())
    return normalized == normalized[::-1]

def analyze_string(text):
    return {
        "length": len(text),
        "uppercase": text.upper(),
        "lowercase": text.lower(),
        "word_count": len(text.split()),
        "starts_with_python": text.lower().startswith("python"),
    }

def main():
    first = "Python"
    second = "Programming"
    combined = first + " " + second
    print("Combined:", combined)
    print("Uppercase:", combined.upper())
    print("Lowercase:", combined.lower())
    print("Replace:", combined.replace("Programming", "Development"))
    print("First six characters:", combined[:6])
    print("Last eleven characters:", combined[-11:])
    print("Every second character:", combined[::2])
    print(f"{first} is useful for learning and building projects.")
    print("Reversed:", reverse_text("developer"))
    print("Level palindrome:", is_palindrome("Level"))
    print("Phrase palindrome:", is_palindrome("A man, a plan, a canal: Panama"))
    print("String report:", analyze_string(combined))

if __name__ == "__main__":
    main()
