import datetime
def find_day_of_week(date_string):
    month, day, year = map(int, date_string.split())
    date = datetime.date(year, month, day)
    day_of_week = date.strftime("%A").upper() # strftime  method is used to convert a datetime object to a string
                                              # % A format code specifies that we want the full name of the week
    return day_of_week

date_string = input("Enter the date: ")
day_of_week = find_day_of_week(date_string)
print(day_of_week)
