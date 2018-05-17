#! python3

import re, pyperclip

#TODO: Create regex for Phonenumbers
phoneRegex = re.compile(r'''
#415-555-4565, 555-4040,(344) 333-4343, 555-2323 ext 12123,ext. 1212,x1212
(
((\d\d\d)|(\(\d\d\d\)))?       #area code
(\s|-)        #first seperator
\d\d\d        #first 3 digits
-        #Seperator
\d\d\d\d        #last 4 digits
(((ext(\.)?\s)|x) (\d{2,5}))?        #extension (optional)
)
''',re.VERBOSE)

#TODO: Create regex for Email
emailRegex = re.compile(r'''
#anuthi_@something.com

[a-zA-Z0-9_.+]+      #name
@        #symbol
[a-zA-Z0-9_.+]+       #domain

''',re.VERBOSE)

#TODO Get the text off of the clipboard
text = pyperclip.paste()

#TODO Extract the Email/PhoneNO from text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for number in extractedPhone:
    allPhoneNumbers.append(number[0])


#TODO Copy extracted Email and PhoneNo to clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)