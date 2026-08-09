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
        duration,
        price
    ):
        self.reservation_id = reservation_id
        self.service_type = service_type
        self.date = date
        self.start_time = start_time
        self.price = price



def select_services(resevation_id):
    services = []
Translator = input("do you want a translator?(yes/no)")
if Translator == "yes":
    date = input("enter date")
    start_time = input("Enter start time:")

    service = Service(reservation_id = reservation_id,service_type = "Translator",date = date ,start_time = start_time,price = 4)
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



    food = input("do you want food service? (yes/no):")
    if food == "yes":
        date = input("Enter date:")
        meal = input("choose meal (breakfast/lunch/dinner):")

        service = Service(reservation_id=Reservation_id,service_type="FOOD",date=date,start_time=None,price=0)
        services.append(service)


    