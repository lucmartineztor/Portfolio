#En este caso la idea es hacer una peticion por python a la pagina escrita de 
# para obtener texto.
#El texto en este caso se coloco por AppScript (como footer)
import requests
import json
#Se hace la peticion a la Url
def Gato():
	#Se hace la peticion a la Url
	r = requests.get("https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1",)
	#Si el proceso es exitoso, extraer la informacion del json
	if r.status_code == 200:
		cat_fact=json.loads(r.text)
		return cat_fact["text"]

#Se crea el objeto a partir de la clase 
gato1=Gato()
print (gato1)


