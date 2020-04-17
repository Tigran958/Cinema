from rest_framework import serializers
from . models import *


a = []
c=0
for i in range(6):
	for j in range(8):
		b = (c + 1, (F"{i+1}_{j+1}"))
		a.append(b)
		c += 1

SEAT_CHOICE = tuple(a)

class PresentationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Presentation
		fields = ('id','presentation_date','movie','room')



class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['id','movie','custommer_email','phone','seats']

	# seats = serializers.MultipleChoiceField(choices=SEAT_CHOICE)