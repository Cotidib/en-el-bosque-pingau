from django.contrib import admin
from reservations.models import Day, Time, Reservation

# Register your models here.
admin.site.register(Day)
admin.site.register(Time)
admin.site.register(Reservation)