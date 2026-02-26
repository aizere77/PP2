from datetime import datetime, timedelta
#TASK1
#Write a Python program to subtract five days from current date.

today = datetime.now()
future = today - timedelta(days=5)
print(future)