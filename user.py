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