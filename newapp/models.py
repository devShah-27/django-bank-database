# newapp/models.py
from django.db import models

class Role(models.Model):
    USER_TYPE_CHOICES = (
        (1, 'User'),
        (2, 'Seller'),
        (3, 'Admin'),
    )
    user_typename = models.IntegerField(choices=USER_TYPE_CHOICES)

class Country(models.Model):
    country_name = models.CharField(max_length=50)

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=50)

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50)

class UserDetail(models.Model):
    ROLE_CHOICES = (
        (1, 'User'),
        (2, 'Seller'),
        (3, 'Admin'),
    )
    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    )
    u_name = models.CharField(max_length=50)
    u_password = models.CharField(max_length=50)
    u_email = models.EmailField()
    u_phone = models.CharField(max_length=15)
    u_type = models.ForeignKey(Role, on_delete=models.CASCADE)
    u_status = models.CharField(max_length=10, choices=STATUS_CHOICES)

class UserAddress(models.Model):
    u_id = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=100)
    street_name = models.CharField(max_length=100)
    city_name = models.ForeignKey(City, on_delete=models.CASCADE)
    pin_code = models.CharField(max_length=10)

class BankDetail(models.Model):
    u_id = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=12)
    end_month = models.IntegerField(choices=[(i, i) for i in range(1, 13)])
    end_year = models.IntegerField(choices=[(i, i) for i in range(2022, 2031)])