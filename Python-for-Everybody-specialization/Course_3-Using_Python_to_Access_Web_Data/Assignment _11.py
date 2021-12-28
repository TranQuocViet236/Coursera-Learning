'''
In this assignment you will read through and parse a file with text and numbers.
You will extract all the numbers in the file and compute the sum of the numbers.
Data Files
We provide two files for this assignment. One is a sample file where we give you
the sum for your testing and the other is the actual data you need to process for
the assignment. ('sample data.txt' - There are 90 values with a sum=445833
and 'actual data.txt' - There are 103 values and the sum ends with 604)

Handling The Data
The basic outline of this problem is to read the file, look for integers using the
re.findall(), looking for a regular expression of '[0-9]+' and then converting the
extracted strings to integers and summing up the integers.
'''

import re

name = input("Enter file name: ")
if(len(name) < 1): name = 'actual data.txt'
fh = open(name)

new_list = list()

for line in fh:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        new_list.append(int(number))

print(sum(new_list))
