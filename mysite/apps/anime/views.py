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
        try:
            inputanime = anime.name
            res = jikan.search('anime', inputanime, page=1)
            anime_info = {
                'title': res["results"][0]["title"],
                'score': res["results"][0]["score"],
                'rated': res["results"][0]["rated"],
                'episodes': res["results"][0]["episodes"],
                'image': res["results"][0]["image_url"],
                'synopsis': res["results"][0]["synopsis"]
            }

            all_animes.append(anime_info) 
        except:
            pass
    all_revanime  = reversed(all_animes)
    context = {'all_info': all_revanime, 'form': form}
    return render(request, 'anime.html', context)