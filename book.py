class Book:
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.available = True

    def check_out(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"Title: {self.title} | Author: {self.author} | ISBN: {self.isbn} | Status: {status}"

class Member:
    MAX_BOOKS = 5

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, isbn):
        if len(self.borrowed_books) < Member.MAX_BOOKS:
            self.borrowed_books.append(isbn)
            return True
        return False

    def return_book(self, isbn):
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)
            return True
        return False

    def __str__(self):
        return f"Member ID: {self.member_id} | Name: {self.name}"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.isbn] = book
        print("Book added successfully!")

    def register_member(self, member):
        self.members[member.member_id] = member
        print("Member registered successfully!")

    def find_book(self, keyword):
        results = []

        for book in self.books.values():
            if (keyword.lower() in book.title.lower() or
                keyword.lower() in book.author.lower() or
                keyword == book.isbn):
                results.append(book)
        return results

    def borrow_book(self, member_id, isbn):
        if member_id in self.members and isbn in self.books:
            member = self.members[member_id]
            book = self.books[isbn]

            if not book.available:
                print("Book is already borrowed.")
                return

            if member.borrow_book(isbn):
                book.check_out()
                print("Book borrowed successfully!")
            else:
                print("Borrow limit reached (5 books).")
        else:
            print("Member or Book not found.")

    def return_book(self, member_id, isbn):
        if member_id in self.members and isbn in self.books:
            member = self.members[member_id]
            book = self.books[isbn]

            if member.return_book(isbn):
                book.return_book()
                print("Book returned successfully!")
            else:
                print("This member did not borrow this book.")
        else:
            print("Member or Book not found.")

    def statistics(self):
        total_books = len(self.books)
        available_books = sum(
            1 for book in self.books.values() if book.available
        )

        print("\n===== LIBRARY STATISTICS =====")
        print("Total Books:", total_books)
        print("Available Books:", available_books)
        print("Borrowed Books:", total_books - available_books)

# Main Program
library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. View Statistics")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        isbn = input("Enter ISBN: ")
        year = input("Enter Year: ")

        book = Book(title, author, isbn, year)
        library.add_book(book)

    elif choice == "2":
        name = input("Enter Member Name: ")
        member_id = input("Enter Member ID: ")

        member = Member(name, member_id)
        library.register_member(member)

    elif choice == "3":
        keyword = input("Enter Title, Author, or ISBN: ")

        books = library.find_book(keyword)

        if books:
            print("\nSearch Results:")
            for book in books:
                print(book)
        else:
            print("No books found.")

    elif choice == "4":
        member_id = input("Enter Member ID: ")
        isbn = input("Enter Book ISBN: ")

        library.borrow_book(member_id, isbn)

    elif choice == "5":
        member_id = input("Enter Member ID: ")
        isbn = input("Enter Book ISBN: ")

        library.return_book(member_id, isbn)

    elif choice == "6":
        library.statistics()

    elif choice == "7":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")