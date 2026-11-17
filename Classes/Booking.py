from datetime import datetime, date,time,timedelta
from typing import Literal

class Booking():
    def __init__(self,customer_name:str,room_id:str,booking_date:date,start_time:time,players:int,total_price:int|float,status:Literal['Active','Cancelled']='Active',cancellation_fee:float = 0.0) -> None:
        
        #booking_id
        self._customer_name:str = customer_name
        self._room_id:str = room_id 
        self._booking_date:date = booking_date
        self._start_time:time = start_time
        self._players:int = players 
        self._total_price:int|float = total_price 
        self._status:Literal['Active','Cancelled'] = status 
        #cancellation_fee
    
    def cancel(self,fee:float):
        pass

    def update_details(self,booking_date:date , start_time:time, players:int, total_price:int|float):
        pass

    def to_dict(self)->dict:
        pass

    @classmethod
    def from_dict(cls,data:dict)->Booking:
        pass

