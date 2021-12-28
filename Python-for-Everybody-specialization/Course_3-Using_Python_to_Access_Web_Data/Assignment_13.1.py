#Actual data: http://py4e-data.dr-chuck.net/comments_1361457.xml
#Parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
#Data format and approach:
'''<comment>
  <name>Matthias</name>
  <count>97</count>
</comment>
'''
#To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named 'count' with the following line of code:
#counts = tree.findall('.//count')

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url  = input("Enter url: ")
print("1_Retrieving ", url, type(url))
url_op = urllib.request.urlopen(url)
print("2_url_op", url_op, type(url_op))
data = url_op.read()
print("3_url.read() or data", data, type(data))
data = data.decode()
print("4_data decode", data, type(data))
tree = ET.fromstring(data)
print("5_tree", tree, type(tree))
count = tree.findall('.//count')
print("6_count", count, type(count), "len", len(count))

i = 0
i = int(i)
sumum= list()

while True:
    try:
        count_text = int(count[i].text)
        sumum.append(count_text)
        print("7_count", count_text, type(count_text))
        i += 1
        continue
    except:
        break
print("sumum", sum(sumum), type(sumum))