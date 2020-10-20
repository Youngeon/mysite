from django.shortcuts import render
from .models import Randomizer
from .forms import RandForm
from random import choice

def index(request):
    
    if(request.method == "POST"):# Проверяем запрос
        words = Randomizer.objects.all()
    
    
    words = Randomizer.objects.all()
    ranword = choice(words.values())
    ranword = ranword['word']
    context = {'info': ranword}
    return render(request, 'randomizer.html', context)