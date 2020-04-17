from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Booking

class RegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'password1',
			'password2',
			)
	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']

		if commit:
			user.save()

		return user

class BookingForm(ModelForm):

    class Meta:
        model = Booking
        fields = '__all__'


