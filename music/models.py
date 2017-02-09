from django.db import models



class Person(models.Model):
	name = models.CharField(max_length=200)
	#birthday = models.DateTimeField(max_length=200)

	def __str__(self):
		return self.name


class Album(models.Model):
	#album_person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
	artist = models.CharField(max_length=250)
	album_title = models.CharField(max_length=500)
	genre = models.CharField(max_length=100)
	album_logo = models.CharField(max_length=1000)
	author = models.CharField(max_length=200)

	person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.album_title + ' - ' + self.artist 


class Song(models.Model):
	file_type = models.CharField(max_length=10)
	song_title = models.CharField(max_length=250)
	singer = models.CharField(max_length=200)

	album = models.ManyToManyField('Album')
	person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.song_title