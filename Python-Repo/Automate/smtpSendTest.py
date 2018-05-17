import imapclient, pprint, pyzmail, logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

#if importing too many messages
# import imaplib
# imaplib._MAXLINE = 100000

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
passFile = open(r'G:\Pycode\Automate\API\SMTPpassword.txt','r')
SMTPuser = passFile.read().split()
# imapObj.login(username,password)
print(imapObj.login(SMTPuser[0],SMTPuser[1]))
print("Printing latest mail for user : ",SMTPuser[0])
# pprint.pprint(imapObj.list_folders())
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search('All')
rawMessage = imapObj.fetch(UIDs[-1],['BODY[]', 'FLAGS'])

message = pyzmail.PyzMessage.factory(rawMessage[UIDs[-1]][b'BODY[]'])
print("TO : ", message.get_address('to'))
print("FROM : ", message.get_address('from'))
print("SUBJECT : ", message.get_subject())
print("FLAGS : ", rawMessage[UIDs[-1]][b'FLAGS'])
if message.text_part:
    print("BODY : ")
    pprint.pprint(message.text_part.get_payload().decode((message.text_part.charset)))

if message.text_part:
    print("BODY(HTML) : ")
    pprint.pprint(message.html_part.get_payload().decode((message.html_part.charset)))

#Subject of all emails
for x in UIDs:
    rawMessage = imapObj.fetch(x, ['BODY[]'])
    message = pyzmail.PyzMessage.factory(rawMessage[x][b'BODY[]'])
    print("Message ID : ",x)
    print("FROM : ", message.get_address('from'))
    print("SUBJECT : ", message.get_subject())
    print('')
imapObj.logout()

'''
DELETING MESSAGE

>>> imapObj.select_folder('INBOX', readonly=False)
>>> imapObj.delete_messages(4)
{4: (b'\\Seen', b'\\Deleted')}
>>> imapObj.expunge()
(b'Success', [])
>>> imapObj.logout()
b'LOGOUT Requested'
'''