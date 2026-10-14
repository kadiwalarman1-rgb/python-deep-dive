import random
import datetime

def generate_random_date(year):
    start_date = datetime.date(year, 1, 1)
    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    days_in_year = 366 if is_leap_year else 365
    random_days = random.randint(0, days_in_year - 1)
    random_date = start_date + datetime.timedelta(days=random_days)
    return random_date

print("Generating 5 random dates in the year 2026:\n")
for i in range(1, 6):
    result_date = generate_random_date(2026)
    formatted = result_date.strftime("%A, %B %d, %Y")
    print(f"Random date {i}: {formatted}")
