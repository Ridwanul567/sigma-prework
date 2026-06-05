# Age Calculator Program
# Returns the age of a person after birthdate is entered
import datetime as dt

'''
today = dt.datetime.today()
print(today)

random_date = dt.datetime.strptime("01/04/2015", "%d/%m/%Y")
print(random_date)


print(type(today))
print(type(random_date))

print(today.year-random_date.year)
'''


def age_calculator():
    repeat = True
    today = dt.datetime.today()
    while repeat is True:
        print("Please enter the birthdate in dd/mm/yyyy format.")
        date = input()
        date = dt.datetime.strptime(date, "%d/%m/%Y")
        year = today.year - date.year
        month = today.month - date.month
        if month < 0:
            age = year - 1
            print(age)
        elif month == 0:
            day = today.day - date.day
            if day < 0:
                age = year - 1
                print(age)
            elif day == 0:
                age = year
                print(f"{age}. Happy Birthday!")
            else:
                age = year
                print(age)
        else:
            age = year
            print(age)
        print("Do you want to try again with another birthdate? 1 for Yes, 0 for No")
        choice = input()
        repeat = False
        if choice == "1":
            repeat = True


age_calculator()
