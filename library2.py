from library import*
print("""
      BOOKCASE

      Choose the operation you want:

      1) Show the books

      2) Question book

      3) Add book

      4) Delete book

      5) Sum Page

      6) Updating Edition

      7) How Much Books

      8) Grouping

      To exit, please press "q"

""")

lib = Library()

while True:
    opr = input("Choose the operation:")

    if opr == "q":
        break

    elif opr == "1":
        
        print("Loading....")
        time.sleep(1)
        lib.show_library()

    elif opr == "2":
        book_name = input("Which book do you question:")
        
        print("Questioning...")
        time.sleep(2)
        lib.questioning_book(book_name)

    elif opr == "3":
        name = input("Name:")
        author = input("Author:")
        publisher = input("Publisher:")
        category = input("Category:")
        edition = input("Edition:")
        page = input("Page:")

        new_book = Book(name,author,publisher,category,edition,page)

        print("Adding book...")
        time.sleep(1.5)

        lib.adding_book(new_book)

        print("The book has been added.")

    elif opr == "4":
        s = input("Which book do you delete?:")
        
        print("Deleting...")
        time.sleep(0.5)
        lib.deleting(s)
    
    elif opr == "5":
        time.sleep(0.5)

        lib.sum_page()

    elif opr == "6":
        x = input("Which book do you want to update?:")
        lib.update_edition(x)
        
    elif opr == "7":
        print("Counting...")
        time.sleep(0.5)
        lib.how_many_books()

    elif opr == "8":
        lib.grouping()




        

