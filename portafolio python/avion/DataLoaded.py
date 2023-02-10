
import matplotlib.pyplot as plt
import numpy as np
import pymongo
import datetime
import certifi
import pandas as pd
import matplotlib.pyplot as plt 
import numpy
'''_id
airline
origin_airport     
destination_airport
scheduled_time     
elapsed_time       
scheduled_departure
departure_delay    
arrival_delay'''

def connection():
    try:
        conn_str = "mongodb+srv://jmelo:Platino1941$@cluster0.kxsnpeg.mongodb.net/?retryWrites=true&w=majority"
        ca = certifi.where()
        try:
            client = pymongo.MongoClient(conn_str, tlsCAFile=ca)
            
        except Exception:
            print("Error:" + Exception)
        db = client["Final_Project"]
        #print (db)
        mycollection = db["Flights"]
        return mycollection ,client
    except Exception as e:
        print(e)
        
    
       

def HeatMap(mycollection):
        start = datetime.datetime(2015,1,1,0,5)
        end = datetime.datetime(2015,1,31,23,59)

        #myquery = mycollection.find({'departure_delay':{'$gt':240}}) #flights with delays greatest than 6 hours
        myquery = mycollection.find().limit(10000)
        #myquery = mycollection.find({'$and':[{'scheduled_departure':{'$gt':start, '$lt':end}},{'destination_airport':'Denver International Airport'}]})
        
        #myquery2 = flights departured from Denver International Airport between 2015-01-01 00:05 and 2015-01-31 23:59
        #for i in myquery:
        #    print(i) 
        
        airlines=[]
        origin_airport=[]
        
        data = pd.DataFrame(list(myquery))
        print(type(data))
        for i in data.columns:
            print(i)
        
        for i in data['airline'].unique():
            airlines.append(i)
        for i in data['origin_airport'].unique():
             origin_airport.append(i)
        print(airlines)
        data.drop(columns='_id')
        data['airline']=data['airline'].astype('category').cat.codes
        #print(data['origin_airport'])
        data['origin_airport']=data['origin_airport'].astype('category').cat.codes
        #print(data['origin_airport'])
        data['destination_airport']=data['destination_airport'].astype('category').cat.codes
        plt.matshow(data.corr())
        
        plt.show()
        return airlines,origin_airport
        
        
def DelayvsAirline(mycollection,airlines):
    plot=[]
    for i in airlines:
        myquery = mycollection.count_documents({'$and':[{'arrival_delay':{'$lt':0}},{'airline':i}]})
        plot.append(myquery)
    print(plot)
    sum=0
    for i in plot:
        sum=sum+i

    percent=[]
    for i in plot:
        i=i*100/sum
        percent.append(i)
    x=numpy.array(airlines,dtype=object) 
    y=numpy.array(percent,dtype=object)
    plt.barh(x,y)
    plt.title("Number of arrival flights delayed")
    plt.xlabel("Number of arrival flights delayed")
    plt.ylabel("airline")
    plt.show()                  

def NondelayvsAirline(mycollection,airlines):
    plot=[]
    for i in airlines:
        myquery = mycollection.count_documents({'$and':[{'departure_delay':{'$gt':0}},{'airline':i}]})
        plot.append(myquery)
    print(plot)
    sum=0
    for i in plot:
        sum=sum+i
    print(sum)
    percent=[]
    for i in plot:
        i=i*100/sum
        percent.append(i)
    print(percent)
    x=numpy.array(airlines,dtype=object) 
    y=numpy.array(percent,dtype=object)
    plt.barh(x,y)
    plt.title("Number of departure flights delayed")
    plt.xlabel("Number of flights delayed")
    plt.ylabel("airline")
    plt.show()

def DelayvsOriginairport(mycollection,origin_airport):
    plot=[]
    for i in origin_airport:
        myquery = mycollection.count_documents({'$and':[{'departure_delay':{'$gt':0}},{'origin_airport':i}]})
        plot.append(myquery)
    print(plot)
    sum=0
    for i in plot:
        sum=sum+i
    font = {'size': 10}
    percent=[]
    for i in plot:
        i=i*100/sum
        percent.append(i)
    x=numpy.array(origin_airport[0:20],dtype=object) 
    y=numpy.array(percent[0:20],dtype=object)
    plt.barh(x,y,color=['green'])
    plt.rc('font', **font)
    plt.title("Number of flights delayed")
    plt.xlabel("Number of flights delayed")
    plt.ylabel("airport")
    plt.show()
    
def MostDelayed(mycollection):
    
    myquery = mycollection.find({'$and':[{'arrival_delay':{'$lt':0}}]}).sort('arrival_delay',1).limit(15)
    data = pd.DataFrame(list(myquery))
    x=numpy.array(data.destination_airport,dtype=object) 
    y=numpy.array(data.arrival_delay,dtype=object)
    plt.barh(x,y,color=['black', 'red', 'black', 'red', 'black'])
    plt.tick_params(axis='y', which='both', labelleft=False, labelright=True, labelsize=10)
    
    plt.title("Arrival delayed accumulated")
    plt.xlabel("Hours delayed",rotation=0, fontsize=8)
    plt.ylabel("Destination Airport",rotation=90, fontsize=8)
    plt.savefig("ArrivalDelayedAccumulated.jpg")
    plt.show()
    
    

try:
    mycollection,client = connection()
except Exception as e:
    print(e)
    pass
try:    
    airlines,origin_airport=HeatMap(mycollection)
except Exception as e:
    print(e)
    pass
try:    
    DelayvsAirline(mycollection,airlines)
except Exception as e:
    print(e)
    pass
try:    
    NondelayvsAirline(mycollection,airlines)
except Exception as e:
    print(e)
    pass
try:    
    DelayvsOriginairport(mycollection,origin_airport)
except Exception as e:
    print(e)
    pass
try:    
    MostDelayed(mycollection)
except Exception as e:
    print(e)
    pass
client.close()
    
