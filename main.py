from datetime import datetime
import application.salary
import application.db.people

if __name__ == '__main__':
    date_and_time = datetime.today()
    print(date_and_time)
    print(application.salary.calculate_salary(128,375))
    print(application.db.people.get_employees(35, 128))