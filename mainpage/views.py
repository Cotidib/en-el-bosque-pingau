from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import loader
from django.db.models.signals import post_init, pre_delete, post_save
from django.core.mail import EmailMessage
from django.conf import settings

from .models import Page, Subpage, Gallery, Image, Credit, CreditArea
from reservations.models import Reservation, Day, Time

def index(request):
    page__req = Page.objects.all().order_by('id')
    subpage_req = Subpage.objects.all().order_by('id')
    gallery_req = Gallery.objects.get(gallery_name='team')
    # images_req = Image.objects.filter(gallery=gallery_req)
    images_req = gallery_req.image_set.all()
    template = loader.get_template('mainpage/index.html')
    context = {
        'page_req' : page__req,
        'subpage_req' : subpage_req,
        'images_req' : images_req,
    }
    return HttpResponse(template.render(context,request))
    

def film(request):
    page__req = Page.objects.all().order_by('id')
    subpage_req = Subpage.objects.all().order_by('id')
    gallery_bts_req = Gallery.objects.get(gallery_name='bts')
    images_bts_req = gallery_bts_req.image_set.all()
    template = loader.get_template('mainpage/filmpage.html')
    context = {
        'page_req' : page__req,
        'subpage_req' : subpage_req,
        'images_bts_req': images_bts_req,
    }
    return HttpResponse(template.render(context,request))

def installation(request):
    page__req = Page.objects.all().order_by('id')
    subpage_req = Subpage.objects.all().order_by('id')
    template = loader.get_template('mainpage/installationpage.html')
    
    days = Day.objects.filter(available=True)
    days_dic = {}
    for d in days:
        days_dic[d.day]=d.day_times.filter(available=True).values_list("time",flat=True)
    
    if request.method == 'POST':
        reservation_user_name = request.POST.get('name')
        reservation_user_email = request.POST.get('email')
        reservation_visitors = request.POST.get('group')
        
        post_day = request.POST.get('day')
        day_instance = Day.objects.get(day=post_day)
        post_time = request.POST.get('time')
        time_instance = Time.objects.get(time=post_time, day=day_instance.id)
        reservation_time = time_instance
        
        try:
            reservation = Reservation(user_name=reservation_user_name, user_email=reservation_user_email, visitors=reservation_visitors, time=reservation_time)
            reservation.save()
            return redirect('/reserva')

        except Exception as e:
            print(e)

    context = {
        'page_req' : page__req,
        'subpage_req' : subpage_req,
        'days': days_dic,
    }
    return HttpResponse(template.render(context,request))


def credits(request):
    page__req = Page.objects.all().order_by('id')
    subpage_req = Subpage.objects.all().order_by('id')
    corto_credit_req = Credit.objects.filter(person_area=1)
    inst_credits_req = Credit.objects.filter(person_area=2)
    special_credits_req = Credit.objects.filter(person_area=3)
    template = loader.get_template('mainpage/credits.html')
    context = {
        'page_req' : page__req,
        'subpage_req' : subpage_req,
        'corto_credits_req' : corto_credit_req,
        'inst_credits_req': inst_credits_req,
        'special_credits_req': special_credits_req,
    }
    return HttpResponse(template.render(context,request))

def reservation(request):
    page__req = Page.objects.all().order_by('id')
    subpage_req = Subpage.objects.all().order_by('id')
    template = loader.get_template('mainpage/reservationpage.html')
    context = {
        'page_req' : page__req,
        'subpage_req' : subpage_req,
    }
    return HttpResponse(template.render(context,request))



# DJANGO SIGNALS
# https://docs.djangoproject.com/en/3.2/topics/email/

def handleNewReservation(sender, instance, **kwargs):
    time_instance = Time.objects.get(id=instance.time.id)
    time_instance.available = False
    time_instance.save()

    all_times_of_that_day = Time.objects.filter(day=instance.time.day)
    times_availability = all_times_of_that_day.values_list('available', flat=True)
    # si todos son available falso, entonces el dia se saca
    if(all(element == False for element in times_availability)): 
        day_instance = Day.objects.get(id=instance.time.day.id)
        day_instance.available = False
        day_instance.save()
post_init.connect(handleNewReservation, sender=Reservation)

# def handleConfirmationEmail(sender, instance, **kwargs):
#     template = loader.render_to_string('mainpage/emailcontent.html', {'name': instance.user_name, 'date': instance.time, 'visitors':instance.visitors})
#     email = EmailMessage(
#                 'Confirmacion de Reserva',
#                 template,
#                 settings.EMAIL_HOST_USER,
#                 [instance.user_email, settings.EMAIL_HOST_USER],
#             )
#     email.fail_silently = False
#     email.send()
# post_save.connect(handleConfirmationEmail, sender=Reservation)

def handleRemoveReservation(sender,instance,**kwargs):
    time_instance = Time.objects.get(id=instance.time.id)
    time_instance.available = True
    time_instance.save()
pre_delete.connect(handleRemoveReservation, sender=Reservation)