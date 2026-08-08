class Room:

    def __init__(
        self,
        room_number,
        floor,
        room_type,
        price_per_night,
        capacity,
        status="AVAILABLE" 
        ):
        self.room_number = room_number
        self.floor = floor
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.capacity = capacity
        self.status = status

    def show_info(self):
        print(f"Room Number: {self.room_number}")
        print(f"Floor: {self.floor}")
        print(f"Room Type: {self.room_type}")
        print(f"Price Per Night: ${self.price_per_night}")
        print(f"Capacity: {self.capacity} people")
        print(f"Status: {self.status}")
        