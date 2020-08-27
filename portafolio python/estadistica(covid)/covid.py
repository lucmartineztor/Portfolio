import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as nsn
import csv
import datetime

data=pd.read_csv("osbcovid19_Mayo8.csv",encoding="ISO-8859-1")

registro=10
print(data.head(registro))

data['Fecha de diagnóstico']=pd.to_datetime(data["Fecha de diagnóstico"], dayfirst="True").dt.strftime("%Y%m%d")
data['Fecha de diagnóstico']=data['Fecha de diagnóstico'].astype('datetime64[D]')
data['Fecha de diagnóstico']=data['Fecha de diagnóstico'].dt.dayofyear

print(data.head(registro))

#plt.rcParams["figure.figsize"]=(14,5)

ax=data.hist('Fecha de diagnóstico', bins =(max(data['Fecha de diagnóstico'])-min(data['Fecha de diagnóstico'])+1))
print('Dia del año con diagnóstico')
plt.show()
ax=data.hist('Fecha de diagnóstico', bins =(max(data['Fecha de diagnóstico'])-min(data['Fecha de diagnóstico'])+1), cumulative='True')
print('Casos acumulados año con diagnóstico')
plt.show()



data['Fecha de diagnóstico']=data['Fecha de diagnóstico']-min(data['Fecha de diagnóstico'])
ax=data.hist('Fecha de diagnóstico', bins =(max(data['Fecha de diagnóstico'])-min(data['Fecha de diagnóstico'])+1))
print('Casos acumulados año con diagnóstico a partir del primer caso ')
plt.show()

ax=data.hist('Edad', bins =(max(data['Edad'])-min(data['Edad'])+1))
print('Casos por edad en Bogota')
plt.show()

data_kennedy=data[(data["Localidad de residencia"]=="08 - Kennedy")]
print("Contagios Localidad kennedy: ", len(data_kennedy))

data_fallecido=data[(data["Estado"]=="Fallecido")]
print("Contagios Fallecidos  en kennedy: ", len(data_fallecido))

print(data.head(registro))

data_fallecido_Kennedy=data_fallecido[(data_fallecido["Localidad de residencia"]=="08 - Kennedy")]
print("Fallecido  en kennedy", len(data_fallecido_Kennedy))
print(data_fallecido_Kennedy)



df=data[["Edad","Estado", "Ubicación","Fecha de diagnóstico"]]
df.Edad.plot.hist ( bins =(max(data['Fecha de diagnóstico'])-min(data['Fecha de diagnóstico'])+1))
plt.show()    #  ES lo mismo
x=data.Edad.plot.hist (bins =(max(data['Fecha de diagnóstico'])-min(data['Fecha de diagnóstico'])+1))
plt.title("Edad")
plt.xlabel("fecha")
plt.ylabel("cantidad")

plt.show()    #  ES lo mismo

x=data.hist ("Edad", bins =(max(data['Fecha de diagnóstico'])-min(data['Fecha de diagnóstico'])+1))
plt.show()    #  ES lo mismo (con titulo y cuadricula)


df.plot.scatter(x="Estado", y="Edad", alpha=0.2) #dispersion de datos
plt.show()

valor_por_edad=df.groupby("Estado")["Edad"].mean()#Observar el valor promedio de edades por estado
valor_por_edad.head(10).plot.bar()
plt.show()

df.groupby("Estado")["Estado"].count().plot(kind='bar')#Para contar cantidad en cada elemtno
plt.show()

df.Estado.value_counts().plot.pie()
plt.show()

plt.plot(df.Edad,df.Edad) #funcion continua
plt.show()

# df["VALOR"]=pd.qcut(df.Edad,5)
# df.boxplot(column="Estado", by="VALOR", figsize=(8,6))
# plt.show()
