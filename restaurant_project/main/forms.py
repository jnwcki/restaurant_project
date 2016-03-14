from django import forms
from django.contrib.auth.forms import UserCreationForm


class NewUserCreationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    number = forms.CharField()
    city = forms.CharField()
    zip_code = forms.IntegerField()
    address = forms.CharField()
    allergies = forms.CharField()


class NewManagerCreationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    restaurant_name = forms.CharField()
