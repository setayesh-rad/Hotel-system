class Room:

    def __init__(
        self,
        room_number,
        floor,
        capacity,
        status="AVAILABLE" 
        ):
        self.room_number = room_number
        self.floor = floor
        self.capacity = capacity
        self.status = status
        self.room_type = self.get_room_type()
        self.price_per_night = self.calculate_price()
    


    def get_room_type(self):
        if 1 <= self.floor <=4 :
            return "ECONOMY"

        elif 5 <= self.floor <= 8 :
            return "STANDARD"

        elif 9 <= self.floor <= 12 :
            return "LUXURY"

        else:
            raise ValueError("invalid floor")



    def calculate_price(self):

        if not 2 <= self.capacity <= 6:
            raise ValueError("Capacity must be between 2 and 6")

        if self.room_type == "ECONOMY":
            base_price = 7.5
            extra_person_price = 2
            floor_price = 0.4
            base_floor = 1

        elif self.room_type == "STANDARD":
            base_price = 12.5
            extra_person_price = 4
            floor_price = 0.6
            base_floor = 5

        else:
            base_price = 22
            extra_person_price = 6
            floor_price = 1
            base_floor = 9

        extra_people = self.capacity - 2
        extra_floors = self.floor - base_floor

        price = (
            base_price
            + (extra_people * extra_person_price)
            + (extra_floors * floor_price)
        )

        return price


    def show_info(self):
        print(f"Room Number: {self.room_number}")
        print(f"Floor: {self.floor}")
        print(f"Room Type: {self.room_type}")
        print(f"Price Per Night: ${self.price_per_night}")
        print(f"Capacity: {self.capacity} people")
        print(f"Status: {self.status}")

       



                       