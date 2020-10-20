from .models import Randomizer
from django.forms import ModelForm, TextInput

class RandForm(ModelForm):
    class Meta:
        model = Randomizer
        fields = ['word']
        widgets = {'word': TextInput(attrs={
            'class': 'form-control',
            'name': 'word',
            'id': 'word',
            'placeholder':'Введите город'
            })}