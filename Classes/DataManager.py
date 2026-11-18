from Classes.Room import Room
from Classes.Booking import Booking
from pathlib import Path
import json

class DataManager():
    def __init__(self,rooms_file,bookings_file) -> None:
        self.__rooms_file:str = rooms_file
        self.__bookings_file:str = bookings_file 

    def load_rooms(self)->list[Room]:
        ROOMS_FILE = Path(__file__).parent / self.__rooms_file
        if not ROOMS_FILE.exists():
            return []
    
        try:
            with open(ROOMS_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []

    def load_bookings(self)->list[Booking]:
        BOOKINGS_FILE = Path(__file__).parent / self.__rooms_file
        if not BOOKINGS_FILE.exists():
            return []
            
        try:
            with open(BOOKINGS_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []

    def save_rooms(self,rooms:list[Room]):
        ROOMS_FILE = Path(__file__).parent / self.__rooms_file
        with open(ROOMS_FILE, "w", encoding="utf-8") as file:
            json.dump(rooms, file, indent=2, ensure_ascii=False)
                
    def save_bookings(self,bookings:list[Booking]):
        BOOKINGS_FILE = Path(__file__).parent / self.__bookings_file
        with open(BOOKINGS_FILE, "w", encoding="utf-8") as file:
            json.dump(bookings, file, indent=2, ensure_ascii=False)
        


    