from django.forms import ModelForm, TextInput
from .models import Anime

class AnimeForm(ModelForm):
    class Meta:
        model = Anime
        fields = ['name']
        widgets = {'name': TextInput(attrs={
            'class': 'form-control',
            'name': 'name',
            'id': 'name',
            'placeholder':'Введите аниме'
            })}