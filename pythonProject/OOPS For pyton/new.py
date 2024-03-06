class Book:
    def __init__(self,ISBN,Title,Author,Genre,Publication_Year):
        self._ISBN = ISBN
        self._Title = Title
        self._Author = Author
        self.Genre = Genre
        self._Publication_Year = Publication_Year


    def display(self):
        print(f"The ISBN is {self._ISBN} Title of book is {self._Title} Author is {self._Author} the genre is {self.Genre} Published year is {self._Publication_Year}")

class LibraryMember(Book):
    def __init__(self,ISBN,Title,Author,Genre,Publication_Year,Id,name):
        super().__init__(ISBN,Title,Author,Genre,Publication_Year)
        self.Id = Id
        self.name = name
        self.borrowed_books = []

    def borrowbooks(self,book):
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed the book {self._Title}")

    def returnbook(self,book):
        if self.borrowed_books in book:
            self.borrowed_books.remove(book)
            print(f"{self.name} has returend the {self._Title}")
        else:
            print(f"{self.name} has returend the {self._Title}")

    def display_borrowbook(self):
        print(f"{self.name}'s borrowed book")
        for book in self.borrowed_books:
            print(f"{self._Title} and Published year {self._Publication_Year}")



b1 = Book("231","The cold war","Harry Williasm","fiction","2008")
m1 = LibraryMember("314","The war in ICE","james rolling","Action","2019","31","Amily")

m1.borrowed_books(b1)
m1.display_borrowbook()
m1.returnbook("The cold war")

