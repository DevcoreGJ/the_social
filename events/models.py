from django.db import models

# import a django default class.
# in event class mmake manager status super users only
from django.contrib.auth.models import User

# Create your models here.
class Venue(models.Model):
	name = models.CharField('Venue Name', max_length=120)
	address = models.CharField(max_length=300)
	zip_code = models.CharField('Zip Code', max_length=12)
	phone = models.CharField('Contact Phone', max_length=25, blank=True)
	web = models.URLField('Website Address')
	email_address = models.EmailField('Email Field', blank=True)

	def __str__(self):
		return self.name

class MyClubUser(models.Model):
	first_name = models.CharField('first_name', max_length=30)
	last_name = models.CharField('last_name', max_length=30)
	email = models.EmailField('user_email')

	def __str__(self):
		return self.first_name + ' ' + self.last_name

class Event(models.Model):
	name = models.CharField('Event Name', max_length=120)
	event_date = models.DateTimeField('Event_date')
	#venue = models.CharField(max_length=120), deprecated
	venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE) # event.venue will now pull all of venue
	
	# manager dependent on django user class connected as a foreign key foreign key
	manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL) # models.CharField(max_length=60)
	
	description = models.TextField(blank=True)
	attendees = models.ManyToManyField(MyClubUser, blank=True)
	
	def __str__(self):
		return self.name