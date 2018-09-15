from Library import Library
import unicodedata


def createBook(book):
    if book in Library().books:
        raise Exception("Tried to insert duplicate book: " + book.title)
    Library().books.append(book)


def deleteBook(book):
    if book not in Library().books:
        __bookNotFound(book.title)
    Library().books.remove(book)


def findBookByTitle(title):
    for book in Library().books:
        if book.title == title:
            return book
        __bookNotFound(title)


def editBook(isbnNumber, book):
    for bk in Library().books:
        if bk.isbnNumber == isbnNumber:
            bk = book
            break
    __bookNotFound(book.title)

def __getUniqueAuthors():
    __listedAuthors = []
    for book in Library().books:
        if book.author not in __listedAuthors:
            __listedAuthors.append(book.author)
    return __listedAuthors


def listAuthors():
    print("#### Autores ####")
    print(__getUniqueAuthors())


def listAllBooks():
    print("#### Libros ####")
    for book in Library().books:
            print(book.title)


def listBooksByGenre(genre):
    print("#### Libros por genero: " + genre + " ####")
    for book in Library().books:
        if book.genre == genre:
            print(book.title)


def listBooksByAuthor(author):
    print("#### Libros por autor: " + author + " ####")
    for book in Library().books:
        if book.author == author:
            print(book.title)


def listBooksByEditorial(editorial):
    print("#### Libros por editorial: " + editorial + " ####")
    for book in Library().books:
        if book.editorial == editorial:
            print(book.title)


def listBooksByEditionWithinRange(editorial, start, end):
    print("#### Libros por editorial: " + editorial + " desde: " + str(start) + " hasta: " + str(end) + " ####")
    for book in Library().books:
        if book.editorial == editorial and start <= book.editionYear <= end:
            print(book.title)


def listAuthorsByEditorial(editorial):
    print("#### Autores por editorial: " + editorial + " ####")
    __listedAuthorsByEditorial = []
    for book in Library().books:
        if book.editorial == editorial:
            if book.author not in __listedAuthorsByEditorial:
                print(book.author)


def listBooksByEditionYear(editionYear):
    print("#### Libros por ano de editorial: " + editionYear + " ####")
    for book in Library().books:
        if book.editionYear == editionYear:
            print(book.title)


def listBooksByAuthorInitialLetter(initialLetter):
    print("#### Libros con autor con letra inicial: " + initialLetter + " ####")
    for book in Library().books:
        if __strip_accents(book.author[0].lower()) == __strip_accents(initialLetter.lower()):
            print(book.title)

def listBooksTitleSubstring(substring):
    print("#### Libros que contienen: " + substring + " ####")
    for book in Library().books:
        if substring in book.title:
            print(book.title)


def __strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def __bookNotFound(title):
    raise Exception("Book not found: " + title)