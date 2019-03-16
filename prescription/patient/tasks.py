from .models import Person
from prescription.celery import app

@app.task
def add_person(first_name, last_name, age, prescription,exp_date):
    person = Person.objects.create(
        first_name=first_name,
        last_name=last_name,
        age=age,
        prescription=prescription,
        exp_date=exp_date
    )
