from django.shortcuts import render
from .forms import AnimeForm
from django.http import HttpResponseRedirect
from .models import Anime
from jikanpy import Jikan


def index(request):
    jikan = Jikan()
    if(request.method == "POST"):# Проверяем запрос
        form = AnimeForm(request.POST) 
        form.save()
    
    form = AnimeForm() # Erase form 
    
    
    animes = Anime.objects.all()

    all_animes = []
    for anime in animes:
        for i in range(20):
            try:
                inputanime = anime.name
                res = jikan.search('anime', inputanime, page=1)
                anime_info = {
                    'title': res["results"][i]["title"],
                    'score': res["results"][i]["score"],
                    'rated': res["results"][i]["rated"],
                    'episodes': res["results"][i]["episodes"],
                    'image': res["results"][i]["image_url"],
                    'synopsis': res["results"][i]["synopsis"]
                }
                all_animes.append(anime_info) 
            except:
                pass
    all_revanime  = reversed(all_animes)
    context = {'all_info': all_revanime, 'form': form}
    return render(request, 'anime.html', context)