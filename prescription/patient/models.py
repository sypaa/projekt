from django.db import models
from django import forms


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    prescription = models.CharField(max_length=180, default='WITAMINA C')
    exp_date = models.DateField(forms.SelectDateWidget)