from django.contrib.auth.forms import UserCreationForm

class NewUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    number = forms.CharField(max_length=15)
    city = forms.CharField(max_length=128)
    zip_code = forms.IntegerField()
    street_namestreet_name = forms.CharField(max_length=255)
    allergies = forms.TextField()
