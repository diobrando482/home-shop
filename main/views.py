from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    context = {
        'title':'home',
        'content':'главная страница home которую я создал в словаре с помощью placeholder',
        'list': ['first','second'],
        'dict': {'first': 1},
        'is_authenticated':False
    }    
    
    return render(request,'main/index.html',context)


def about(request):
    return HttpResponse("about page")