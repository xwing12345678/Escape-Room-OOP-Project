from typing import Literal



class Room():
    def __init__(self,next_id:int,name:str,difficulty:Literal['Easy','Medium','Hard'],duration:int,min_players:int,max_players:int,price_per_player:int|float,is_active:bool =True) -> None:        
        self.room_id = f'R{next_id:03d}'
        self.name = name 
        self.difficulty = difficulty 
        self.duration = duration
        self.min_players = min_players
        self.max_players = max_players
        self.price_per_player = price_per_player
        self.is_active = is_active

    def activate(self):
        self._is_active = True

    def deactivate(self):
        self._is_active = False
       
    def is_valid_players(self,players:int)->bool:
        if not self.max_players <= players >= self.min_players:
            return False
        return True

    def to_dict(self)->dict:
        return self.__dict__
    
    @classmethod
    def from_dict(cls,data:dict)->Room:
        room_id:str = data["room_id"]
        without_R = room_id.strip("R")
        
        return Room(int(without_R),data['name'],data['difficulty'],data['duration'],data['min_players'],data['max_players'],data['price_per_player'],data['is_active'])

t_l = Room(1,"The Lab","Easy",60,2,8,80)
rd = t_l.to_dict()
print(rd)