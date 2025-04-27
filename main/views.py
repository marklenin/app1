from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title':'Home - Main',
        'content': 'Furniture store Home'
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title':'Home - About us',
        'content': 'About us',
        'text_on_page': "Text about this store, and why it is the best."
    }
    return render(request, 'main/about.html', context)