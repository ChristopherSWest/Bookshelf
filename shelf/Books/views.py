from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "books/index.html")

def title(request, title):
    return render(request, "books/title.html" , {
        "title": title
    })

def add(request):
    return render(request, 'books/add.html')
