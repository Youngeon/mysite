from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Articles
from django.urls import reverse
from django.contrib.auth.models import User


def index(request):
    latest_articles_list = Articles.objects.order_by('-date')[:5]
    return render(request, 'news/posts.html', {'latest_articles_list': latest_articles_list})

def detail(request, article_id):
    try:
        a = Articles.objects.get( id = article_id)
    except:
        raise Http404("Статья не найдена!")

    latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'news/post.html',{'article': a,'latest_comments_list': latest_comments_list})

def leave_comment(request,article_id):
    try:
        a = Articles.objects.get( id = article_id)
    except:
        raise Http404("Статья не найдена!")

    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])
    
    return HttpResponseRedirect( reverse('news:detail',args = (a.id,)) )