import random
import os
import sys
import logging
from time import sleep
import shutil 
from datetime import date, time, datetime, timedelta
from zipfile import ZipFile
import zipfile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
import json
import tarsConstruct_debugs
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import numpy as np
import calendar
import pandas as pd
from os import remove
from datetime import date
import datetime
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import csv

downloadpath = r'\\TPCCP-DB20\Dropbox\Transversal\Flow.ai\SUFI'
fileName = 'brain_events.csv'

read_file2 = pd.read_csv(os.path.join(downloadpath,fileName) , sep="\t",error_bad_lines=False,quoting=csv.QUOTE_NONE,engine="python")
#, error_bad_lines=False, quoting=csv.QUOTE_NONE
#read_file2.to_excel(os.path.join(downloadpath,fileName2))
#read_file2=pd.DataFrame(read_file2)
#read_file2=pd.read_excel(os.path.join(downloadpath,fileName2))
#read_file2['step_name'] = read_file2['step_name'].replace('\n','', regex=True)
for i in range(len(read_file2)):
	
 	try:
 		print(i)
		
 		print(read_file2['__time,agent_id,brain_name,channel_id,channel_name,event_name,flow_id,flow_name,intent_id,intent_label,language,query,step_id,step_name,step_type,thread_id,accuracy,threshold,timestamp'][i])
 	except:
 		pass


#read_file2.to_csv(downloadpath+'\\'+'_'+fileName, index = False, sep = ",")

#read_file2=read_file2.apply(lambda x: x.str.replace(',', ';'))
#read_file2=read_file2.stack().str.replace(',',';').unstack()

#read_file2.to_csv(downloadpath+'\\'+'_'+fileName,index = False)
#read_file2['step_name'][42]=read_file2['step_name'][236].replace('\n','blah blaj')
#if '\t' in read_file2['step_name'][40]:
	#print(ok)
#print(read_file2.columns)

try:
	for i in range(len(read_file2['__time,agent_id,brain_name,channel_id,channel_name,event_name,flow_id,flow_name,intent_id,intent_label,language,query,step_id,step_name,step_type,thread_id,accuracy,threshold,timestamp'])):
		if read_file2['__time,agent_id,brain_name,channel_id,channel_name,event_name,flow_id,flow_name,intent_id,intent_label,language,query,step_id,step_name,step_type,thread_id,accuracy,threshold,timestamp'][i].startswith('""'): 
			read_file2['__time,agent_id,brain_name,channel_id,channel_name,event_name,flow_id,flow_name,intent_id,intent_label,language,query,step_id,step_name,step_type,thread_id,accuracy,threshold,timestamp'][i-1]=read_file2['__time,agent_id,brain_name,channel_id,channel_name,event_name,flow_id,flow_name,intent_id,intent_label,language,query,step_id,step_name,step_type,thread_id,accuracy,threshold,timestamp'][i-1]+read_file2['__time,agent_id,brain_name,channel_id,channel_name,event_name,flow_id,flow_name,intent_id,intent_label,language,query,step_id,step_name,step_type,thread_id,accuracy,threshold,timestamp'][i]+'\t'
			print(read_file2['__time,agent_id,brain_name,channel_id,channel_name,event_name,flow_id,flow_name,intent_id,intent_label,language,query,step_id,step_name,step_type,thread_id,accuracy,threshold,timestamp'][i-1])

	for i in range(len(read_file2['__time,agent_id,brain_name,channel_id,channel_name,event_name,flow_id,flow_name,intent_id,intent_label,language,query,step_id,step_name,step_type,thread_id,accuracy,threshold,timestamp'])):
		if read_file2['__time,agent_id,brain_name,channel_id,channel_name,event_name,flow_id,flow_name,intent_id,intent_label,language,query,step_id,step_name,step_type,thread_id,accuracy,threshold,timestamp'][i].startswith('"2'):
			read_file2['__time,agent_id,brain_name,channel_id,channel_name,event_name,flow_id,flow_name,intent_id,intent_label,language,query,step_id,step_name,step_type,thread_id,accuracy,threshold,timestamp'][i]=read_file2['__time,agent_id,brain_name,channel_id,channel_name,event_name,flow_id,flow_name,intent_id,intent_label,language,query,step_id,step_name,step_type,thread_id,accuracy,threshold,timestamp'][i].replace('"2','2')
			read_file2['__time,agent_id,brain_name,channel_id,channel_name,event_name,flow_id,flow_name,intent_id,intent_label,language,query,step_id,step_name,step_type,thread_id,accuracy,threshold,timestamp'][i]=read_file2['__time,agent_id,brain_name,channel_id,channel_name,event_name,flow_id,flow_name,intent_id,intent_label,language,query,step_id,step_name,step_type,thread_id,accuracy,threshold,timestamp'][i].replace('""""','"')
			print('ok')

	for i in range(len(read_file2['__time,agent_id,brain_name,channel_id,channel_name,event_name,flow_id,flow_name,intent_id,intent_label,language,query,step_id,step_name,step_type,thread_id,accuracy,threshold,timestamp'])):
		if read_file2['__time,agent_id,brain_name,channel_id,channel_name,event_name,flow_id,flow_name,intent_id,intent_label,language,query,step_id,step_name,step_type,thread_id,accuracy,threshold,timestamp'][i].startswith('""'):
			read_file2= read_file2.drop([i],axis=0)
			print('ok')
except:
	print('No se realizo correctamente la limpieza de data')
	pass
read_file2.to_csv(downloadpath+'\\'+'_'+fileName,index = False)