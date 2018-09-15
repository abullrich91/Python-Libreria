class Library:
    books = []
    instance = None

    def __init__(self):
        if not Library.instance:
            Library.instance = Library.__Library(self)

    def __Library(self):
        return self