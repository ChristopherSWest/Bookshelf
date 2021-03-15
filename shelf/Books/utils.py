import requests


#print(book_response)


def show_book_details(isbn):
    book_request = requests.get(f'https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&jscmd=data&format=json')
    book_details = []
    book_response = book_request.json()
    print(book_response)
    for book in book_response:
        print(book)
        for item in book_response[book]:
            
            book_details.append(f"{item}: {book_response[book][item]}")

    return book_details

show_book_details('0838535623')

class Book():
    def __init__(self, isbn):
        book_request = requests.get(f'https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&jscmd=data&format=json')
        book_response = book_request.json()
        self.isbn = isbn
        self.title = book_response[f'ISBN:{isbn}']['title']
        self.authors = book_response[f'ISBN:{isbn}']['authors'][0]['name']
        try:
            self.cover = book_response[f'ISBN:{isbn}']['cover']['medium']
        except KeyError:
            self.cover = None
    
    def show_details(self):
        test = 'test'
        results = f"{self.isbn}, {self.title}, {self.authors}"
        return results

'''book = Book(9780525510543)

book.show_details()'''


            
