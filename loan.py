class Loan:
    def __init__(self, book, member):
        if not book.is_available:
            raise Exception("Book not available")
        self.book = book
        self.member = member
        book.is_available = False

    def __str__(self):
        return f"{self.member} borrowed {self.book}"
