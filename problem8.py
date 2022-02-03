from datetime import datetime, timedelta, date
import calendar

def day_of_date(dt):
    # formatting and getting the day number
    dt = datetime.strptime(str(dt), '%Y-%m-%d')
    curr_day_no = dt.weekday()

    # getting day name form day number
    day_name = calendar.day_name[curr_day_no]
    print(f"Current date: {dt.date()}")
    print(f"Week day: {day_name}")
    print(f"Day number: {curr_day_no}")

    # getting 0'th day form current date
    curr_firstday = (dt - timedelta(curr_day_no)).date()
    print("Current Week:")
    print(f"{curr_firstday} {calendar.day_name[curr_firstday.weekday()]}")

    # loop for print next 7 days from curr_firstday
    for i in range(1,7):
        curr_week = curr_firstday + timedelta(i)
        print(f"{curr_week} {calendar.day_name[curr_week.weekday()]}")
        
    # getting 0th day of pass week
    past_firstday = (curr_firstday - timedelta(7))
    print("Past week")
    print(f"{past_firstday} {calendar.day_name[past_firstday.weekday()]}")

    # loop for print next 7 days from past_firstday
    for i in range(1,7):
        past_week = past_firstday + timedelta(i)
        print(f"{past_week} {calendar.day_name[past_week.weekday()]}")



day_of_date("2017-10-11")
    