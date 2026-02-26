from datetime import datetime, timedelta

#1. Write a Python program to subtract five days from current date.
from datetime import datetime, timedelta
current_date = datetime.now()
new_date = current_date - timedelta(days=5)
print("Current date:", current_date)
print("Date 5 days ago:", new_date)


#2. Write a Python program to print yesterday, today, tomorrow.
today = datetime.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


#3. Write a Python program to drop microseconds from datetime.
from datetime import datetime
now = datetime.now()
without_microseconds = now.replace(microsecond=0)

print("Original datetime:", now)
print("Without microseconds:", without_microseconds)


#4. Write a Python program to calculate two date difference in seconds.
date1 = datetime(2026, 2, 20, 12, 20, 0, 0)
date2 = datetime(2026, 2, 25, 15, 0, 0, 0)
difference = date2 - date1
seconds = difference.total_seconds()
print("Difference in seconds:", seconds)