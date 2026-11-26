class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    # Method suggested by an AI coding assistant
    def issue_book(self):
        if not self.available:
            print(f'"{self.title}" is already issued.')
            return

        self.available = False
        print(f'"{self.title}" has been issued.')


books = [
    Book("Python Basics", "John Smith"),
    Book("Clean Code", "Robert Martin"),
    Book("AI Fundamentals", "Alice Brown"),
]

for book in books:
    status = "Available" if book.available else "Issued"
    print(f"{book.title} by {book.author} - {status}")

books[0].issue_book()
books[0].issue_book()  # Prevents issuing the same book twice

# Change made: added an availability check so an issued book cannot be issued again.