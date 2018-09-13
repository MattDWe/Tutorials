"""
EmailCompControl.py
Program is to take instructions from email and tell the computer to complete that task.
Different options will be provided to choose from.
Github: MattDWe
"""

import time, imapclient, pyzmail, subprocess

instructions = {"calculator\r\n": "C:\\Windows\\System32\\calc.exe"}

imapObj = imapclient.IMAPClient("imap.gmail.com", ssl=True)
imapObj.login("matttestemail123@gmail.com", "ERADICATED")
    
while True:
    #for i in range(1, 31):    #Check Email every 30seconds
        #time.sleep(1)
        #print(i)
    time.sleep(5)
    #Check email for new messages
    imapObj.select_folder("INBOX", readonly=False)
    UIDs = imapObj.search(["FROM matttestemail123@gmail.com"])
    print(str(len(UIDs)) + " Emails found.")
    if len(UIDs) == 0:
        continue
    #Search through emails
    for email in UIDs:
        rawMessages = imapObj.fetch([email], ["BODY[]", "FLAGS"])
        message = pyzmail.PyzMessage.factory(rawMessages[email][b"BODY[]"])
        subject = message.get_subject()
        if subject != "password":
            continue
        message = message.text_part.get_payload().decode(message.text_part.charset)
        imapObj.delete_messages(email)
        print(message[0:len(message) - 4])
    #Follow instructions
    subprocess.Popen(instructions[message])
