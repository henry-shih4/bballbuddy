from django.forms import ModelForm
from .models import Room, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class myUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1', 'password2']



class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']



class UserForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'bio', 'avatar' ]