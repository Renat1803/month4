from django import forms
from django.contrib.auth.models import User

from mainapp.models import Director, Movie


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = 'name '.split()

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ' director title description image '.split()

class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    password1 = forms.CharField()

    def save(self):
        """Create user"""
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = User.objects.create_user(username=username, password=password)
        return user

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))




