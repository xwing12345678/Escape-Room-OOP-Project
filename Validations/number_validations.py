from .string_validations import is_non_empty_string
def is_nonnegative_int_str(int_candidate:str)->bool:
    if not is_non_empty_string(int_candidate):
        return False
    return int_candidate.isdigit()

def is_positive_int_str(int_candidate:str)->bool:
    if not is_nonnegative_int_str(int_candidate):
        return False
    integer = int(int_candidate)
    if not isinstance(integer,int) or isinstance(integer,bool):
        return False
    if not integer >= 0:
        return False
    return True

def is_non_negative_number(number:int|float)->bool:
    if not (isinstance(number,int) or isinstance(number,float) ) or isinstance(number,bool):
        return False
    if not number >= 0:
        return False
    return True
    
def is_non_negative_int(number:int)->bool:
    if not isinstance(number,int)  or isinstance(number,bool):
            return False
    if not number >= 0:
        return False
    return True

def is_positive_number(number:int|float)->bool:
    if not is_non_negative_number(number):
        return False
    return number > 0

def is_positive_int(number:int)->bool:
    if not is_non_negative_int(number):
        return False
    return number > 0
         

