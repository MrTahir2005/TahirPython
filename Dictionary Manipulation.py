# 3. Dictionary Manipulation
# Library dictionary with book titles and their availability
library = {
    "1984": True,
    "To Kill a Mockingbird": True,
    "The Great Gatsby": False,
    "Moby Dick": True,
    "Pride and Prejudice": False
}

# Function to check if a book is available
def is_book_available(book_title):
    return library.get(book_title, None)

# Function to borrow a book
def borrow_book(book_title):
    if library.get(book_title):
        library[book_title] = False
        print(f"You have borrowed '{book_title}'.")
    else:
        print(f"Sorry, '{book_title}' is not available.")

# Function to return a book
def return_book(book_title):
    if book_title in library:
        library[book_title] = True
        print(f"Thank you for returning '{book_title}'.")
    else:
        print(f"'{book_title}' is not in the library.")

# Example Usage
print("Library books:", library)

# Check availability
book = "1984"
print(f"Is '{book}' available?", is_book_available(book))

# Borrow a book
borrow_book("1984")
print("Library books after borrowing:", library)

# Return a book
return_book("1984")
print("Library books after returning:", library)
