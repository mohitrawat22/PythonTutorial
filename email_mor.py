import smtplib
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
#print(smtp_object.ehlo())

#print(smtp_object.starttls())

#import getpass
#email = getpass.getpass('Enter email: ')
#password = getpass.getpass('Enter password: ')
#print(password)

email = 'mohitrawat22@gmail.com'
#print(smtp_object.login(email, 'sbxuqehdhvpkrnyd'))

subject = 'Python email subject 1'
message = 'Python email message 1'

msg = 'Subject: '+subject+'\n'+message
from_email = email
to_email = email
#smtp_object.sendmail(from_email, to_email, msg)


# receiving emails

import imaplib

m = imaplib.IMAP4_SSL('imap.gmail.com')
m.login(email, 'sbxuqehdhvpkrnyd')
#print(m.list())

print(m.select('inbox'))

item, data = m.search(None, 'SUBJECT "Python email subject 1"')
email_id = data[0]
result, email_data = m.fetch(email_id, '(RFC822)')
print(email_data)
print(email_data[0])
raw_email = email_data[0][1]

raw_email = raw_email.decode('utf-8')
print()

import email
email_string = email.message_from_string(raw_email)
print('below is raw_email: \n')
print(email_string)

print(email_string['Date'],'\n')

for part in email_string.walk():
    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)
        print(body)


