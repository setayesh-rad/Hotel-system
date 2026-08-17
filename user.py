class User:

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def login(self,username,password):
        return self.username == username and self.password == password


class Employee(User):

    def __init__( 
        self,
        employee_id,
        first_name,
        last_name,
        age,
        national_id,
        address,
        phone,
        years_of_experience,
        hire_date,
        job_title,
        work_schedule,
        salary,
        username,
        password
    ):
        super().__init__(username, password)

        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.national_id = national_id
        self.address = address
        self.phone = phone
        self.years_of_experience = years_of_experience
        self.salary = salary 
        self.hire_date = hire_date
        self.job_title = job_title
        self.work_schedule = work_schedule



class Chef(Employee):

    def __init__(
        self,
        employee_id,
        first_name,
        last_name,
        age,
        national_id,
        address,
        phone,
        years_of_experience,
        hire_date,
        job_title,
        work_schedule,
        salary,
        username,
        password,
        specialties
    ):
        super().__init__(
            employee_id,
            first_name,
            last_name,
            age,
            national_id,
            address,
            phone,
            years_of_experience,
            hire_date,
            job_title,
            work_schedule,
            salary,
            username,
            password
        )

        self.specialties = specialties




class Driver(Employee):

    def __init__(
        self,
        employee_id,
        first_name,
        last_name,
        age,
        national_id,
        address,
        phone,
        years_of_experience,
        hire_date,
        job_title,
        work_schedule,
        salary,
        username,
        password,
        license_number,
        license_plate,
        car_model,
        car_type
    ):
        super().__init__(
            employee_id,
            first_name,
            last_name,
            age,
            national_id,
            address,
            phone,
            years_of_experience,
            hire_date,
            job_title,
            work_schedule,
            salary,
            username,
            password
        )

        self.license_number = license_number
        self.license_plate = license_plate
        self.car_model = car_model
        self.car_type = car_type
        self.availability = []



class Housekeeper(Employee):

    def __init__(
        self,
        employee_id,
        first_name,
        last_name,
        age,
        national_id,
        address,
        phone,
        years_of_experience,
        hire_date,
        job_title,
        work_schedule,
        salary,
        username,
        password
    ):
        super().__init__(
            employee_id,
            first_name,
            last_name,
            age,
            national_id,
            address,
            phone,
            years_of_experience,
            hire_date,
            job_title,
            work_schedule,
            salary,
            username,
            password
        )

        self.shift = {}
        self.floor = None
        self.room_schedule = {}




class Receptionist(Employee):

    def __init__(
        self,
        employee_id,
        first_name,
        last_name,
        age,
        national_id,
        address,
        phone,
        years_of_experience,
        hire_date,
        job_title,
        work_schedule,
        salary,
        username,
        password,
    ):
        super().__init__(
            employee_id,
            first_name,
            last_name,
            age,
            national_id,
            address,
            phone,
            years_of_experience,
            hire_date,
            job_title,
            work_schedule,
            salary,
            username,
            password
        ) 

        self.shift = {}
         



class Translator(Employee):

    def __init__(
        self,
        employee_id,
        first_name,
        last_name,
        age,
        national_id,
        address,
        phone,
        years_of_experience,
        hire_date,
        job_title,
        work_schedule,
        salary,
        username,
        password,
        languages
    ):
        super().__init__(
            employee_id,
            first_name,
            last_name,
            age,
            national_id,
            address,
            phone,
            years_of_experience,
            hire_date,
            job_title,
            work_schedule,
            salary,
            username,
            password
        )

        self.languages = languages
        self.availability = []



class TourGuide(Employee):

    def __init__(
        self,
        employee_id,
        first_name,
        last_name,
        age,
        national_id,
        address,
        phone,
        years_of_experience,
        hire_date,
        job_title,
        work_schedule,
        salary,
        username,
        password
    ):
        super().__init__(
            employee_id,
            first_name,
            last_name,
            age,
            national_id,
            address,
            phone,
            years_of_experience,
            hire_date,
            job_title,
            work_schedule,
            salary,
            username,
            password
        )
        self.availability = []



class FinancialManager(Employee):

    def __init__(
        self,
        employee_id,
        first_name,
        last_name,
        age,
        national_id,
        address,
        phone,
        years_of_experience,
        hire_date,
        job_title,
        work_schedule,
        salary,
        username,
        password
    ):
        super().__init__(
            employee_id,
            first_name,
            last_name,
            age,
            national_id,
            address,
            phone,
            years_of_experience,
            hire_date,
            job_title,
            work_schedule,
            salary,
            username,
            password
        )




class Manager(User):

    def __init__(
        self,
        manager_id,
        first_name,
        last_name,
        age,
        national_id,
        phone,
        username,
        password
    ):
        super().__init__(username, password)

        self.manager_id = manager_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.national_id = national_id
        self.phone = phone                                      


class PersonalInfo:

    def __init__(
        self,
        guest_id,
        first_name,
        last_name,
        age,
        national_id,
        phone,
        address
    ):
        self.guest_id = guest_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.national_id = national_id
        self.phone = phone
        self.address = address




class Reservation:

    def __init__(
        self,
        reservation_id,
        guests: list[PersonalInfo],
        number_of_guests,
        room,
        number_of_nights
    ):
        self.reservation_id = reservation_id
        for guest in guests:
            if not isinstance(guest,PersonalInfo):
                raise TypeError("guest must be a personalinfo object")
        self.guests = guests

        self.number_of_guests = number_of_guests
        self.room = room
        self.number_of_nights = number_of_nights
        self.services = []


class Service:

    def __init__(
        self,
        reservation_id,
        service_type,
        date,
        start_time,
        price
    ):
        self.reservation_id = reservation_id
        self.service_type = service_type
        self.date = date
        self.start_time = start_time
        self.price = price




class Kitchenassistant(Employee):

    def __init__(
        self,
        employee_id,
        first_name,
        last_name,
        age,
        national_id,
        address,
        phone,
        years_of_experience,
        hire_date,
        job_title,
        work_schedule,
        salary,
        username,
        password
    ):

        super().__init__(
            employee_id,
            first_name,
            last_name,
            age,
            national_id,
            address,
            phone,
            years_of_experience,
            hire_date,
            job_title,
            work_schedule,
            salary,
            username,
            password
        )

        self.shift = {}




def select_services(reservation_id):

    services = []

    translator = input("Do you want a translator? (yes/no): ")

    if translator == "yes":
        date = input("Enter date: ")
        start_time = input("Enter start time: ")

        service = Service(
            reservation_id=reservation_id,
            service_type="TRANSLATOR",
            date=date,
            start_time=start_time,
            price=4
        )

        services.append(service)

    driver = input("Do you want a driver? (yes/no): ")

    if driver == "yes":
        car_type = input("Choose car type (normal/luxury): ")
        date = input("Enter date: ")
        start_time = input("Enter start time: ")

        if car_type == "normal":
            price = 2

        elif car_type == "luxury":
            price = 3.5

        else:
            raise ValueError("Invalid car type")

        service = Service(
            reservation_id=reservation_id,
            service_type="DRIVER",
            date=date,
            start_time=start_time,
            price=price
        )

        services.append(service)

    tour_guide = input("Do you want a tour guide? (yes/no): ")

    if tour_guide == "yes":
        date = input("Enter date: ")
        start_time = input("Enter start time: ")

        service = Service(
            reservation_id=reservation_id,
            service_type="TOUR_GUIDE",
            date=date,
            start_time=start_time,
            price=5
        )

        services.append(service)

    food = input("Do you want food service? (yes/no): ")

    if food == "yes":
        date = input("Enter date: ")
        meal = input("Choose meal (breakfast/lunch/dinner): ")

        service = Service(
            reservation_id=reservation_id,
            service_type="FOOD",
            date=date,
            start_time=None,
            price=0
        )

        services.append(service)

    return services


reservation.services = select_services(reservation.reservation_id)
for service in reservation.services:
    print(service.service_type)





def housekeeper_schedule(housekeepers):

    long_count = 25
    night_count = 10
    off_count = 15

    for day in range(1, 31):

        daily_shifts = []

        daily_shifts.extend(["LONG"] * long_count)
        daily_shifts.extend(["NIGHT"] * night_count)
        daily_shifts.extend(["OFF"] * off_count)

        shift_offset = (day - 1) % len(housekeepers)

        daily_shifts = (
            daily_shifts[shift_offset:]
            + daily_shifts[:shift_offset]
        )

        for employee_index, housekeeper in enumerate(housekeepers):

            housekeeper.shift[day] = daily_shifts[employee_index]



def get_housekeepers_by_shift(housekeepers, day, shift_type):

    selected_housekeepers = []

    for housekeeper in housekeepers:

        shift = housekeeper.shift[day]

        if shift == shift_type:
            selected_housekeepers.append(housekeeper)

    return selected_housekeepers



def assign_housekeeper_floors(housekeepers, month):

    number_of_floors = 12

    for index, housekeeper in enumerate(housekeepers):

        floor = ((index + month - 1) % number_of_floors) + 1

        housekeeper.floor = floor


def assign_rooms_to_housekeepers(housekeepers, rooms, day):

    long_housekeepers = get_housekeepers_by_shift(
        housekeepers,
        day,
        "LONG"
    )

    night_housekeepers = get_housekeepers_by_shift(
        housekeepers,
        day,
        "NIGHT"
    )

    working_housekeepers = long_housekeepers + night_housekeepers

    if not working_housekeepers:
        return

    rooms_by_floor = {}

    for room in rooms:

        if room.floor not in rooms_by_floor:
            rooms_by_floor[room.floor] = []

        rooms_by_floor[room.floor].append(room)

    for floor, floor_rooms in rooms_by_floor.items():

        floor_housekeepers = [
            housekeeper
            for housekeeper in working_housekeepers
            if housekeeper.floor == floor
        ]

        if not floor_housekeepers:
            continue

        for housekeeper in floor_housekeepers:
            housekeeper.room_schedule[day] = []

        for index, room in enumerate(floor_rooms):

            housekeeper = floor_housekeepers[
                index % len(floor_housekeepers)
            ]

            housekeeper.room_schedule[day].append(room)




CLEANING_CHECKLIST = ["MAKE_BED","CLEAN_BATHROOM","CLEAN_WINDOWS","VACUUM_FLOOR",
                      "EMPTY_TRASH", "DUST_FURNITURE"]


def create_cleaning_checklist(room):

    room.cleaning_checklist = {
        task: False
        for task in CLEANING_CHECKLIST
    }



def show_cleaning_checklist(room):

    print(f"\nCleaning checklist for room {room.room_number}")

    for task, completed in room.cleaning_checklist.items():

        status = "DONE" if completed else "NOT DONE"

        print(f"{task}: {status}")



def complete_cleaning_task(room, task):

    if task not in room.cleaning_checklist:
        raise ValueError("Invalid cleaning task")

    room.cleaning_checklist[task] = True



def receptionist_schedule(receptionists):

    long_count = 11
    night_count = 5
    off_count = 6

    for day in range(1, 31):

        daily_shifts = []

        daily_shifts.extend(["LONG"] * long_count)
        daily_shifts.extend(["NIGHT"] * night_count)
        daily_shifts.extend(["OFF"] * off_count)

        shift_offset = (day - 1) % len(receptionists)

        daily_shifts = (
            daily_shifts[shift_offset:]
            + daily_shifts[:shift_offset]
        )

        for employee_index, receptionist in enumerate(receptionists):

            receptionist.shift[day] = daily_shifts[employee_index]



def get_receptionists_by_shift(receptionists, day, shift_type):

    selected_receptionists = []

    for receptionist in receptionists:

        shift = receptionist.shift[day]

        if shift == shift_type:
            selected_receptionists.append(receptionist)

    return selected_receptionists   



def chef_schedule(chefs):

    chefs_per_day = 2

    for day in range(1, 31):

        first_chef_index = ((day - 1) * chefs_per_day) % len(chefs)

        for chef in chefs:
            chef.shift[day] = "OFF"

        for i in range(chefs_per_day):

            chef_index = (
                first_chef_index + i
            ) % len(chefs)

            chefs[chef_index].shift[day] = "WORK"



def kitchen_assistant_schedule(kitchen_assistants):

    group_size = 5
    
    group_a = kitchen_assistants[:group_size]
    group_b = kitchen_assistants[group_size:]

    for day in range(1, 31):

        if day % 2 == 1:
            working_group = group_a
            off_group = group_b
        else:
            working_group = group_b
            off_group = group_a

        for assistant in working_group:
            assistant.shift[day] = "WORK"

        for assistant in off_group:
            assistant.shift[day] = "OFF"



def set_available(employee , days):
    employee.availability = days
    
