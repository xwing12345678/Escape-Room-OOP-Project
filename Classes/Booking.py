from datetime import datetime, date,time,timedelta
from typing import Literal

class Booking():
    def __init__(self,next_id:int,customer_name:str,room_id:str,booking_date:date,start_time:time,players:int,total_price:int|float,status:Literal['Active','Cancelled']='Active',cancellation_fee:float = 0.0) -> None: 
        self.booking_id = f'B{next_id:03d}'
        self.customer_name:str = customer_name
        self.room_id:str = room_id 
        self.booking_date:date = booking_date
        self.start_time:time = start_time
        self.players:int = players 
        self.total_price:int|float = total_price 
        self.status:Literal['Active','Cancelled'] = status 
        self.cancellation_fee:float = 0.0

    
    def cancel(self,fee:float):
        self.cancellation_fee += fee

    def update_details(self,booking_date:date , start_time:time, players:int, total_price:int|float):
        self.booking_date,self.start_time,self.players,self.total_price = booking_date,start_time,players,total_price

    def to_dict(self)->dict:
        return vars(self)

    @classmethod
    def from_dict(cls,data:dict)->Booking:
        room_id:str = data["booking_id"]
        # gets rid of the B so the init works normally
        without_B = room_id.strip("B")
        #gets rid of the zeros
        without0 = without_B.lstrip("0")

        return Booking(int(without0),data['room_id'],data['booking_date'],data['start_time'],data['players'],data['total_price'],data['status'],data['cancellation_fee'])


