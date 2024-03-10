from datetime import datetime

date = input("Input the date in format (YYYY-MM-DD): ")                     # Asking user to input the date

def get_days_from_today(date: str) -> datetime:                             # Making function
    try:
        date_datetime = datetime.strptime(date, "%Y-%m-%d")                 # Converting inputed date into datetime class
        sequence_date = date_datetime.toordinal()                           # Convernting datetime datetime date into sequence number
        today = datetime.today()                                            # Current date (today's date)
        sequence_today = today.toordinal()                                  # Converting current day into sequence number
        difference = sequence_today - sequence_date                         # Making difference between current date and inputed date
        return difference                                                   # Returning the result
    except ValueError:
        print("Inappropriate format, please use 'YYYY-MM-DD' format")       # Condition for ValueError exception


difference = get_days_from_today(date)
print(difference)
print(type(difference))

