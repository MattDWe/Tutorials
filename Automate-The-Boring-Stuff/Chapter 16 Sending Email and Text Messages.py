"""
Automate The Boring Stuff Chapter 16
Sending Email And Text Messages
Github: MattDWe
"""

#Sending Email
#SMTP Simple Mail Transfer Protocol
"""
Process of sending an email in Python
import smtplib
smtpObj = smtplib.SMTP("domain name", port)                     #Connects to SMTP Server
smtpObj.ehlo()                                                  #Pings the SMTP server
smtpObj.starttls()                                              #Starts TLS Encryption
smtpObj.login("your email", "SECRET_PASSWORD")                  #Login into email
smtpObj.sendmail("your email", "their email", "Your message")   #Sends Mail
smtpObj.quit()                                                  #Disconnects from SMTP Server
"""

"""
Connecting to an SMTP Server
Provider                  SMTP Server domain name
gmail                     smtp.gmail.com
outlook.com/hotmail.com   smtp-mail.outlook.com
Yahoo Mail                smtp.mail.yahoo.com
AT&T                      smpt.mail.att.net(port 465)
Comcast                   smtp.comcast.net
Verizon                   smtp.verizon.net(port 465)
"""

#Recieving Email/Deleting Emails
#IMAP Internet message Access Protocol
"""
Process of Retrieving Email
import imapclient
imapObj = imapclient.IMAPClient("domain name", ssl=True)                    #Connects to IMAP server
imapObj.login("your email", "password")                                     #Login into Email
imapObj.select_folder("INBOX", readonly=True)                               #Select Folder
UIDs = imapObj.search(["KEY"])                                              #Search for emails/Check Book for different keys
print(UIDs)
rawMessages = imapObj.fetch([ID from UIDs], ["BODY[]", "FLAGS"])            #Fetch email and mark as read
import pyzmail
message = pyzmail.PyzMessage.factory(rawMessages[ID from UIDs]["BODY[]"])   #Fetching Raw message
print(message.get_subject())                                                #Subject
print(message.get_addresses("from"))                                        #Email recieved from
print(message.get_addresses("to"))                                          #Email sent to
print(message.get_addresses('cc'))                                          #Email CC
print(message.get_addresses('bcc'))                                         #Email BCC
print(message.text_part != None)                                            
print(message.text_part.get_payload().decode(message.text_part.charset))    #Text portion of email
print(message.html_part != None)
print("message.html_part.get_payload().decode(message.html_part.charset))   #Text from HTML portion
imapObj.logout()                                                            #Disconnects from IMAP server
"""

"""
Connecting to IMAP Server
Gmail                     imap.gmail.com
Outlook.com/Hotmail.com   imap-mail.outlook.com
Yahoo Mail                imap.mail.yahoo.com
AT&T                      imap.mail.att.net
Comcast                   imap.comcast.net
Verizon                   incoming.verizon.net
"""

#Sending Text Messages
#Requires setting up a Twilio account
"""
Process of sending text
from twilio.rest import TwilioRestClient
accountSID = " "
authToken = " "
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = "+phone"
myCellPhone = "+phone"
message = twilioCli.messages.create(body="Message", from_=myTwilioNumber, to=MyCellPhone)
"""

"""
Practice Questions
1. SMTP and IMAP
2. smtplib.SMTP(), smtpObj.ehlo(), smptObj.starttls(), and smtpObj.login()
3. imapclient.IMAPClient() and imapObj.login()
4.List of strings of IMAP keywords in the book
5. set the max variable to larger imaplib._MAXLINE = 1000000
6. pyzmail
7. Need Twilio account SID number, the auth token, and Twilio phone number
"""
