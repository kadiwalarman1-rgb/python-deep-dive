class Counter:
    def __init__(self, initial_value=0):
        if not isinstance(initial_value, int) or isinstance(initial_value, bool):
            raise TypeError("Initial value must be an integer")
        self.value = initial_value
        print(f"Counter created with initial value: {self.value}")

    def increment(self):
        self.value += 1
        print(f"Counter incremented. Current value: {self.value}")

    def decrement(self):
        self.value -= 1
        print(f"Counter decremented. Current value: {self.value}")

    def add_value(self, amount):
        if not isinstance(amount, int) or isinstance(amount, bool):
            raise TypeError("Amount must be an integer")
        self.value += amount
        print(f"Added {amount} to counter. Current value: {self.value}")

    def reset(self):
        old_value = self.value
        self.value = 0
        print(f"Counter reset from {old_value} to {self.value}")

    def get_value(self):
        return self.value

    def display_status(self):
        print(f"Counter Status: {self.value}")
        if self.value > 0:
            print("Counter is positive")
        elif self.value < 0:
            print("Counter is negative")
        else:
            print("Counter is at zero")


if __name__ == "__main__":
    print("=== Creating Multiple Counters ===")
    counter1 = Counter(5)
    counter2 = Counter(10)
    counter3 = Counter()

    print("\n=== Operating on Different Counters ===")
    counter1.increment()
    counter1.increment()
    counter2.decrement()
    counter2.add_value(3)
    counter3.add_value(7)
    counter3.decrement()

    print("\n=== Final Status of All Counters ===")
    for number, counter in enumerate((counter1, counter2, counter3), 1):
        print(f"Counter {number}:")
        counter.display_status()

    print(f"\nIndependent values - Counter1: {counter1.get_value()}, Counter2: {counter2.get_value()}, Counter3: {counter3.get_value()}")
