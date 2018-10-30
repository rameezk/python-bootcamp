class Book():

    def __init__(self, name, author, pages):
        self.name = name;
        self.author = author;
        self.pages = pages;

    def __str__(self):
        return f"{self.name} by {self.author}"

    def __len__(self):
        return self.pages


book = Book("Lord of the Rings", "J.R.R. Tolkien", 1000)

print(book)
print(len(book))
