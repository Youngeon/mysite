from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'values':['Если у Вас остались вопросы, то задавайте их по телефону', '(***)-***-**-**']})



# Create your views here.