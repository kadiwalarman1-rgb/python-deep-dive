import random

random_float = random.random()
print(f"Random float between 0 and 1: {random_float}")

random_integer = random.randint(1, 100)
print(f"Random integer between 1 and 100: {random_integer}")

def roll_dice():
    return random.randint(1, 6)

print("\nRolling the dice 5 times:")
for roll_number in range(1, 6):
    result = roll_dice()
    print(f"Roll {roll_number}: {result}")
