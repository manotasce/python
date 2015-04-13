__author__ = 'Czar'
# Import modules
import utils



def main():
    insert='y'
    key='s'


    while key.lower() != "q" :
        print(printMenu())

        key = input('Press correct letter for an option or press q to exit.')

        if key.lower()=="i" :

            while  insert != 'n':
                promptAndSaveBookDetails()
                insert = input('Do you want to add other book detail? (y / n) ').lower()
    return


# Insert a new Book Details
def promptAndSaveBookDetails():

    # Prompt for Book Details
    ISBN = input('Book ISBN ')
    name = input('Book Name ')
    author = input('Author (Separate by | for more than one) ')
    category = input('Category ')
    editorial = input('Editorial ')
    pubYear = input('Publishing Year ')
    utils.insertBook(ISBN,name,author,category,editorial,pubYear)
    return

# On screen Menu
def printMenu():
    outPut = "Welcome to Czar's Library\n"
    outPut += "Select one option below:\n"
    outPut += "**Insert a Book detail - Press the i key\n"
    outPut +="**Update a Book detail - Press the u key\n"
    return outPut


main()