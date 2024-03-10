from datetime import datetime, timedelta


users = [                                                                               # List of dictionary of people with their birthdays
    {"name": "John Doe", "birthday": "1985.03.17"},
    {"name": "Jane Smith", "birthday": "1990.03.15"},
    {"name": "Paul Washington", "birthday": "1984.04.20"},
    {"name": "Amanda Rickman", "birthday": "1977.06.17"},
    {"name": "Jake", "birthday": "1995.03.10"}
]

def get_prepared_users(users: list) -> list:                                            # Function for converting data from str to datetime format
    prepared_users = []
    for user in users:
        try:
            birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            prepared_users.append({"name": user['name'], 'birthday': birthday})
        except ValueError:
            print("Inappropriate format!")
    return prepared_users


def find_next_weekday(d, weekday: int):                                                 # Function for determining next 7 days
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + timedelta(days=days_ahead)



def get_upcoming_birthdays(prepared_users: list) -> list:                               # Function for getting upcoming birthdays from users's list
    days = 7
    today_date = datetime.today().date()
    upcoming_birthdays = []
    for user in get_prepared_users(users):
        birthday_this_year = user["birthday"].replace(year=today_date.year)
        if birthday_this_year < today_date:
            birthday_this_year = birthday_this_year.replace(year=today_date.year + 1)
        elif 0 <= (birthday_this_year - today_date).days <= days:
            if birthday_this_year.weekday() >= 5:
                birthday_this_year = find_next_weekday(birthday_this_year, 0)
            congratulation_date = birthday_this_year.strftime('%Y.%m.%d')
            upcoming_birthdays.append({'name': user["name"],
                                       "congratulation_date": congratulation_date})
    return upcoming_birthdays

print(get_upcoming_birthdays(users))



