from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView

from .forms import NewUserCreationForm


class Signup(CreateView):
    """Allow a user to signup"""
    model = User
    form = NewUserCreationForm

    def form_valid(self, form):
        """Validate the form"""
        new_user = form.commit(save=False)
        new_user.user = new_user
        new_user.first_name = form.cleaned_data['first_name']
        new_user.last_name = form.cleaned_data['last_name']
        new_user.save()
        return super().form_valid(form)
