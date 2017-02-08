from django.test import TestCase

# Create your tests here.
from music.models import Person


class PersonTestCase(TestCase):
	
	def setUp(self):
		Person.objects.create(name="Person1")
		Person.objects.create(name="Person2")


	def test_person_is_exists(self):
		person = Person.objects.get(name='Person1')
		for people in Person.objects.all():
			print 'p', people, people.name
		self.assertEqual(person.name, 'Person1')