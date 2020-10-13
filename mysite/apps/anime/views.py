from django.shortcuts import render
from .forms import AnimeForm
from mal import Anime
from django.http import HttpResponseRedirect


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AnimeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/anime/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AnimeForm()
    print(form)

    return render(request, 'anime.html', {'form': form})