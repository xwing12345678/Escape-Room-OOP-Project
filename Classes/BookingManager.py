from datetime import datetime
from .Room import Room
from .Booking import Booking
from .PricingManager import PricingManager





class BookingManager():
    def __init__(self) -> None:
        self._rooms:list[Room] = []
        self._bookings:list[Booking] = []
        self._pricing_manager:PricingManager = PricingManager()

    def create_booking(customer_name, room_id, booking_date, start_time, players):
        pass

    def get_booking(booking_id)->Booking|None:
        pass

    def get_customer_bookings(customer_name)->list[Booking]:
        pass

    def get_bookings_by_date(booking_date)->list[Booking]:
        pass
    
    def check_availability(room_id, booking_date, start_time, exclude_booking_id=None)->bool:
        pass

    def update_booking(booking_id, booking_date, start_time, players):
        pass
    
    def cancel_booking(booking_id, current_datetime:datetime):
        pass


 