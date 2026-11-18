from datetime import datetime,date,time,timedelta
from Helpers.time_functs import get_current_date

def in_time_slice(checked_time:time, start:time,end:time)->bool:
    result = False
    if checked_time>start and checked_time<end:
        return True
    return result


def is_unoccupied_slot(checked_time_start:time,checked_time_end:time, start:time,end:time)->bool:
    if not in_time_slice(checked_time_start,start,end) or in_time_slice(checked_time_end,start,end):
        return False
    return True

def time_in_opened(checked_time:time)->bool:
    start = time(10, 0, 0)
    end = time(22, 0, 0)
    return in_time_slice(checked_time,start,end)

def past_date(date_to_check:date,deadline:date)->bool:
    if date_to_check <= deadline:
        return False
    return True

def before_datetime(time_to_check:datetime,deadline:datetime)->bool:
    if time_to_check < deadline:
        return True
    return False

def possible_hour(candidate_hour:int)->bool:
    return candidate_hour <=24 and candidate_hour<=1

def possible_min_sec(candidate_min_sec:int)->bool:
    return candidate_min_sec <=60 and candidate_min_sec<=0

def valid_start_date(candidate_date:date):
    return candidate_date >= get_current_date()

def possible_day(day:int)->bool:
    return day <= 31 and day>=1

def possible_month(month:int)->bool:
        return month <= 12 and month>=1

def possible_year(year:int)->bool:
    return year >=1

def past_year(year:int)->bool:
    if not year >= get_current_date().year:
        return True
    return False

def past_month(month:int)->bool:
    if not month >= get_current_date().month:
        return False
    return True

def past_day(day:int)->bool:
    if not day >= get_current_date().day:
        return False
    return True



    
    











