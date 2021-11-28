import datetime
from django.db import models
from django.utils import timezone

class Page(models.Model):
    page_name = models.CharField(max_length=200)
    page_url = models.CharField(max_length=200)
    def __str__(self):
        return self.page_name

class Subpage(models.Model):
    page = models.ForeignKey(Page,on_delete=models.PROTECT)
    subpage_name = models.CharField(max_length=20)
    subpage_anchor = models.CharField(max_length=200)
    def __str__(self):
        return self.subpage_name
    
class Gallery(models.Model):
    gallery_name = models.CharField(max_length=200)
    def __str__(self):
        return self.gallery_name

class Image(models.Model):
    gallery = models.ForeignKey(Gallery,on_delete=models.PROTECT)
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='image') 
    def __str__(self):
        return self.name
    class Meta:
        db_table = "filmbts"

class CreditArea(models.Model):
    area_name = models.CharField(max_length=200)
    def __str__(self):
        return self.area_name


class Credit(models.Model):
    person_name = models.CharField(max_length=200)
    person_role = models.CharField(max_length=200)
    person_area = models.ForeignKey(CreditArea,on_delete=models.PROTECT)
    def __str__(self):
        return self.person_name + " " + self.person_role + " " + self.person_area.area_name