from datetime import date,datetime
from Classes.Room import Room
from Classes.Booking import Booking
class PricingManager():

    def calculate_price(self,room:Room, players:int, booking_date:date)->float:
        return room._price_per_player * players 

    def calculate_cancellation_fee(self,booking:Booking, current_datetime:datetime)->float:
        pass
