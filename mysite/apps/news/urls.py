from django.urls import path
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from news.models import Articles
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:article_id>/', views.detail, name = 'detail'),
    path('<int:article_id>/leave_comment', views.leave_comment, name = 'leave_comment'),
   # url(r'^$', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20], 
    #template_name="news/posts.html")),
    #url('^(?P<pk>\d+)$', DetailView.as_view(model = Articles, template_name ="news/post.html"))
    
 ]  