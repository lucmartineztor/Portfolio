from flask import Flask, request,json,abort

app = Flask(__name__)

#Genera la ruta del endpoint para la peticion
@app.route("/procesingEndpoint",methods=["GET"])



def formulario():
    try:
        #almacena los parametros de la peticion get
        monto = request.args.get('monto')
        Id = request.args.get('Id')
        total=int(monto)*int(Id)/4
        #almacena valores en forma de diccionario
        respuesta = {'success':'ok','total':total}
        #convierte a Json
        respuesta_Json = json.dumps(respuesta)
        return respuesta_Json

    except:
        return "Introduzca valores validos de monto y Id"



if __name__ == '__main__':
    app.run(debug=True, port=5)


    #return "<h1>El monto es: {}</h1> <h1>El Id es: {} </h1>".format(monto,Id)
    #ID = request.args.get('ID')

 #   @app.route('/saludo/',methods=['GET'])
#def saludo(nombre):
   # return 'Hola ' + nombre + '!!!'