import json

class Library:
    def __init__(self):
        self.allBooks = []
        self.options = {1 : self.printAllBooks,
                        2 : self.addBook,
                        3 : self.deleteBook,
                        4 : self.saveToFile,
                        5 : self.loadFromFile
        }
        
    def addBook(self):
        title = input("What is the book called? ")
        author = input("Who wrote the book? ")
        genre = input("What is the books genre? ")        
        newBook = Book(len(self.allBooks),title, author,genre)
        self.allBooks.append(newBook)

    def deleteBook(self):
        searchTerm = input("What book(s) do you want to remove? ")
        possibleBooksToDelete = []
        for b in self.allBooks:
            if b.title == searchTerm or b.author == searchTerm:
                possibleBooksToDelete.append(b)
        if(len(possibleBooksToDelete) == 0):
            print("No books found with that description.")
        if(len(possibleBooksToDelete) == 1):
            print("Removed - ", possibleBooksToDelete[0].title)
            self.allBooks.remove(possibleBooksToDelete[0])
        if(len(possibleBooksToDelete) > 1):
            print("Multiple books found with that description \n")
            for b in possibleBooksToDelete:
                print(b.title, " - ", b.id)
            bookToDelete = input("Type the number of book you want to remove ('x' removes all) - ")
            if(bookToDelete == "x"):
                for b in possibleBooksToDelete:
                    self.allBooks.remove(b)
            else:
                self.allBooks.remove(possibleBooksToDelete[int(bookToDelete)])

    def printAllBooks(self):
         for b in self.allBooks:
            print(b.getTitle(), " - ", b.id)
    
    def saveToFile(self):
        d = dict()
        d['books'] = []
        for b in self.allBooks:
            d['books'].append({
                'ID': b.id,
                'title': b.title,
                'author': b.author,
                'genre': b.genre
            })
        with open('data.txt', 'w') as outfile:        
            json.dump(d, outfile)

    def loadFromFile(self):
        with open('data.txt') as json_file:
            data = json.load(json_file)
            for p in data['books']:
                newBook = Book(p['ID'], p['title'], p['author'], p['genre'])
                self.allBooks.append(newBook)

class Book:
  '''base class for a book'''
  def __init__(self,idNumber, title, author, genre):
    self.id = idNumber
    self.title = title
    self.author = author
    self.genre = genre

  def getTitle(self):
    return self.title

  def setTitle(self, title):
      self.title = title

ourLibrary = Library()

while True:
    choice = input("\n\nWhat do you want to do in your library? \n1 - show books\n2 - add book\n3 - delete books\n4 - save to JSON \n5 - load from JSON\t")
    ourLibrary.options[int(choice)]()
