class Book:
    def __init__(self, title, author, genre, year, price):
        self.title  = title
        self.author = author
        self.genre  = genre
        self.year   = year
        self.price  = price


class Library:
    def __init__(self):
        self.books = []  


    # 1. DISPLAY ALL BOOKS
    # Time: O(n) — visits every book once.

    def display_all(self):
        if len(self.books) == 0:
            print("No books found.")
            return
        for i in range(len(self.books)):
            b = self.books[i]
            print(str(i + 1) + ". " + b.title + " | " + b.author +
                  " | " + b.genre + " | " + str(b.year) + " | $" + str(b.price))


    # 2. ADD A BOOK
    # Time: O(1) — same speed whether 1 book or 10,000.

    def add_book(self, book): 
        self.books.append(book)
        print("Book added: " + book.title)


    # 3. DELETE A BOOK
    # Loops through books comparing titles (both lowercased so capitalisation does not matter — "hobbit" matches "The Hobbit").
    # Time: O(n) — worst case checks every book.

    def delete_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print("Book deleted: " + title)
                return
        print("Book not found.")


    # 4. SEARCH BY TITLE OR AUTHOR
    # Loops every book. Uses "in" (substring match) not "==" (exact match) so "Tolk" finds "J.R.R. Tolkien".
    # Time: O(n) — must check every book (list not sorted by name).

    def search_title_author(self, query):
        found = False
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                print(book.title + " by " + book.author)
                found = True
        if not found:
            print("No results found.")


    # 5. SEARCH BY GENRE
    # Time: O(n) — must check every book.

    def search_genre(self, genre):
        found = False
        for book in self.books:
            if book.genre.lower() == genre.lower():
                print(book.title + " by " + book.author)
                found = True
        if not found:
            print("No books found in that genre.")


    # 6. SORT BY YEAR  —  Merge Sort  O(n log n)
    # Asks the user: ascending (oldest first) or descending (newest first). Runs Merge Sort then reverses if needed.

    # WHY MERGE SORT over Bubble Sort?
    #   Bubble Sort: O(n^2) — 1000 books = 1,000,000 comparisons.
    #   Merge Sort:  O(n log n) — 1000 books = ~10,000 comparisons.
    
    # HOW IT WORKS — divide and conquer:
    #   1. Split the list in half repeatedly until every piece 
    #      has 1 book (a list of 1 is already sorted).
    #   2. Merge pairs of sorted pieces back together in order.
    
    # Ascending vs Descending:
    #   Merge Sort always produces ascending order (smallest first).
    #   For descending we simply reverse the sorted list.
    #   Reversing a list is O(n) — fast and straightforward.

    def sort_by_year(self):
        print("  a. Ascending  (oldest first)")
        print("  b. Descending (newest first)")
        order = input("Choose order (a/b): ").strip().lower()

        self.books = self.merge_sort_year(self.books)

        if order == "b":
            self.books = self.reverse_list(self.books)
            print("Books sorted by year: newest first.")
        else:
            print("Books sorted by year: oldest first.")


    # 9. SORT BY AUTHOR NAME  —  Merge Sort  O(n log n)

    # Same idea as sort_by_year but compares author names
    # alphabetically instead of years numerically.
    # .lower() on both sides makes it case-insensitive so "dan brown" and "Dan Brown" sort correctly together.
    # Ascending = A to Z, Descending = Z to A.

    def sort_by_author(self):
        print("  a. Ascending  (A to Z)")
        print("  b. Descending (Z to A)")
        order = input("Choose order (a/b): ").strip().lower()

        self.books = self.merge_sort_author(self.books)

        if order == "b":
            self.books = self.reverse_list(self.books)
            print("Books sorted by author: Z to A.")
        else:
            print("Books sorted by author: A to Z.")


    # MERGE SORT — by year
    # Splits the list in half recursively until base case
    # (0 or 1 item), then merges halves back in sorted order.
    # merge_year compares book.year (integer comparison).

    def merge_sort_year(self, arr):
        if len(arr) <= 1:
            return arr
        mid   = len(arr) // 2
        left  = self.merge_sort_year(arr[:mid])
        right = self.merge_sort_year(arr[mid:])
        return self.merge_year(left, right)

    def merge_year(self, left, right):
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i].year <= right[j].year:
                result.append(left[i])
                i = i + 1
            else:
                result.append(right[j])
                j = j + 1
        while i < len(left):
            result.append(left[i])
            i = i + 1
        while j < len(right):
            result.append(right[j])
            j = j + 1
        return result


    # MERGE SORT — by author name
    # merge_author compares book.author.lower() (string
    # comparison — Python compares strings alphabetically).
    # "a" < "b" is True in Python, so the same <= logic works.

    def merge_sort_author(self, arr):
        if len(arr) <= 1:
            return arr
        mid   = len(arr) // 2
        left  = self.merge_sort_author(arr[:mid])
        right = self.merge_sort_author(arr[mid:])
        return self.merge_author(left, right)

    def merge_author(self, left, right):
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i].author.lower() <= right[j].author.lower():
                result.append(left[i])
                i = i + 1
            else:
                result.append(right[j])
                j = j + 1
        while i < len(left):
            result.append(left[i])
            i = i + 1
        while j < len(right):
            result.append(right[j])
            j = j + 1
        return result


    # REVERSE A LIST
    # Builds a new list by reading the original backwards.
    # Used to turn ascending sort into descending sort.
    # Time: O(n) — visits every item once.

    def reverse_list(self, arr):
        result = []
        i = len(arr) - 1
        while i >= 0:
            result.append(arr[i])
            i = i - 1
        return result


    # 7. SEARCH BY YEAR  —  Binary Search  O(log n)
    # REQUIRES the list to be sorted by year first.
    # If not sorted, Binary Search gives wrong results because it assumes everything left of mid is smaller and everything right of mid is larger — only true when sorted ascending.
    
    # WHY FASTER than a loop?
    #   Loop: up to 1000 checks for 1000 books.
    #   Binary Search: up to 10 checks for 1000 books (log2(1000) ≈ 10).
    #   Each step cuts the remaining search space in half.
    
    # HOW IT WORKS:
    #   low and high mark the current search range.
    #   mid = middle index of that range.
    #   If books[mid].year == target → found.
    #   If target < mid year → answer is in left half, move high left.
    #   If target > mid year → answer is in right half, move low right.
    #   Loop ends when low > high — range is empty, not found.

    def search_by_year(self, year):
        low  = 0
        high = len(self.books) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.books[mid].year == year:
                print("Found: " + self.books[mid].title + " (" + str(self.books[mid].year) + ")")
                return
            elif year < self.books[mid].year:
                high = mid - 1
            else:
                low = mid + 1
        print("No book found for year " + str(year) + ".")


    # 8. LOST BOOK FINE

    # Finds the book by title (linear scan, same as delete).
    # Asks how many days overdue — input() returns a string
    # so int() converts it to a number for the calculation.
    # Fine formula: replacement price + (days x $0.50 daily rate).
    # round(fine, 2) keeps the result to 2 decimal places.
    # Time: O(n) — linear scan to find the book.
    # ----------------------------------------------------------
    def lost_book_fine(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                days = int(input("Days overdue: "))
                fine = book.price + (days * 0.50)
                print("Fine for '" + book.title + "': $" + str(round(fine, 2)))
                return
        print("Book not found.")


# MENU

def print_menu():
    print("\n--- Library Menu ---")
    print("1. Display all books")
    print("2. Add a book")
    print("3. Delete a book")
    print("4. Search by title or author")
    print("5. Search by genre")
    print("6. Sort by year (ascending or descending)")
    print("7. Search by year (sort by year ascending first)")
    print("8. Lost book fine")
    print("9. Sort by author name (ascending or descending)")
    print("0. Exit")


# MAIN

def main():
    lib = Library()

    lib.add_book(Book("The Hobbit",              "J.R.R. Tolkien",  "Fantasy",  1937, 18.99))
    lib.add_book(Book("Dune",                    "Frank Herbert",   "Sci-Fi",   1965, 16.99))
    lib.add_book(Book("1984",                    "George Orwell",   "Fiction",  1949, 14.99))
    lib.add_book(Book("The Da Vinci Code",       "Dan Brown",       "Thriller", 2003, 15.99))
    lib.add_book(Book("John Wick",               "Greg Pak",        "Action",   2017, 12.99))
    lib.add_book(Book("Harry Potter",            "J.K. Rowling",    "Fantasy",  1997, 19.99))
    lib.add_book(Book("The Hunger Games",        "Suzanne Collins", "Action",   2008, 13.99))
    lib.add_book(Book("A Brief History of Time", "Stephen Hawking", "Science",  1988, 17.99))

    while True:
        print_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            lib.display_all()
        elif choice == "2":
            title  = input("Title: ")
            author = input("Author: ")
            genre  = input("Genre: ")
            year   = int(input("Year: "))
            price  = float(input("Price: $"))
            lib.add_book(Book(title, author, genre, year, price))
        elif choice == "3":
            title = input("Title to delete: ")
            lib.delete_book(title)
        elif choice == "4":
            query = input("Enter title or author: ")
            lib.search_title_author(query)
        elif choice == "5":
            genre = input("Enter genre: ")
            lib.search_genre(genre)
        elif choice == "6":
            lib.sort_by_year()
            lib.display_all()
        elif choice == "7":
            year = int(input("Enter year: "))
            lib.search_by_year(year)
        elif choice == "8":
            title = input("Enter title: ")
            lib.lost_book_fine(title)
        elif choice == "9":
            lib.sort_by_author()
            lib.display_all()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


main()
