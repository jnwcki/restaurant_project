from django import forms
from django.contrib.auth.forms import UserCreationForm


class NewUserCreationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    number = forms.CharField()
    city = forms.CharField()
    zip_code = forms.IntegerField()
    street_namestreet_name = forms.CharField()
    allergies = forms.CharField()
