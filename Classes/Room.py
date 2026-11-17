from typing import Literal



class Room():
    def __init__(self,name:str,difficulty:Literal['Easy','Medium','Hard'],duration:int,min_players:int,max_players:int,price_per_player:int|float,is_active:bool =True) -> None:        

        self._name = name 
        self._difficulty = difficulty 
        self._duration = duration
        self._min_players = min_players
        self._max_players = max_players
        self._price_per_player = price_per_player
        self._is_active = is_active
        #room_id
    
    def activate():
        pass

    def deactivate():
        pass

    def is_valid_players(self,players:int)->bool:
        if not self._max_players <= players >= self._min_players:
            return False
        return True

    def to_dict()->dict:
        pass
    
    @classmethod
    def from_dict(cls,data:dict)->Room:
        pass

