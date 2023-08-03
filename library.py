# importing modules
import sqlite3
import time
from prettytable import PrettyTable

class Book():
    def __init__(self,name,author,publisher,category,edition,page):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.category = category
        self.edition = edition
        self.page = page

    def __str__(self):

        return "Name: {}\nAuthor: {}\nPublisher:{}\nCategory: {}\nEdition: {}\nPage: {}".format(self.name,self.author,self.publisher,self.category,self.edition,self.page)


# creating library class
class Library():
    def __init__(self):

        self.creating_connection()
     
    # connecting the table
    def creating_connection(self):
        self.con = sqlite3.connect("lib.db")

        # to operate on database, creating self.cursor
        self.cursor = self.con.cursor()
    
        self.cursor.execute("CREATE TABLE IF NOT EXISTS bookcase (Name TEXT, Author TEXT, Publisher TEXT, Category TEXT, Edition INT, Page INT)")
        
        # commiting is needed the query to be valid on the database 
        self.con.commit()
        
           
    def disconnecting(self):
        self.con.close()


    def show_library(self):
        # getting all 
        self.cursor.execute("SELECT * FROM bookcase")                   
        # to get information from db, use fetchall function
        data = self.cursor.fetchall()

        if len(data) == 0:
            print("No books here..")
        else:
            for i in data:
                book = Book(i[0],i[1],i[2],i[3],i[4],i[5])
                print(book)
                print("***********************************")
    
    def questioning_book(self,name):
        self.cursor.execute("SELECT * FROM bookcase WHERE name = ?",(name,))
        data2 = self.cursor.fetchall()

        if len(data2) == 0:
            print("There is no such book.")
        else:
            book2 = Book(data2[0][0],data2[0][1],data2[0][2],data2[0][3],data2[0][4],data2[0][5])
            print(book2)

    def adding_book(self,book3):
        query = "INSERT INTO bookcase VALUES(?,?,?,?,?,?)"
        self.cursor.execute(query,(book3.name,book3.author,book3.publisher,book3.category,book3.edition,book3.page))
        self.con.commit()

    def deleting(self,name):
        
        #  Before deleting, check the book existance
        query = "SELECT * FROM bookcase WHERE name=?"

        self.cursor.execute(query,(name,))
        data5 = self.cursor.fetchall()

        if len(data5)==0:
            print("There is no such book.")
        else:
            query2 = "DELETE FROM bookcase WHERE name = ?"
            self.cursor.execute(query2,(name,))
            self.con.commit()
            print("The book has been deleted.")

    def sum_page(self):
        query = "SELECT SUM(Page) FROM bookcase "
        self.cursor.execute(query)

        # The fetchone() function returns the result as a tuple. 
        # The first element (index 0) of this tuple represents the total number of pages in the query result.
        total_pages = self.cursor.fetchone()[0]

        print("Total pages are {}".format(total_pages))


    def update_edition(self,name):
        query = "SELECT * FROM bookcase WHERE name = ?"
        self.cursor.execute(query,(name,))

        data4 = self.cursor.fetchall()

        if len(data4) == 0:
            print("The book to be updated could not be found.")
        else:

            new_edt = int(input("Current edition:"))

            self.cursor.execute("UPDATE bookcase SET edition = ? WHERE name = ?",(new_edt,name))
            self.con.commit()

            print("The edition of {} has been updated.".format(name))

            # We re-queried the book's information to show the updated edition.
            self.cursor.execute("SELECT * FROM bookcase WHERE name = ?",(name,))
            data5= self.cursor.fetchall()
            book4 = Book(data5[0][0],data5[0][1],data5[0][2],data5[0][3],data5[0][4],data5[0][5])
            print(book4)

    def how_many_books(self):
        q = "SELECT COUNT(*) FROM bookcase"
        self.cursor.execute(q)
        d = self.cursor.fetchone()[0]

        print("There are {} books in the bookcase.".format(d))

    def grouping(self):
        qu = "SELECT category, GROUP_CONCAT(name) FROM bookcase GROUP BY category"
        self.cursor.execute(qu)
        data__ = self.cursor.fetchall()

        table = PrettyTable()
        table.field_names = ["Category","Name"]


        for category,books in data__:
            table.add_row([category, books])
        print(table)

    