from django.db import models
import datetime
from multiselectfield import MultiSelectField

# Create your models here.

a = []
c=0
for i in range(8):
	for j in range(10):
		b = (c + 1, (F"{i+1}_{j+1}"))
		a.append(b)
		c += 1

SEAT_CHOICE = tuple(a)

ROOM_CHOICE = (
	(1,("Hall")),
	(2,("Mini")),
	(3,("Makro"))
	)

# class Movie(models.Model):
# 	name = models.CharField(max_length=50)

# 	def __str__(self):
# 		return self.name

# class Hall(models.Model):
# 	room = models.CharField(max_length=10)
# 	available_seets = models.IntegerField()

# 	def __str__(self):
# 		return self.room

class Presentation(models.Model):
	movie = models.CharField(max_length=50)
	presentation_date = models.DateTimeField(default=datetime.datetime.now)
	 # = models.ForeignKey(Movie, on_delete=models.CASCADE)
	room = models.IntegerField(choices=ROOM_CHOICE)
	
	class Meta:
		constraints = [models.UniqueConstraint(fields=['movie','room', 'presentation_date'], name='unique_movie') ]
	def __str__(self):
		return F"{self.movie} in {self.room}"

class Booking(models.Model):
	custommer_email = models.EmailField()
	movie = models.ForeignKey(Presentation, on_delete=models.CASCADE)
	phone = models.CharField(max_length=14)
	seats = models.IntegerField(choices=SEAT_CHOICE)
	# seats = MultiSelectField(choices=SEAT_CHOICE)
	class Meta:
		constraints = [models.UniqueConstraint(fields=['movie','seats'], name='unique_booking') ]

	def __str__(self):
		return self.custommer_email
		