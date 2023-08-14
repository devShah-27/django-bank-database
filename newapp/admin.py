from django.contrib import admin
from .models import Role, Country, State, City, UserDetail, UserAddress, BankDetail

admin.site.register(Role)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(UserDetail)
admin.site.register(UserAddress)
admin.site.register(BankDetail)
