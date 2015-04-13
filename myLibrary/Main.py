__author__ = 'Czar'
# import libraries
import csv

# Setup variables
fileName = "Data/BookData.csv"
READ = 'r'
WRITE = 'w'
APPEND = 'a'
# Unicode Characters
UTF8 = "UTF-8"

# Prompt for Book Details
ISBN = input('Book ISBN ')
name = input('Book Name ')
author = input('Author (Separate by | for more than one) ')
category = input('Category ')
editorial = input('Editorial ')
pubYear = input('Publishing Year ')

# open BookData CSV File
bookData = open(fileName, mode=APPEND,buffering=-1,encoding=UTF8, newline='\n')

# Save Book Entry
bookData.write(ISBN + ',' + name + ',' + author + ',' + category + ','
               + editorial + ',' + pubYear+'\n')


print('Book '+name+' details was saved!' )

bookData.close()