'''
The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract
the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and
the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1361458.json (Sum ends with 9)

'''
import urllib.request as ur
import json

json_url = input("Enter url: ")
print("Retrieving ", json_url)
data = ur.urlopen(json_url).read().decode('utf-8')
print(f'Retrieved {len(data)} characters')
json_obj = json.loads(data)

counts = 0
total_comments = 0

for comment in json_obj["comments"]:
    counts += int(comment["count"])
    total_comments += 1

print('Count:', total_comments)
print('Sum:', counts)