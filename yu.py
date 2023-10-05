informacio = {}

class Vehiculo:
    id = 0
    marca='' # Privado
    modelo=""
    velocidad = 0 
    velocidadMaxima = 0
    velocidadmn=0 
    color = '' 
    pais = 'Colombia' 
    
    def __init__(self,id,marca,modelo,color,pais,velocidad_m):
        self.id = id
        self.marca = marca
        self.modelo=modelo
        self.color = color
        self.pais = pais
        self.velocidadMaxima = velocidad_m

    def encender(self):
        self.estado = "encendido"

    def apagar(self):
        self.estado = "apagado"
    def velocidadm(self,cant):
        self.velocidadMaxima = cant
        
    def acelerar(self,cant):

        cant = int(input("ingrese cuánto quiere acelerar:"))
        self.velocidad = self.velocidad + cant
        if (self.velocidad <0):
                self.velocidad =0
        elif    self.velocidad > self.velocidadMaxima:
                 self.velocidad = self.velocidadMaxima 

 
    def frenar(self):
                cant = int(input("ingrese cuánto quiere frenar:"))
                self.velocidad = self.velocidad - cant
                if self.velocidad < 0:
                    self.velocidad = 0
                
        

def cambiarVelocidad(id, cant):
    for elem in listaAutos:
        if(id==elem.id):
            elem.velocidad=elem.velocidad + cant
            if(elem.velocidad<0):
                elem.velocida=0
            elif (elem.velocidad > elem.velocidadMaxima):
                elem.velocidad = elem.velocidadMaxima

            

def frenarVelocidad(id, cant):
    for elem in listaAutos:
        if(id==elem.id):
            elem.velocidad=elem.velocidad - cant
            if(elem.velocidad<0):
                elem.velocidad=0
            
def mostrar():
    for elem in listaAutos:
        print("id:",elem.id,"marca:",elem.marca,"modolo:",elem.modelo,"color:",elem.color,"pais:",elem.pais,"velocidad maxima:", elem.velocidadMaxima,"velocidad actual:",elem.velocidad )
        
def registrar():
    marca = input(f"ingrese la marca del vehículo :")
    modelo = input("ingrese el modelo del vehículo:")
    color = input("ingrese el color del vehículo:")
    pais = input("ingrese el país de origen del vehículo:")
    velocidad_m = int(input("ingrese la velocidad máxima del vehículo:"))
    id = int(len(listaAutos)) + 1
    informacio[id] = {
            "id": id ,
            "marca":marca,
            "modelo": modelo,
            "color": color,
            "pais": pais,
            "velocidad": 0,
            "velocidad_maxima": velocidad_m,
        }
    carros = Vehiculo(id,marca,modelo,color,pais,velocidad_m)
    listaAutos.append(carros)
    return carros

listaAutos = [] 
op=0      
while True:
    print("1. registar auto")
    print("2. mostrar autos")
    print("3. aclerarar auto")    
    print("4. frenar auto")    
    print("3. acelerar auto")    
    print("4. frenar auto")             
    op=int(input("ingrese una opcion:"))

    if(op==1):
       carro=registrar()
    elif(op==2):
        mostrar()
    elif(op==3):
        carro.encender()
        print("auto encendido")
    elif(op==4):
        carro.apagar()
        print("vehiculo apagado")
    elif(op==5):
        mostrar()
        idw = int(input("Seleccione el id del auto: "))        
        cants = int(input("Cuanto desea acelerar: "))
        cambiarVelocidad(idw,cants)
    elif(op==6):
        mostrar()
        idw = int(input("Seleccione el id del auto: "))        
        cants = int(input("Cuanto desea acelerar: "))
        frenarVelocidad(idw,cants)