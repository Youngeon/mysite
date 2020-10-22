from django.shortcuts import render
from .models import Randomizer,Item1,Item2,Item3,Item4,Item5,Item6,Item7,Item81,Item82
from .forms import RandForm
from random import choice

def index(request):
    
    if(request.method == "POST"):# Проверяем запрос
        words = Randomizer.objects.all()
    
    items = [Item1,Item2,Item3,Item4,Item5,Item6,Item7,Item81,Item82]
    random_items = []
    for item in items:
        words = item.objects.all()
        ranword = choice(words.values())
        ranword = ranword['item']
        print(ranword)
        random_items.append(ranword)
        #random_items.append(choice(item.values()['item'])) 
   # print(random_items)
    #words = Randomizer.objects.all()
    #ranword = choice(words.values())
    #ranword = ranword['word']
    context = {'info': random_items}
    return render(request, 'randomizer.html', context)