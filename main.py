class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author}"

class Member:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Member: {self.name}"

class Loan:
    def __init__(self, book, member):
        if not book.is_available:
            raise Exception("Book not available")
        self.book = book
        self.member = member
        book.is_available = False

    def __str__(self):
        return f"{self.member} borrowed {self.book}"

# اجرای اصلی
if __name__ == "__main__":
    book1 = Book("1984", "George Orwell")
    member1 = Member("Fatemeh")
    loan1 = Loan(book1, member1)
    print(loan1)
