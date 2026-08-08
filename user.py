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


