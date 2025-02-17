from datetime import datetime, timedelta


curr_date = datetime.now()

new = curr_date - timedelta(days=5)


print("Current date:", curr_date.strftime("%Y-%m-%d"))
print("New date:", new.strftime("%Y-%m-%d"))