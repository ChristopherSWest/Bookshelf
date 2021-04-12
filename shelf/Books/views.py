from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from . import utils
from django.contrib.auth.models import User


class new_book_form(forms.Form):
    isbn = forms.CharField(label="ISBN")

class add_book_form(forms.Form):
    hidden_field = forms.CharField(initial="test")

# Create your views here.
def index(request):
    
    return render(request, "books/index.html", {
        'all_books': utils.show_all_books()
    })

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

def add_success(request, isbn, user):
    form = new_book_form()
    book = utils.Book(isbn)
    results = book.show_details()
    if request.method == 'POST':
        form = new_book_form(request.POST)
        add_form = add_book_form(request.POST)
        if add_form.is_valid():
            return HttpResponseRedirect(reverse("books:add_success", args=[isbn,user]))
        if form.is_valid():
            isbn = form.cleaned_data['isbn']
            return HttpResponseRedirect(reverse("books:add_title", args=[isbn]))
    else:
        form = new_book_form()
        
    return render(request, 'books/add/success.html',{
        "form": new_book_form(),
        "book": book,
        "add_book": utils.add_book(book, user)
    })