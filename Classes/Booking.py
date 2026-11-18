from datetime import datetime, date,time,timedelta
from typing import Literal
from Validations.number_validations import is_non_negative_number, is_non_negative_int,is_positive_int,is_positive_number
from Validations.string_validations import is_non_empty_string,in_literal_list
from Validations.time_validations import valid_start_date, time_in_opened



class Booking():
    open_time:time = time(10,0)
    close_time:time = time(22,0)
    def __init__(self,booking_id :str,customer_name:str,room_id:str,booking_date:date,start_time:time,players:int,total_price:int|float,status:Literal['Active','Cancelled']='Active',cancellation_fee:float = 0.0) -> None:         
        self.__booking_id = booking_id       
        self.customer_name = customer_name
        self.__room_id = room_id 
        self.__booking_date = booking_date
        self.start_time = start_time
        self.players = players 
        self.total_price = total_price 
        self.__status = status 
        self.__cancellation_fee = 0.0

    @property 
    def booking_id(self):
        return self.__booking_id

    @property
    def customer_name(self):
        return self.__customer_name
    @customer_name.setter
    def customer_name(self,customer_name:str):
        if not is_non_empty_string(customer_name):
            raise ValueError("Name needs to be non-empty!")
        self.__customer_name = customer_name

    @property 
    def room_id(self):
        return self.__room_id
    @property
    def booking_date(self):
        return self.__booking_date

    @property
    def start_time(self):
        return self.__start_time
    @start_time.setter
    def start_time(self,start_time:time):
        if not time_in_opened(start_time):
            raise ValueError("You can only order inside operating hours!")
        self.__start_time = start_time

    @property
    def players(self):
        return self.__players
    @players.setter
    def players(self,players:int):
        if not is_positive_int(players):
            raise ValueError("You need a positive whole number of players!")
        self.__players = players

    @property
    def total_price(self):
        return self.__total_price
    @total_price.setter
    def total_price(self,total_price:int|float):
        if not is_positive_number(total_price):
            raise ValueError("You need a positive price! This is a business not a charity!")
        self.__total_price = total_price
        self.status = 'Cancelled'

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self,status:Literal['Active','Cancelled']):
        if not in_literal_list( status,['Active','Cancelled']):
            raise ValueError(" Status can only be Active or Cancelled!")
        self.__status = status

    @property
    def cancellation_fee(self):
        return self.__cancellation_fee 
    
    def cancel(self,fee:float):
        if not is_non_negative_number(fee):
            raise ValueError("Fee must not be a non-negative number!")
        self.__cancellation_fee += fee

    def update_details(self,booking_date:date|None = None , start_time:time|None = None, players:int|None=None, total_price:int|float|None=None):
        changed = False
        if booking_date:
            self.__booking_date = booking_date
            changed = True
        if start_time:
            self.__start_time = start_time
            changed = True
        if players:
            self.__players = players
            changed = True
        if total_price:
            self.__total_price = total_price
            changed = True
        if not changed:
            raise ValueError("You didn't enter anything you wanted to change!")
        
        




        




        
    def to_dict(self)->dict:
        return {"booking_id": self.__booking_id,
        "customer_name": self.customer_name,
        "room_id": self.room_id,
        "booking_date": self.booking_date,
        "start_time": self.start_time,
        "players": self.players,
        "total_price": self.total_price,
        "status": self.status,
        "cancellation_fee": self.cancellation_fee}
    
    @classmethod
    def from_dict(cls, data: dict) -> Booking:
        return cls(**data)