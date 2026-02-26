from datetime import datetime, timedelta
#TASK1
#Write a Python program to subtract five days from current date.

today = datetime.now()
five_days_ago = today - timedelta(days=5)

print("1. Five days ago:")
print(five_days_ago)
print()