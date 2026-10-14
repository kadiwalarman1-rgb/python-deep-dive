def mean(data):
    if not data:
        raise ValueError("Cannot calculate mean of an empty dataset")
    return sum(data) / len(data)


def median(data):
    if not data:
        raise ValueError("Cannot calculate median of an empty dataset")
    sorted_data = sorted(data)
    middle = len(sorted_data) // 2
    if len(sorted_data) % 2 == 0:
        return (sorted_data[middle - 1] + sorted_data[middle]) / 2
    return sorted_data[middle]


def mode(data):
    if not data:
        raise ValueError("Cannot calculate mode of an empty dataset")
    frequencies = {}
    for value in data:
        frequencies[value] = frequencies.get(value, 0) + 1
    highest_frequency = max(frequencies.values())
    modes = [value for value, frequency in frequencies.items() if frequency == highest_frequency]
    return modes[0] if len(modes) == 1 else modes


def range_value(data):
    if not data:
        raise ValueError("Cannot calculate range of an empty dataset")
    return max(data) - min(data)


def variance(data):
    if len(data) < 2:
        raise ValueError("At least two data points are required to calculate variance")
    average = mean(data)
    return sum((value - average) ** 2 for value in data) / (len(data) - 1)


def standard_deviation(data):
    return variance(data) ** 0.5
