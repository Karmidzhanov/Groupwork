import datetime

from django.utils import timezone
from django.test import TestCase
from polls.models import Question
from django.core.urlresolvers import reverse


class UserMethodTests(TestCase):

    def create_user(username, first, last, password):
		
		return User.objects.create(username = username, first_name = first, last_name = last, password = password )
		
		
	def test_Name(self):
        
        self.assertEqual(self.Name(), self.first_name + " " + last_name)

		
class CadetMethodTests(TestCase):

    def create_cadet(username, first, last, password, xnumber, company, sport):
		
		return Cadet.objects.create(username = username, first_name = first, last_name = last, password = password, xnumber = xnumber, company = company, password = password )
		
		
	def test_permission(self):
        
        self.assertEqual(self.is_staff, False)
    

class MealTests(TestCase):

    def create_meal(date, meal_type, meal_description):
		self.assertEqual(self.isinstance(datetime.date), True)
		self.assertEqual(self.meal_type in self.meal_type_choices, True)
		self.assertEqual(self.meal_description.max_length, 255)
		return Meal.objects.create(date = date, meal_type = meal_type, meal_description = meal_description )

    