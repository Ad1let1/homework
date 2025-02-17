from datetime import datetime

def date_difference_in_seconds(date1_str, date2_str, date_format="%Y-%m-%d %H:%M:%S"):
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)
    difference = date2 - date1
    return difference.total_seconds()

date1 = "2023-10-01 12:00:00"
date2 = "2023-10-02 12:00:00"
print(f"Difference in seconds: {date_difference_in_seconds(date1, date2)}")