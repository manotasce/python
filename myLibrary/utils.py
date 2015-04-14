__author__ = 'Czar'
# import libraries
import csv
import sys

# Setup variables
fileName = "Data/BookData.csv"
READ = 'r'
WRITE = 'w'
APPEND = 'a'

# Unicode Characters
UTF8 = "UTF-8"

# Insert new Book detail
def insertBook(ISBN,name,author,category,editorial,pubYear):

    try :
        # open BookData CSV File
        bookData = open(fileName, mode=APPEND,buffering=-1,encoding=UTF8, newline='\n')

        # Save Book Entry
        bookData.write(ISBN + ',' + name + ',' + author + ',' + category + ','
                   + editorial + ',' + pubYear+'\n')

        print('Book '+name+' details was saved!' )

        # Close file
        bookData.close()

    except :
        print('There is some issues on insertBook, Details' +sys.exc_info()[0])


# Count existing book details
# 4/13/2015
def countBookByIsbn(ISBN):
    """

    :type ISBN: object
    """
    isbn=[]
    try:
        with open(fileName) as bookData:
            dataFile=csv.reader(bookData)

            for row in dataFile:
                isbn.append(row[0])

        return isbn.count(ISBN)

    except:
        print('There is some issues on insertBook, Details' + sys.exc_info()[0])


