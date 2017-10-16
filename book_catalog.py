#!/usr/bin/env python3
import pickle
filename = 'book-catalog.bin'

def read_book_catalog():
    with open(filename, 'rb') as file:
        try:
            book_catalog = pickle.load(file)
        except EOFError:
            book_catalog = {}
    return book_catalog

def write_book_catalog(book_catalog):
    with open(filename, 'wb') as file:
        pickle.dump(book_catalog, file)


def show_book(book_catalog):
    title = input("Title: ")
    if title in book_catalog:
        book = book_catalog[title]
        print("Title:    " + title)
        print("Author:   " + book["author"])
        print("Pub year: " + book["pubyear"])
    else:
        print("Sorry, " + title + " doesn't exist in the catalog.")

def list_book(book_catalog):
    for title in book_catalog:
        book = book_catalog[title]
        print('Title:    ', title)
        print('Author:   ', book['author'])
        print('Pub year: ', book['pubyear'])
        print('Press:    ', book['press'])
        print()

def add_edit_book(book_catalog, mode):
    title = input("Title: ")
    if mode == "add" and title in book_catalog:
        print(title + " already exists in the catalog.")
        response = input ("Would you like to edit it? (y/n): ").lower()
        if(response != "y"):
            return
    elif mode == "edit" and title not in book_catalog:
        print(title + " doesn't exist in the catalog.")
        response = input("Would you like to add it? (y/n): ").lower()
        if (response != "y"):
            return

    author = input("Author name: ")
    pubyear = input("Publication year: ")
    press = input('Publication press:')

    # Create a dictionary for the book data
    book = {"author": author,
            'press':press,
            "pubyear": pubyear}

    # Add the book data to the catalog using title as key
    book_catalog[title] = book
    print(book_catalog)
    write_book_catalog(book_catalog)

def delete_book(book_catalog):
    title = input("Title: ")
    if title in book_catalog:
        del book_catalog[title]
        print(title + " removed from catalog.")
    else:
        print(title + " doesn't exist in the catalog.")

def display_menu():
    print("The Book Catalog program")
    print()
    print("COMMAND MENU")
    print("show - Show book info")
    print('list - List books')
    print("add -  Add book")
    print("edit - Edit book")
    print("del -  Delete book")
    print("exit - Exit program")

def main():
    display_menu()
    book_catalog = read_book_catalog()
    while True:
        print()
        command = input("Command: ").lower()
        if command == "show":
            show_book(book_catalog)
        elif command == 'list':
            list_book(book_catalog)
        elif command == "add":
            add_edit_book(book_catalog, mode="add")
        elif command == "edit":
            add_edit_book(book_catalog, mode="edit")
        elif command == "del":
            delete_book(book_catalog)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()


'dot' of an object is always convenient than 'bracket[]' of a dict to call data during typing.
I have MylibraryDir as class to store the directory of books:

    import os
    class MylibraryDir():
        python = '~/mylibrary/python'
        javacript = '~/mylibrary/javacript'
    So I can jump around through`os.chdir(MylibraryDir.python)

Now I need to analyze the data in a dict.I tried to convert them to.

    >>> dict(vars(Mylibrary))
    {'__module__': '__main__', 'html': '/Users/gaowei/Documents/myLibrary/1.2.Computing/HTML', '__dict__': <attribute '__dict__' of 'Mylibrary' objects>, '__weakref__': <attribute '__weakref__' of 'Mylibrary' objects>, '__doc__': None, 'base': '/Users/gaowei/Documents/myLibrary', 'language': '/Users/gaowei/Documents/myLibrary/2.Social-Science/Language', 'psychology': '/Users/gaowei/Documents/myLibrary/2.Social-Science/Psychology'}

Filter the qualified:

    mydict = dict(vars(Mylibrary))
[mydict for key in mydict if '__' in key del mydict[key]]

def class_to_dict(cls):
    dict = dict(vars(Mylibrary))
    for key in dict:
        if '__' not in key:
            del dict[key]
    return dict




function `getattr()`
def main():
    class_to_dict(Mylibrary)
