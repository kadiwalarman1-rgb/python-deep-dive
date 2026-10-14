import datetime

now = datetime.datetime.now()
print(f"Current date and time: {now}")

today = datetime.date.today()
print(f"Today's date: {today}")

formatted_date = now.strftime("%A, %B %d, %Y")
print(f"Formatted date: {formatted_date}")

formatted_time = now.strftime("%I:%M %p")
print(f"Formatted time: {formatted_time}")

thirty_days_later = today + datetime.timedelta(days=30)
print(f"30 days from today will be: {thirty_days_later}")
