import unittest
from book import Book
from member import Member
from loan import Loan

class TestLibrarySystem(unittest.TestCase):
    def test_book_creation(self):
        book = Book("1984", "George Orwell")
        self.assertEqual(book.title, "1984")
        self.assertEqual(book.author, "George Orwell")
        self.assertTrue(book.is_available)

    def test_member_creation(self):
        member = Member("Fatemeh")
        self.assertEqual(member.name, "Fatemeh")

    def test_loan_process(self):
        book = Book("1984", "George Orwell")
        member = Member("Fatemeh")
        loan = Loan(book, member)
        self.assertFalse(book.is_available)
        self.assertEqual(str(loan), "Member: Fatemeh borrowed 1984 by George Orwell")

if __name__ == "__main__":
    unittest.main()
