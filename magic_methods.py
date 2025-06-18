class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages"
    
    def __repr__(self):
        return f"Book(title ='{self.title}', author='{self.author}', pages={self.pages})"
    
b1 = Book("The Alchemist", "Philip Gisore", 2003)
print(str(b1)) #calls __str__()
print(repr(b1)) #calls __repr__()