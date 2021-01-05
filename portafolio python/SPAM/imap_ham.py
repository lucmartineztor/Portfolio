import imaplib, email, os
import time
import datetime as dt
from os import path
from datetime import timezone
from bs4 import BeautifulSoup
import pickle
from dominio import dominio1,correo
import retrain_text_ham
from retrain_text_ham  import sending_data

user=correo
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
        #cleantext=BeautifulSoup(cleantext,'lxml').text
        pickle.dump(cleantext,open("cleantextHam"+dominio1,"wb"))
        return cleantext
    else:
        cleantext=msg.get_payload(None,True)
        cleantext=BeautifulSoup(cleantext,'html5lib').text
        pickle.dump(cleantext,open("cleantextHam"+dominio1,"wb"))
        #cleantext=BeautifulSoup(cleantext,'xlmx').text
        texto="texto de prueba"
        Status="texto de prueba"
        sending_data(texto,Status) 
        return cleantext

        


# allows you to download attachments
def single():
    con = auth(user,password,imap_url)
    con.select('INBOX')
    print(con.select('INBOX')) 

    i=3
    result, data = con.fetch(str(i),'(RFC822)')
    raw = email.message_from_bytes(data[0][1])
    print(get_body(raw))

    con = auth(user,password,imap_url)
    con.select('INBOX')
 
#Para realizar multiples veces el proceso
""" i=1
while i<5:
    result, data = con.fetch(str(i),'(RFC822)')
    raw = email.message_from_bytes(data[0][1])
    print(get_body(raw))
    i=i+1 """
    
def multiple():
    con = auth(user,password,imap_url)
    con.select('INBOX')
    print(con.select('INBOX'))
    number=str(con.select('INBOX')[1]).replace("b","").replace("'","").replace("[","").replace("]","")
    numbers=int(number)
    
    i=1
    while i<=numbers:
        result, data = con.fetch(str(i),'(RFC822)')
        raw = email.message_from_bytes(data[0][1])
        get_body(raw)
        i=i+1
        print(i)
        
    """ i=1 
    while i<5:
        result, data = con.fetch(str(i),'(RFC822)')
        raw = email.message_from_bytes(data[0][1])
        get_body(raw)
        i=i+1 """
        
print(multiple())