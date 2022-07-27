
import subprocess
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from sqlalchemy import create_engine
import _mssql
import pandas as pd
import pyodbc as pyodbc
from cryptography.fernet import Fernet
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import formatdate
from email import encoders
from pathlib import Path
import logging
import win32com.client as win32
from zipfile import ZipFile
from PIL import Image
import time
import datetime
import urllib
import sys
import shutil
import smtplib
import ssl
import os
import traceback
import json
COMMASPACE = ', '
__file__ = os.path.abspath(__file__)
path = os.path.dirname(__file__)
from cryptography.fernet import Fernet
BASE_DIR = os.path.split(path)[0]
import clr
clr.AddReference(path+r"\BaseAc.dll")
from CBaseAc import BaseAC
BAC=BaseAC()
DEBUG = True
import pyotp
import paramiko


# ====================================================================================================================================
# Gmain class
            
# ====================================================================================================================================
# login app  
def app_login(
            app,
            request_token,
            credentials_services=[],
            **kwargs
            ):
    """retrieve  emails send /cc list from SQL 
    **kwargs:           
        server(str): servername
        credentials_service
        usernamefield_id
        passwordfield_id
        usernamefield_xpath
        passwordfield_xpath
        usernamefield_name
        passwordfield_name
        two_factor_code_field_xpath
    """

    if not isinstance(credentials_services,list):
        return("if you send credentials_services info this must be a list like object")

    
    def __get_start_app_service(service):
        try:
            header = {'Authorization':"Token "+request_token}
            #response = requests.get('https://workforcens.teleperformance.co:5051/api/cred_auth/',headers=header)
            response = requests.get('https://tarsweb.teleperformance.co/api/cred_auth/',headers=header)
            if response.status_code == 200:
                results = json.loads(response.content)['results']
                if len(results) > 0:
                    for result in results:
                        if result['service'] == service:
                            cusername = BAC.Decode(result['username'])
                            cpassword = BAC.Decode(result['password'])
                            # key = bytes(result['key'],'utf-8')
                            # my_fernet = Fernet(key)
                            # cusername = result['username']
                            # cpassword = bytes(result['password'], 'utf-8')
                            # password = my_fernet.decrypt(cpassword)
                            # cpassword = password.decode('utf-8')
                            return cusername, cpassword
                    return "this service is not included in your authorization services"
                else:
                    return "theres no results from TARS rest API call, your authorization possibily has been expired"
            else:
                return"theres a problem with the api call: "+str(response.content) +" please verify"
        except Exception:
            traceback.print_exc()
    try:
        if len(credentials_services) == 0:
            return print("\nTARS ERROR, \ncredentials services has not been included\n")
        else:
            username = ''
            password = ''
            client_id = ''
            client_secret = ''
            token = ''
            auth_code = ''
            twofactor_code = ''
            tenant_id = ''
            if app.__class__.__name__ == 'str':
                app_name = app
            elif app.__class__.__name__ == 'module':
                app_name = app.__name__
            elif app.__class__.__name__ == 'type':
                name = app.__bases__[0].__name__
                if name == 'object':
                    app_name = app.__name__
                else:
                    app_name = app.__bases__[0].__name__
            else:
                app_name = app.__class__.__name__
            for service in credentials_services:
                try:
                    print(service)
                    username, password = __get_start_app_service(service)
                except Exception as e:
                    return print(__get_start_app_service(service))
                if 'clientid' in service.lower() or 'client_id' in service.lower():
                    client_id = password
                elif 'clientsecret' in service.lower() or 'client_secret' in service.lower():
                    client_secret = password
                elif 'authcode' in service or 'auth_code' in service.lower():
                    auth_code = password
                elif 'twofactor' in service.lower() or 'two_factor' in service.lower():
                    twofactor_code = password
                elif 'token' in service.lower() or 'token_' in service.lower():    
                    token = password
                elif 'tenantid' in service.lower() or 'tenant_id' in service.lower():    
                    tenant_id = password
            if app_name == 'Domo':
                from pydomo import Domo
                api_host = 'api.domo.com'
                instance = app(client_id, client_secret, logger_name='foo', log_level=logging.INFO, api_host=api_host)
            elif app_name =='SkypeObj':
                instance = app(username, password, tokenFile=kwargs['tokenfile'])
            elif app_name == 'Webex':
                tokenfile = kwargs['tokenfile']
                redirect_uri = 'https://webexapis.com/auth'
                instance = app(client_id=client_id,client_secret=client_secret,tokenfile=tokenfile,auth_code=auth_code,redirect_uri=redirect_uri)
            elif app_name == 'Zoom':
                tokenfile = kwargs['tokenfile']
                redirect_uri = 'https://api.zoom.us/v2'
                instance = app(client_id=client_id,client_secret=client_secret,token_file=tokenfile,
                            auth_code=auth_code,redirect_uri=redirect_uri)
            elif app_name == 'MSGraph':
                tokenfile = kwargs['tokenfile']
                redirect_url =  kwargs['redirect_url']
                scopes = kwargs['scopes']
                instance = app(client_id=client_id,client_secret=client_secret,tokens_file=tokenfile,
                            tenant_id=tenant_id,redirect_url=redirect_url,scopes=scopes)
            elif app_name == 'Slack':
                if kwargs['service'] == 'Hashtags':
                    method ='https://slack.com/api/conversations.history?token='
                    instance = requests.get(method+token+'&channel='+str(kwargs['channel'])+'&pretty=1&limit=100')
            elif app_name == 'SMTP':
                app.login(username, password)
                instance = 'smtp app log in succesfully'
            elif app_name =='tableauserverclient':
                site_name =kwargs['site_name']
                instance = app.TableauAuth(username, password, site_name)
            elif app_name == 'spExec':
                server = kwargs['server']
                instance = _mssql.connect(server=server, user=username,
                                password=password, appname="TARSspExec")
            elif app_name == 'send_df_to_sql':
                database = kwargs['database']
                server = kwargs['server']
                instance = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};"
                                        "SERVER="+server+";"
                                        "DATABASE="+database+";"
                                        "UID="+username+";"
                                        "PWD="+password+";"
                                        "appname=TARSdfToSQL")
            elif app_name == 'execute_SQLquery':
                server = kwargs['server']
                instance = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+
                                    ';UID='+username+';PWD='+password+';appname=TARSexecute_SQLquery')
            elif app_name == 'pyodbc':
                server = kwargs['server']
                instance = app.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';UID='+username+';PWD='+ password)
            elif app_name == 'WebDriver':
                if 'usernamefield_id' in kwargs:
                    app.find_element(By.ID,kwargs['usernamefield_id']).send_keys(username)
                    time.sleep(1)
                if 'passwordfield_id' in kwargs:
                    app.find_element(By.ID,kwargs['passwordfield_id']).send_keys(password)
                    time.sleep(1)
                if 'usernamefield_xpath' in kwargs:
                    app.find_element(By.XPATH,kwargs['usernamefield_xpath']).send_keys(username)
                    time.sleep(1)
                if 'passwordfield_xpath' in kwargs:
                    app.find_element(By.XPATH,kwargs['passwordfield_xpath']).send_keys(password)
                    time.sleep(1)
                if 'usernamefield_name' in kwargs:
                    app.find_element(By.NAME,kwargs['usernamefield_name']).send_keys(username)
                    time.sleep(1)
                if 'passwordfield_name' in kwargs:
                    app.find_element(By.NAME,kwargs['passwordfield_name']).send_keys(password)
                    time.sleep(1)
                if 'two_factor_code_field_xpath' in kwargs:
                    codeinput = app.find_element(By.XPATH, kwargs['two_factor_code_field_xpath'])
                    totp = pyotp.TOTP(twofactor_code) 
                    code = totp.now()
                    codeinput.send_keys(code)
                    time.sleep(1)
                if 'two_factor_code_field_name' in kwargs:
                    codeinput = app.find_element(By.NAME, kwargs['two_factor_code_field_name'])
                    totp = pyotp.TOTP(twofactor_code) 
                    code = totp.now()
                    codeinput.send_keys(code)
                    time.sleep(1)
                instance = 'selenium login'
            elif app_name == 'remote_script_connect':
                ssh = paramiko.SSHClient()
                server = kwargs['server'] #'TPCCP-DB128.teleperformance.co'
                print("connection to remote server: "+server)
                logging.info("connection to remote server: "+server)
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(server, username=username, password=password)
                instance = ssh
            elif app_name == 'sftp':
                ssh = paramiko.SSHClient()
                hostname = kwargs['hostname'] #'TPCCP-DB128.teleperformance.co'
                key_filename = kwargs['key_filename'] 
                port = kwargs['port'] 
                sshcon   = paramiko.SSHClient()  # will create the object
                sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # no known_hosts error
                sshcon.connect(hostname, port=port, username=username, password=password, key_filename=key_filename)
                instance = sshcon
            else:
                return "error, this app is not in the app login service"
            return instance
    except Exception as e:
        print(e)
        logging.exception("\nError in login process: \n")
            

# ====================================================================================================================================
# Configurators  

# ====================================================================================================================================
# Get Emails

# ============================================================================================================
# Send Email
def send_mail(send_to, cc_to, subject, message,market=1, files=[], use_tls=True, imgfiles=[],include_ribbon=False):
    """Compose and send email with provided info and attachments.

    Args:
        send_to (list[str]): to name(s)
        cc_to (list[str]): cc to name(s)
        subject (str): message title
        message (str): message body
        files (list[str]): list of file paths to be attached to email
        username (str): server auth username
        password (str): server auth password
        use_tls (bool): use TLS mode
        imgfiles(list[str]): list of attached img files (always return image name as "image(n)")
    """
    #preparing sento ccto 
    temp_to = []
    for x in send_to:
        if '@gmail' in x or '@outlook' in x or '@hotmail' in x or '@yahoo' in x or x == '':
            print('skiping account, '+x+' this domain isnt authorized')
        else:
            temp_to.append(x)
    send_to = temp_to
    temp_cc = []
    for x in cc_to:
        if '@gmail' in x or '@outlook' in x or '@hotmail' in x or '@yahoo' in x or x == '':
            print('skiping account, '+x+' this domain isnt authorized')
        else:
            temp_cc.append(x)
    cc_to = temp_cc
    markets = read_SQL_table(server='TPCCP-DB128\\SQL2016STD',database='PRE_TARSWeb',tablename='tbMarkets')
    accounts = read_SQL_table(server='TPCCP-DB128\\SQL2016STD',database='PRE_TARSWeb',tablename='tbServiceAccounts')
    account = accounts[accounts['id']==int(markets[markets['id']==market]['service_account_id'])]
    send_as = account['email_address'].tolist()[0]
    service = account['service'].tolist()[0]
    context = ssl.create_default_context()
    msg = MIMEMultipart()
    msg['From'] = send_as
    msg['To'] = COMMASPACE.join(send_to)
    msg['Cc'] = COMMASPACE.join(cc_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'html'))
    if include_ribbon == True:
        x = 0
    else:
        x = 1
    if len(imgfiles) > 0:
        for p in imgfiles:
            fp = open(p, 'rb')
            msgImage = MIMEImage(fp.read(), _subtype="png")
            fp.close()
            msgImage.add_header('Content-ID', '<image'+str(x)+'>')
            msg.attach(msgImage)
            x += 1
    else:
        logging.info("no se adjuntaran imagenes al cuerpo del correo")
    for path in files:
        part = MIMEBase('application', "octet-stream")
        with open(path, 'rb') as filex:
            part.set_payload(filex.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename="{}"'.format(Path(path).name))
        msg.attach(part)
    try:
        smtp = smtplib.SMTP("smtp.office365.com", 587)
        if use_tls:
            smtp.starttls(context=context)
        app_login(app=smtp,credentials_services=[service])
        smtp.sendmail(send_as,
                      send_to+cc_to, msg.as_string())
    except Exception as e:
        # Print any error messages to stdout
        logging.exception("\nEmail Send error: \n")
        print(e)
    finally:
        smtp.quit()


# ============================================================================================================
# Open Excel file and extract images

# ============================================================================================================
# Email alerts, notification about performance

# ============================================================================================================
# SQL Transactions
def spExec(spname, request_token, server='',query_timeout=600,credentials_services=[]):
    try:
        con1 = app_login(app='spExec',request_token=request_token,credentials_services=credentials_services,server=server)
        if con1 == None:
            return
        con1.query_timeout=query_timeout
        con1.execute_query('EXEC '+spname)
        print("Stored Procedure  ejecutado correctamente" + spname)
        resultado = "Stored Procedure  ejecutado correctamente" + spname
        con1.close()
    except Exception as e:
        logging.exception(str(e))
        print("Se ha producido un error inesperado al ejecutar el sp " + spname)
        resultado = "Se ha producido un error inesperado al ejecutar el sp " + spname
    return resultado


def execute_SQLquery(request_token,server="",credentials_services=['SCNEAR'],query=""):
    try:
        conn = app_login(app='execute_SQLquery',request_token=request_token,credentials_services=credentials_services,server=server)
        if conn == None:
            return print("conection to SQl error")
        cursor = conn.cursor()
        conn.autocommit = True
        execution = cursor.execute(query)
        try:
            resultado = cursor.fetchone()[0]
        except Exception as e:
            print(e)
            resultado = execution
        conn.close()
    except IOError as e:
        logging.exception(str(e))
        print("Se ha producido un error inesperado al ejecutar el query " + query)
    return resultado


def SQL_query_to_df(request_token,server=None,credentials_services=[],query=""):
        conn = app_login(app=pyodbc,request_token=request_token,credentials_services=credentials_services,server=server)
        if conn == None:
            return print("conection to SQl error")
        table = pd.read_sql_query(query,conn)
        conn.close()
        return table


def send_df_to_sql(dataframe, tlname, database, schema, request_token,if_exists='replace', server='TPCCP-DB128\\SQLD2016STD',credentials_services=[],index=None, dtype=None):
    """get a given Dataframe and send it to SQL Database.
    Args:
    dataframe(dataframetipe): Dataframe to send
    tlname(str): Name of the table 
    database¨(str): Name of the database
    schema(str): Schema to use (dbo,mail...etc)
    if_exists(str): condition to use, replace or append
    index(str): include index column True or None
    """
    tsql_chunksize = 2097 // len(dataframe.columns)
    # cap at 1000 (limit for number of rows inserted by table-value constructor)
    tsql_chunksize = 1000 if tsql_chunksize > 1000 else tsql_chunksize
    params = app_login(app='send_df_to_sql',request_token=request_token,database=database,server=server,credentials_services=credentials_services)
    if params == None:
            return
    engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
    dataframe.to_sql(name=tlname, schema=schema, if_exists=if_exists, con=engine,
                     index=index, chunksize=tsql_chunksize, dtype=dtype, method='multi')
    engine.dispose()


# ====================================================================================================================================
# file download verify
def file_download_verify(downloadpath):
    x = 0
    while True:
        if os.listdir(downloadpath):
            logging.info(str(downloadpath)+" has files")
            break
        else:
            x += 1
            logging.info(str(downloadpath)+
                         " is empty yet, searching for files again")
            time.sleep(5)
            if x == 12:
                logging.info(
                    "webpage nevers send the file, error in the download process")
                print(
                    "webpage nevers send the file, error in the download process")
                return
            else:
                pass
    while True:
        try:
            filename = max(
            [downloadpath+"\\"+f for f in os.listdir(downloadpath)], key=os.path.getctime)
            time.sleep(10)
            if not ".part" in filename:
                sizefile = os.stat(filename).st_size
                print("file downloaded... verifying size")
                logging.info("file downloaded... verifying size")
                print("File size is: "+str(sizefile))
                logging.info("File size is: "+str(sizefile))
                if sizefile > 0:
                    print("File ok")
                    logging.info("File ok")
                    break
                else:
                    print("The download is not completed yet")
                    logging.info(
                        "The download is not completed yet")
            else:
                print(".part format file found, searching the downloaded file again")
                logging.info(
                    "part format file found,  searching the downloaded file again")
        except Exception:
            print(
                "Verification error, theres not found any file in this folder")
            logging.info(
                "Verification error, theres not found any file in this folder")
            break
    return filename


# ====================================================================================================================================
# stats upload 
    

# ====================================================================================================================================
# email body config
def body_config(body=None, imgcant=0, imgfilespath=None,style='100', imagesheight=[],
                imageswidth=[], timedelta=0,datedelta=0,banner_id=0,request_token=None, credentials_services=[]):
    
    if datedelta == '' or datedelta == ' ':
        datedelta=0
    if timedelta == '' or timedelta == ' ':
        timedelta=0
    banners = read_SQL_table(server='TPCCP-DB128\\SQL2016STD',request_token=request_token,credentials_services=credentials_services,database='PRE_TARSweb',tablename='tbEmailBanners')
    if not int(banner_id) == 0:
        banner=banners[banners['banner_id']==banner_id]
        b64 = banner['banner_base64'].iloc[0]
        bannertag = '<br><img width=1334 height=107  style="width:13.8958in;height:1.1145in"  src="data:image/png;base64,'+b64+'" /><br>'
        body = bannertag+body
    # if '$$$RIBBON--REPORT$$$' in body:
    #     ribbon_image = path+r'\EmailsService\Resources\Ribbons\email label WFM NS - Report.png'
    #     body = body.replace('$$$RIBBON--REPORT$$$',
    #                         '<img width=1334 height=107  style="width:13.8958in;height:1.1145in"  src="cid:image0">')
    #     bodyimgfiles = [ribbon_image]+[os.path.abspath(os.path.join(imgfilespath, p)) for p in sorted(os.listdir(imgfilespath))]
    # elif '$$$RIBBON--ALERT$$$' in body:
    #     ribbon_image = path+r'\EmailsService\Resources\Ribbons\email label WFM NS - Alert.png'
    #     body = body.replace('$$$RIBBON--ALERT$$$',
    #                         '<img width=1334 height=107  style="width:13.8958in;height:1.1145in"  src="cid:image0">')
    # elif '$$$RIBBON--NOTIFICATION$$$' in body:
    #     ribbon_image = path+r'\EmailsService\Resources\Ribbons\email label WFM NS - Notification'
    #     body = body.replace('$$$RIBBON--NOTIFICATION$$$',
    #                         '<img width=1334 height=107  style="width:13.8958in;height:1.1145in"  src="cid:image0">')
    #     bodyimgfiles = [ribbon_image]+[os.path.abspath(os.path.join(imgfilespath, p)) for p in sorted(os.listdir(imgfilespath))]
    # else:
    #     print("this file has not images to send")
    #     bodyimgfiles = [os.path.abspath(os.path.join(imgfilespath, p)) for p in os.listdir(imgfilespath)]
    # adding images to body    
    if imgcant > 0:
        
        bodyimgfiles = [os.path.abspath(os.path.join(imgfilespath, p)) for p in os.listdir(imgfilespath)]
        for x in range(0, imgcant):
            body = body.replace('$$$IMAGE'+str(x+1)+'--HERE$$$', '<div><img width='+str(imageswidth[x])+' height='+str(
                imagesheight[x])+' src="cid:image'+str(x+1)+'" style="width:'+str(style)+'%;height:auto;" /> </div> ')
    else:
        bodyimgfiles = []
        pass
    # adding datetime to body 
    time = datetime.datetime.now()
    time_delta = datetime.timedelta(hours=float(timedelta))
    time = time+time_delta
    date = datetime.datetime.now()
    date_delta = datetime.timedelta(days=float(datedelta))
    date = date+date_delta
    body = body.replace('$$$TIME--HERE$$$', time.strftime("%H:%M"))
    body = body.replace('$$$DATE--HERE$$$', date.strftime("%Y-%m-%d"))
    body = """
    <!DOCTYPE html style="width:auto;height: auto;min-height: 100%;">
    <head>
    </head>
    <body dir="ltr" style="font-size:12pt;color:#000000;background-color:#FFFFFF;font-family:Calibri,Arial,Helvetica,sans-serif;">
    """+body+"""
    </body>
    </html>
    """
    return (body, bodyimgfiles)


# ====================================================================================================================================
# extract images from excel

# ============================================================================================================
# Open Excel file and update

# ==================================================================================================================================================================================
def read_SQL_table(server=None, database=None, tablename=None,request_token=None,credentials_services=[]):
    conn = app_login(app=pyodbc,request_token=request_token,credentials_services=credentials_services,server=server)
    table = pd.read_sql_query(
        'SELECT * FROM ['+database+'].[dbo].['+tablename+']', conn)
    conn.close()
    return table





#def send_df_to_sql_139(dataframe, tlname, database, schema, request_token,if_exists='replace', server='TPCCP-DB139\\SQLD2016STD',credentials_services=[],index=None, dtype=None):
def send_df_to_sql_139(dataframe, sql_user, sql_pw, database, tlname, server ,schema,if_exists, index,dtype ):

    tsql_chunksize = 2097 // len(dataframe.columns)
    # cap at 1000 (limit for number of rows inserted by table-value constructor)
    tsql_chunksize = 1000 if tsql_chunksize > 1000 else tsql_chunksize


    print('SENDING TO DATABASE')
    params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};"

                                        "SERVER="+server+";"

                                        "DATABASE="+database+";"

                                        "Trusted_Connection=yes;"

                                        "UID="+sql_user+";"

                                        "PWD="+sql_pw+";"

                                        "appname=send_df_to_sql_139")

    

    try:
        engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params), encoding="utf-8")
        dataframe.to_sql(name=tlname, schema=schema, if_exists=if_exists, con=engine,
                     index=index, chunksize=tsql_chunksize, dtype=dtype, method='multi')
        engine.dispose()
        #df.to_sql(name=tlname, schema=schema, if_exists='replace', con=engine, chunksize=tsql_chunksize, dtype=dtype, method='multi', )

    except Exception as e:

        traceback.format_exc(e)

        print('Error sending data to sql')



