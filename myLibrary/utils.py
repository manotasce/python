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