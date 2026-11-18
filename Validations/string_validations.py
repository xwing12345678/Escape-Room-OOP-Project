
def is_non_empty_string(string:str)->bool:
    clean_string = string.strip()
    if not clean_string:
        return False
    return True

def in_literal_list(option:str,literal_list:list[str])->bool:
    if not is_non_empty_string(option):
        return False
    return option in literal_list 

