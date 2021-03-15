from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from . import utils

class new_book_form(forms.Form):
    isbn = forms.CharField(label="ISBN")

# Create your views here.
def index(request):
    return render(request, "books/index.html")

def title(request, title):
    return render(request, "books/title.html" , {
        "title": title
    })

def add(request):
    if request.method == 'POST':
        form = new_book_form(request.POST)
        if form.is_valid():
            isbn = form.cleaned_data['isbn']
            return HttpResponseRedirect(reverse("books:add_title", args=[isbn]))
    else:
        form = new_book_form()
    return render(request, 'books/add.html', {
        "form": new_book_form(),
        
    })

def add_title(request, isbn):
    form = new_book_form()
    book = utils.Book(isbn)
    results = book.show_details()
    test = 'test'
    if request.method == 'POST':
        form = new_book_form(request.POST)
        if form.is_valid():
            isbn = form.cleaned_data['isbn']
            return HttpResponseRedirect(reverse("books:add_title", args=[isbn]))
    else:
        form = new_book_form()
    return render(request, 'books/add/isbn.html',{
        "form": new_book_form(),
        "book": book
    })
