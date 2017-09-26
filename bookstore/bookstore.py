class Bookstore(object):
    def __init__(self, name): # a work in progress
        self.name = name
        self.books = []
    
    def add_book(self, book): # a work in progress
        self.books.append(book)
    
    def get_books(self): # a work in progress
        return self.books

    def search_books(self, title=None, author=None): # a work in progress
        search_results = []
        for book in self.books:
            if (title is not None) and (title.lower() in book.title.lower()):
                search_results.append(book)
            if (author is not None) and (author.name == book.author.name):
                search_results.append(book)
        return search_results
    

class Author(object):
    def __init__(self, name, country): # these parameters are set per another test
        self.name = name
        self.nationality = country
        self.books = []
    
    def get_books(self):
        return self.books
    
    
class Book(object):
    def __init__(self, title, author): # these parameters are set per another test
        self.title = title
        self.author = author
        author.books.append(self)
        
    
