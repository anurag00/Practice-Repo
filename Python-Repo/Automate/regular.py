import re

message = 'Call me 415-333-1929 tomorrow or call my office at 565-777-6454'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
""" mo = phoneNumRegex.search(message)     # for finding first occurences
print(mo)
print(mo.group()) """
print(phoneNumRegex.findall(message))