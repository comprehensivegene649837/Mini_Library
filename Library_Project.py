class Library:
    def __init__(self, listofbooks):
        self.books = listofbooks
    
    def booksInfo(self):
       print ("List of the books available: " )
       for books in self.books:
        print(books)
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print("You have been issued: " , bookName)
            self.books.remove(bookName)
            return True

        else:
            print("sorry, the book is not available")
            return False
    
    def returnBook(self, bookName):
        self.books.append(bookName)
        print(f"thank you! for returning {bookName} ")

    
            

class Student:
    def reqBook(self):
        
        self.book = input("Enter the name of the book that you wish to buy: ")
        return self.book
    
    def returnBook(self):
        self.book = input("Enter the name of the book that you want to return: ")
        return self.book
#
        

    

        
if __name__ == "__main__":
    lib = Library(["Python crash course" ,  "advanced python" , "Python Modules"])
    

    student= Student()
    

    while True:
        print('''*****WELCOME TO THE LIBRARY****
        Press 1 to list the available books.
        Press 2 to borrow a book
        Press 3 to add/return a book
        Press 4 to exit the library''')
        try:
            choice = int(input("enter your choice: "))
        except Exception as e:
                print("error: ", e)
                continue
        if choice == 1:
           
            lib.booksInfo() 
           
        elif choice == 2:
            
            lib.borrowBook(student.reqBook())                    #student.reqbook() 
        
        elif choice == 3:
            
            lib.returnBook(student.returnBook())                                                    #student.returnbook()

        elif choice == 4:
           print("Thank you for using the library!") 
           break
        
        else:
            print("INVALID INPUT")
        

            





