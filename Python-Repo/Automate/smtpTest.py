import smtplib, logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def sendMail():
    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com',587)
        temp = smtpObj.ehlo()
        logging.debug("Starting tls")
        smtpObj.starttls()
        #read pass from file
        passFile = open(r'G:\Pycode\Automate\API\SMTPpassword.txt','r')
        SMTPuser = passFile.read().split()
        #STMPuser = ['username','password']
        logging.debug("Logging in...")
        smtpObj.login(SMTPuser[0],SMTPuser[1])
        logging.debug("Sending Mail...")
        smtpObj.sendmail('senderEmail@gmail.com','recieverEmail@gmail.com',
                         'Subject: I am awesome\n\nDear Bot,\nI am awesome and i wanted to tell you that')
        logging.debug("Mail Sent!")
        smtpObj.quit()
    except Exception as ex:
        print("There was an error : ",ex)

if __name__ == '__main__':
    sendMail()