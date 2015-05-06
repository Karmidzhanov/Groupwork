import datetime
#import validators

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 


# You can find an example class diagram for the Model at
# http://yuml.me/edit/53759046
# You'll notice that the Model class provided by Django is
# elided (it doesn't have the attributes or methods listed.

class Admin(User):
	
	is_staff = True 	
	
	def Name(self):
		return self.first_name + " " + self.last_name
	
	def __unicode__(self):
		return self.username

class Cadet(User):
	
	#user = models.OneToOneField(User)
	
	xNumber = models.CharField(max_length = 6)
	company = models.CharField(max_length = 2)
	sport = models.CharField(max_length = 30)	
	
	def Name(self):
		return self.first_name + " " + self.last_name
	
	def __unicode__(self):
		return self.username
		

class Meal(models.Model):
	
	BREAKFAST = 'BF'
	BRUNCH = 'BN'
	LUNCH = 'LU'
	DINNER = 'DN'
	meal_type_choices = (
		(BREAKFAST, 'Breakfast'),
		(BRUNCH, 'Brunch'),
		(LUNCH, 'Lunch'),
		(DINNER, 'Dinner'),
	)
	
	"""def __init__(self, date, meal_type, meal_description):
		self.date = date
		self.meal_type = meal_type
		self.meal_description = meal_description"""
	
	date = models.DateField('Meal Date')
	meal_type = models.CharField('Meal Type',max_length = 2, choices = meal_type_choices)
	meal_description = models.CharField('Menu',max_length=255)
	
	def __unicode__(self):
		return self.date.strftime('%m/%d/%Y') + " " + self.meal_type + " " + self.meal_description