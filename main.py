from BookOperations import *
from Book import Book
from Library import Library
from random import randint


def Libros():
    print("Hola mundo")
    authors = ["Alejandro", "Bernardo", "Carlos", "Daniel", "Ezequiel", "Francisco", "Gerardo", "Hernan", "Ismael", "Joaquin"]
    registeredISBNs = []
    editorials = ["Pixar", "Editorial Pepito", "Lenin & Marx"]
    genres = ["Accion", "Terror", "Aventura", "Fantasia", "Detectivesco"]
    for i in range (0, 10):
        randomISBN = randint(100, 900)
        while randomISBN in registeredISBNs:
            randomISBN = randint(100, 900)
        book = Book("title"+str(i), authors[i], randint(100, 500), randomISBN, randint(1900, 2018), editorials[randint(0, len(editorials)-1)], genres[randint(0, len(genres)-1)])
        createBook(book)
    print ("title, author, pageQuantity, isbnNumber, editorionYear, editorial, genre")
    for book in Library.books:
        print(book.title, book.author, book.pageQuantity, book.isbnNumber, book.editionYear, book.editorial, book.genre)
    listAuthors()
    listAllBooks()
    listBooksByEditorial("Pixar")
    listAuthorsByEditorial("Pixar")
    listBooksByEditionWithinRange("Pixar", 1900, 1950)
    listBooksTitleSubstring("Pocahontas")


Libros()
