from django.core import validators
from django import forms
from .models import Movie

#I make this using (Model Form Concept).
class MovieRegistration(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name','imdb_score','popularity','director','genre']
        # widgets = {
        #     'name': forms.TextInput(attrs={'class':'form-control'}),
        #     'email': forms.TextInput(attrs={'class':'form-control'}),
        #     'password': forms.PasswordInput(attrs={'class':'form-control'}),
        # }