#!/usr/bin/python3
import re


# string = ['21.22.95.38 - [2024-03-31 18:06:50.048925] "GET /projects/260 HTTP/1.1" 405 521',
string = '174.56.28.201 - [2024-03-31 20:04:34.840945] "GET /projects/260 HTTP/1.1" 200 479'

pattern = r'(.*?)\s-\s\[(.*?)\]\s"(.*?)"\s(\d{3})\s(.*?)\Z'


results = re.match(pattern, string)


print(len(results.groups()))


print(results.group(0))
print(results.group(1))
print(results.group(2))
print(results.group(3))
print(results.group(4))
print(results.group(5))