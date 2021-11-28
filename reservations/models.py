from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms

class Day(models.Model):
    day = models.DateField()
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.day.strftime("%Y-%m-%d")


class Time(models.Model):
    day = models.ForeignKey(Day,on_delete=models.PROTECT,related_name="day_times")
    time = models.TimeField()
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.day.__str__() + " a las " + self.time.strftime("%H:%M")
        # return self.day.__str__() + " a las " + self.time.__str__()

class Reservation(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField(max_length=200)
    visitors = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
        ]
     )
    # date = models.ForeignKey(Day,on_delete=models.PROTECT) 
    time = models.ForeignKey(Time,on_delete=models.PROTECT)
    def __str__(self):
        return self.user_name + " " + self.time.__str__()




