from django.test import TestCase

# Create your tests here.
from music.models import Person, Song, Album


class PersonTestCase(TestCase):

	def setUp(self):
		Person.objects.create(name="Person1")
		Person.objects.create(name="Person2")


	def create_person(self, name='Person_test'):
		return Person.objects.create(name=name)


	def test_person_creation(self):
		p = self.create_person()
		self.assertTrue(isinstance(p, Person))
		self.assertEqual(p.__str__(), p.name)


	def test_person_is_exists(self):
		person = Person.objects.get(name='Person1')
		for people in Person.objects.all():
			print 'p', people, people.name
		self.assertEqual(person.name, 'Person1')
		self.assertEqual(Person.objects.count(), 2)

		# SQLite3 can pass the following code which is wrong.
		#with self.assertRaises(Exception):
	#		Person.objects.create(name="Person2" * 200)


class SongTestCase(TestCase):

	def setUp(self):
		Song.objects.create(file_type='mp4',
							song_title='J`adore la baguette',
							singer='Unknown')

	def test_song_is_created(self):
		song = Song.objects.get(song_title='J`adore la baguette')
		self.assertEqual(song.song_title, 'J`adore la baguette')
		self.assertEqual(Song.objects.count(), 1)



