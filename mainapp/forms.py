from django import forms
from mainapp.models import Director, Movie


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = 'name '.split()

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ' director title description image '.split()
