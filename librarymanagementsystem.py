library = {}

# Function to add a book to the library
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")
    copies = int(input("Enter the number of copies: "))
    library[isbn] = {
        'title': title,
        'author': author,
        'copies': copies,
    }
    print(f"Book '{title}' added to the library.")

# Function to search for a book by title or author
def search_book():
    search_term = input("Enter book title or author: ")
    found_books = []
    for isbn, book in library.items():
        if search_term.lower() in book['title'].lower() or search_term.lower() in book['author'].lower():
            found_books.append(book)
    if found_books:
        print("\nFound books:")
        for book in found_books:
            print(f"Title: {book['title']}, Author: {book['author']}, Copies available: {book['copies']}")
    else:
        print(f"No books found matching '{search_term}'.")

# Function to borrow a book
def borrow_book():
    isbn = input("Enter ISBN of the book you want to borrow: ")
    if isbn in library:
        if library[isbn]['copies'] > 0:
            library[isbn]['copies'] -= 1
            print(f"You have successfully borrowed '{library[isbn]['title']}'.")
        else:
            print("Sorry, there are no copies available for this book.")
    else:
        print("Book not found in the library.")

# Function to return a book
def return_book():
    isbn = input("Enter ISBN of the book you want to return: ")
    if isbn in library:
        library[isbn]['copies'] += 1
        print(f"Thank you for returning '{library[isbn]['title']}'.")

# Main loop
while True:
    print("\nLibrary Management System")
    print("1. Add a book")
    print("2. Search for a book")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        search_book()
    elif choice == '3':
        borrow_book()
    elif choice == '4':
        return_book()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")