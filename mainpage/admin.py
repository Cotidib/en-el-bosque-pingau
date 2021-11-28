from django.contrib import admin
from mainpage.models import Page, Subpage, Gallery, Image, Credit, CreditArea

# Register your models here.
admin.site.register(Page)
admin.site.register(Subpage)
admin.site.register(Gallery)
admin.site.register(Image)
admin.site.register(Credit)
admin.site.register(CreditArea)