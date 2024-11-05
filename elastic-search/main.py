import random
from faker import Faker
import requests
import json

fake = Faker()


def generate_random_employee():
    employee_id = random.randint(1, 1000)  # Generating a random employee ID
    name = fake.name()  # Generating a random name
    age = random.randint(20, 60)  # Generating a random age between 20 and 60
    department = random.choice(["Finance", "HR", "Engineering", "Marketing", "Sales"])  # Random department
    position = fake.job()  # Generating a random job title
    hire_date = fake.date_between(start_date="-5y", end_date="today").strftime(
        "%Y-%m-%d")  # Random hire date within the last 5 years

    employee_data = {
        "employee_id": str(employee_id),
        "name": name,
        "age": age,
        "department": department,
        "position": position,
        "hire_date": hire_date
    }

    return employee_data


url = "http://localhost:5000/employee"

for _ in range(20):
    payload = json.dumps(generate_random_employee())
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
