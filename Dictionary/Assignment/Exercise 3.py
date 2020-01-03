# Excersise 13.3 Chapter 13 Assignment
# Tissan Kugathas
# ICS4U0
# November 28 2019

# Initializes the libarary dictionary
library = dict()

# if called, it adds the a book to the library
def _addBook():
    # Gets the name of the book
    name = input('Enter the name of the book: ')
    # creates a dictionary inside the library dictionary
    library[name] = dict()
    # asks the user for the author's first name of the book
    library[name]['author_first_name'] = input('Enter first name of the author of {}: '.format('"'+name+'"'))
    # asks the user for the author's last name of the book
    library[name]['author_last_name'] = input('Enter last name of the author of {}: '.format('"'+name+'"'))
    # asks the user for location number of the book
    library[name]['located'] = int(input('Enter the location number of {} by {} {}: '.format('"'+name+'"',library[name]['author_first_name'],library[name]['author_last_name'])))
    print()

#if called, finds the book in the library
def findBookLocation():
    # asks the user what the name of the book they are looking for
    name = input('Enter the name of the book: ')
    # asks the full name of the author of the book
    author = input("Enter the author's full name of {}: ".format('"'+name+'"'))
    # splits the first name and last name of the author
    author = author.split(' ')
    # this variable keeps track if the book is found as the book may not be in the library
    notfound = True
    # goes through each book to see if the name and author matches the book
    for book in library.keys():
        if name == book:
            if author[0] == library[book]['author_first_name'] and author[1] == library[book]['author_last_name']:
                notfound = False
                # if the book is found it tells the user where that book is located
                print('The {} is located in {}'.format('"'+book+'"',library[book]['located']))
    # if the book is not found then it tells the user that the library does not have it
    if notfound:
        print('This book is not in the library.')

# if called, list all the book that certain author wrote
def listAuthorBooks():
    # asks the user to enter the full name of the author
    author = input('Enter the full name of the author: ')
    # splits the first name and last name of the author
    author = author.split()
    # a list to keep track of the books that the author wrote
    authorbooks = []
    # this variable keeps track if the library has no books written by this author
    notfound = True
    # goes through all the books in the library to look for books written by the author
    for book in library.keys():
        if library[book]['author_first_name'] == author[0] and author[1] == library[book]['author_last_name']:
            notfound = False
            # if the book is written by the author then it will put that book into the authorbooks list
            authorbooks.append(book)
    # if there are no books written by the author then it will the user that library does not have any book from that author
    if notfound:
        print('There are no books written by {} {} in this library')
    else:
        print('The author has writen the book(s): ')
        for book in authorbooks:
            print('"'+book+'"')



# Asks the user how many books there are in the library
num_of_books = int(input("Enter the number of books in the libary: "))

# A for loop to get the info about the books in the library from the user
for book in range(num_of_books):
    _addBook()

# a bool variable that will run the user interface of library's search system
status = True

# a loop to run the user interface of the library's search system
while status:

    print()
    print('Option 1: Find book by title and author')
    print('Option 2: List book from an author')
    print('Option 3: Add a book to library')
    print('Option 4: Quit the application')
    print()

    # asks the user what they want to do
    choice = int(input('Enter a option: '))

    # runs a certain function according to the user's choice
    if choice == 1:
        findBookLocation()
    elif choice == 2:
        listAuthorBooks()
    elif choice == 3:
        _addBook()
    elif choice == 4:
        status = False
        break
