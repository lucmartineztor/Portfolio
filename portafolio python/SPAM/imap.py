import imaplib, email, os
import time
import datetime as dt
from os import path
from datetime import timezone
from bs4 import BeautifulSoup
import pickle
from dominio import dominio1,correo
import retrain_text
from retrain_text  import sending_data

user= correo
password="sI2wU0iB7wG2"
imap_url="imap.mi.com.co"
# sets up the auth
def auth(user,password,imap_url):
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user,password)
    return con

# extracts the body from the email
def get_body(msg):
    if msg.is_multipart():
        cleantext=get_body(msg.get_payload(0))
        cleantext=BeautifulSoup(cleantext,'html5lib').text
        #cleantext=BeautifulSoup(cleantext,'xlmx').text
        pickle.dump(cleantext,open("cleantext"+dominio1,"wb"))
        return cleantext
    else:
        cleantext=msg.get_payload(None,True)
        cleantext=BeautifulSoup(cleantext,'html5lib').text
        #cleantext=BeautifulSoup(cleantext,'xlmx').text
        pickle.dump(cleantext,open("cleantext"+dominio1,"wb"))
        return cleantext

# allows you to download attachments
con = auth(user,password,imap_url)
con.select('INBOX.Junk')
print(con.select('INBOX.Junk'))

i=3
result, data = con.fetch(str(i),'(RFC822)')
raw = email.message_from_bytes(data[0][1])
print(get_body(raw))

con = auth(user,password,imap_url)
con.select('INBOX.Junk')




 
