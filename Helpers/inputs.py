from .time_functs import get_current_date
from Validations.time_validations import past_year,past_month,past_day
from Validations.number_validations import is_positive_int_str

def get_valid_year()->int:
    raw_year = ""
    valid_year = False
    while not valid_year:
        raw_year = input("Enter in the year you want to reserve: ")
        if not is_positive_int_str(raw_year):
            print(" You need to enter a positive whole number!")
            continue
        year = int(raw_year)
        if past_year(year):
            print("The year you entered is in the past! You can only reserve in the present or future! ")
            continue
        valid_year = True
        break
    return int(raw_year)

def get_valid_month()->int:
    raw_month = ""
    valid_month = False
    while not valid_month:
        raw_month = input("Enter in the month you want to reserve: ")
        if not is_positive_int_str(raw_month):
            print(" You need to enter a positive whole number!")
            continue
        month = int(raw_month)
        if past_month(month):
            print("The month you entered is in the past! You can only reserve in the present or future! ")
            continue
        valid_month = True
        break
    return int(raw_month)

def get_valid_day()->int:
    raw_day = ""
    valid_day = False
    while not valid_day:
        raw_day = input("Enter in the day you want to reserve: ")
        if not is_positive_int_str(raw_day):
            print(" You need to enter a positive whole number!")
            continue
        day = int(raw_day)
        if past_day(day):
            print("The dau you entered is in the past! You can only reserve in the present or future! ")
            continue
        valid_day = True
        break
    return int(raw_day)

def get_valid_minute()->int:
    raw_day = ""
    valid_day = False
    while not valid_day:
        raw_day = input("Enter in the day you want to reserve: ")
        if not is_positive_int_str(raw_day):
            print(" You need to enter a positive whole number!")
            continue
        day = int(raw_day)
        if past_day(day):
            print("The dau you entered is in the past! You can only reserve in the present or future! ")
            continue
        valid_day = True
        break
    return int(raw_day)

