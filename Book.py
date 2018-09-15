class Book:
    title = ""
    author = []
    pageQuantity = 0
    isbnNumber = 0
    editionYear = 0
    editorial = ""
    genre = ""

    def __init__(self, title, author, pageQuantity, isbnNumber, editionYear, editorial, genre):
        self.title = title
        self.author = author
        self.pageQuantity = pageQuantity
        self.isbnNumber = isbnNumber
        self.editionYear = editionYear
        self.editorial = editorial
        self.genre = genre
