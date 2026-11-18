
from Classes.Room import Room

r1_dict = {
        "room_id": "R001",
        "name": "The Lab",
        "difficulty": "Easy",
        "duration": 60,
        "min_players": 2,
        "max_players": 8,
        "price_per_player": 80,
        "is_active": True
    }
r1 = Room.from_dict(r1_dict)
print(r1.to_dict())
