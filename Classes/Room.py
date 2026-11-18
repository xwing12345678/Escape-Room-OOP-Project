from typing import Literal
from Validations.number_validations import is_positive_int, is_non_negative_int,is_positive_number 
from Validations.string_validations import is_non_empty_string, in_literal_list



class Room():
    def __init__(self,room_id:str,name:str,difficulty:Literal['Easy','Medium','Hard'],duration:int,min_players:int,max_players:int,price_per_player:int|float,is_active:bool =True) -> None:        
        self.__room_id:str = room_id          # no setter -> read-only
        self.name = name             
        self.difficulty = difficulty 
        self.duration = duration
        self.min_players = min_players
        self.max_players = max_players
        self.price_per_player = price_per_player     # no underscore: goes through the setter
        self.__is_active = is_active      # changed only via activate()/deactivate()

    @property
    def room_id(self): 
        return self.__room_id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name:str):
        if not is_non_empty_string(name):
            raise ValueError("Name cannot be empty!")
        self.__name = name

    @property
    def difficulty(self):
        return self.__difficulty
    @difficulty.setter
    def difficulty(self,difficulty:Literal['Easy','Medium','Hard']):
        if not in_literal_list(difficulty,['Easy','Medium','Hard']):
            raise ValueError("Difficulty must be in the list: ['Easy','Medium','Hard']!")
        self.__difficulty = difficulty
    
    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self,duration:int):
        if not is_positive_int(duration):
            raise ValueError("Duration must be a positive whole number!")
        self.__duration = duration

    @property
    def min_players(self):
        return self.__min_players 
    
    @min_players.setter
    def min_players(self,min_players:int):
        if not is_positive_int(min_players):
            raise ValueError("Min_players must be a positive whole number!")
        self.__min_players = min_players

    @property
    def max_players(self):
        return self.__max_players 
    @max_players.setter
    def max_players(self,max_players:int):
        if not is_positive_int(max_players):
            raise ValueError("Max_players must be a positive whole number!")
        if not max_players >= self.min_players:
            raise ValueError("Max_players must be greater or equal to min_players!")
        self.__max_players = max_players
    
    @property
    def price_per_player(self): 
        return self.__price_per_player

    @price_per_player.setter
    def price_per_player(self,price:int|float):
        if not is_positive_number(price):
            raise ValueError("price_per_player cannot be negative")
        self.__price_per_player = price
    
    @property
    def is_active(self): return self.__is_active

    def activate(self):
        self.__is_active = True

    def deactivate(self):
        self.__is_active = False
       
    def is_valid_players(self,players:int)->bool:
        if not self.max_players <= players >= self.min_players:
            return False
        return True

    def to_dict(self) -> dict:
        return {
            "room_id": self.__room_id,
            "name": self.name,
            "difficulty": self.__difficulty,
            "duration": self.__duration,
            "min_players": self.__min_players,
            "max_players": self.__max_players,
            "price_per_player": self.__price_per_player,
            "is_active": self.__is_active,}

    @classmethod
    def from_dict(cls, data: dict) -> "Room":
        return cls(**data)


