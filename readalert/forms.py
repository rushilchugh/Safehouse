__author__ = 'Rushil'

from django.forms import ModelForm
from .models import UserProfile


class UserForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'mobile']
