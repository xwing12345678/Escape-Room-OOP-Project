from datetime import date,datetime
from Classes.Room import Room
from Classes.Booking import Booking
from pathlib import Path
import json



class DataManager():
    def __init__(self,rooms_file,bookings_file) -> None:
        self._rooms_file = rooms_file
        self._bookings_file = bookings_file 


    def load_rooms()->list[Room]:
        pass

    def load_bookings()->list[Booking]:

        pass

    def save_rooms(rooms):
        
        pass

    def save_bookings(bookings):
        
        pass


    