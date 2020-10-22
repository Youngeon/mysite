from django.shortcuts import render
from .models import Randomizer,Item1,Item2,Item3,Item4,Item5,Item6,Item7,Item8,Item81,Item82
from .forms import RandForm
from random import choice

def index(request):
    
    if(request.method == "POST"):# Проверяем запрос
        words = Randomizer.objects.all()
    
    items = [Item1,Item2,Item3,Item4,Item5,Item6,Item7,Item8,Item81,Item82]
    random_items = []
    for item in items:
        words = item.objects.all()
        ranword = choice(words.values())
        ranword = ranword['item']
        
        random_items.append(ranword)
    all_items = {
        'Item1': random_items[0],
        'Item2': random_items[1],
        'Item3': random_items[2],
        'Item4': random_items[3],
        'Item5': random_items[4],
        'Item6': random_items[5],
        'Item7': random_items[6],
        'Item8': random_items[7],
        'Item81': random_items[8],
        'Item82': random_items[9],
    }

    context = {'info': all_items}
    return render(request, 'randomizer.html', context)