from datetime import datetime

def Diff_of_dates(d1,d2):
    d1 = datetime.strptime(str(d1), "%Y-%m-%d")
    d2 = datetime.strptime(str(d2), "%Y-%m-%d")
    return (d1-d2)


date1 = input("Enter date1 (yyyy-mm-dd): ")
date2 = input("Enter date2 (yyyy-mm-dd): ")

print(Diff_of_dates(date1, date2))