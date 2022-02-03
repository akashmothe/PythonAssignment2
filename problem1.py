from datetime import datetime, timedelta
import calendar

def NextDay(d):
    curr_date = datetime.strptime(d, "%d-%m-%Y")
    # adding 1 day to current date and getting its day number
    next_date = (curr_date + timedelta(days=1)).date().weekday()
    # getting day name form day number
    next_day = calendar.day_name[next_date]
    return next_day

d = input("Enter date (dd-mm-yyyy): ")
print(NextDay(d))


