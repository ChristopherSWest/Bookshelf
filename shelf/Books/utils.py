import requests
from . import models
from django.contrib.auth.models import User


#print(book_response)

#testing script
'''def show_book_details(isbn):
    book_request = requests.get(f'https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&jscmd=data&format=json')
    book_details = []
    book_response = book_request.json()
    print(book_response)
    for book in book_response:
        print(book)
        for item in book_response[book]:
            
            book_details.append(f"{item}: {book_response[book][item]}")

    return book_details

show_book_details('9780618260300')'''

class Book():
    def __init__(self, isbn):
        book_request = requests.get(f'https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&jscmd=data&format=json')
        book_response = book_request.json()
        self.isbn = isbn
        self.title = book_response[f'ISBN:{isbn}']['title']
        try:
            self.authors = book_response[f'ISBN:{isbn}']['authors'][0]['name']
        except:
            self.authors = None
        self.publisher = book_response[f'ISBN:{isbn}']['publishers'][0]['name']
        try:
            self.published_date = book_response[f'ISBN:{isbn}']['publish_date']
        except:
            self.published_date = None
        try:
            self.cover = book_response[f'ISBN:{isbn}']['cover']['medium']
        except KeyError:
            self.cover = None
        try:
            self.number_of_pages = book_response[f'ISBN:{isbn}']['number_of_pages']
        except:
            self.number_of_pages = 'unknown'
        try:
            self.subjects = []
            for item in book_response[f'ISBN:{isbn}']['subjects']:
                self.subjects.append(item["name"])
            self.last_subject = len(self.subjects) - 1
        except KeyError:
            self.subjects = None
            self.last_subject = 0
    def show_details(self):
        test = 'test'
        results = f"{self.isbn}, {self.title}, {self.authors}"
        return results

# A function to add a book to the database
def add_book(book,user):
    
    try:
        user_object = User.objects.get(username=user)
        b = models.Book(isbn=book.isbn,title=book.title,author=book.authors,cover_url=book.cover,publisher=book.publisher,published_date=book.published_date,subjects=book.subjects)
        b.save()
        b.owner.add(user_object.id) 
        
    except:
        user_object = User.objects.get(username=user)
        b = models.Book.objects.get(isbn=book.isbn)
        b.owner.add(user_object.id)

# function to list all of the user's books
def show_my_books(user):
    user_object = User.objects.get(username=user)
    my_books = models.Book.objects.filter(owner=user_object.id)
    return my_books

#function to show all of the books in the database
def show_all_books():
    all_books = models.Book.objects.all()
    return all_books
            
