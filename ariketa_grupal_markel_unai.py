#clase padre: coche con información básica (num puertas, potencia, km, gasolina/diesel).
#clase pijadas: color, materiales, carrocería, sistemas inteligentes, accesorios.
#clase entidades: viendo la información de las dos clases anteriores, ver información de entidades con API.
#clase cliente: edad, permisos de conducción (B, A2), vigencia del permiso, necesidades especiales, compromiso mediambiental.
#¿ALGÚN TIPO DE SISTEMA DE RESERVAS?

#The free data-set is limited to 2020 vehicles.

#HERENCIA: PADRE > PIJADAS > ENTIDADES
#CLIENTE (APARTE)

#api token: f0f9e10c-0542-4b91-a45c-54419b56409d
#api secret: e556018c33fa71b761aeeeb432bf3c7d

#(api ninjas) api key: rUOzDWFri1lB3FtYK8/GPA==Y1fB8p8RH8uO0EDt

from datetime import datetime, date
import requests
import json
from tabulate import tabulate

class Cliente:
    def __init__(self, edad, nombre, residencia, permiso = []):
        self.edad = edad
        self.mayoria_edad = self.comprobacion_edad()
        self.nombre = nombre
        self.residencia = residencia
        self.permiso = permiso

    def comprobacion_edad(self):
        if self.edad>= 18:
            return True
        else:
            return False

    def añadir_permiso(self, permiso_nuevo):
        self.permiso.append(permiso_nuevo)

    def show_cliente(self):
        return(print("Datos del cliente: " + "\n" + "NOMBRE: " + self.nombre + "\n" + "EDAD: " + str(self.edad) + "\n" + "RESIDENCIA: " 
                     + self.residencia + "\n" + "PERMISO(S):" + str(self.permiso) + "\n" + "MAYOR DE EDAD: " + "SI" if self.mayoria_edad == True else "NO"))

class ClienteExt(Cliente):
    def __init__(self, cliente, vigencia_permiso, necesidades_especiales, compromiso_medioambiental, nivel_cliente):
        super().__init__(cliente.edad, cliente.nombre, cliente.residencia, cliente.permiso)
        self.vigencia_permiso = datetime.strptime(str(vigencia_permiso), "%Y-%m-%d").date()
        self.necesidades_especiales = necesidades_especiales
        self.compromiso_medioambiental = compromiso_medioambiental
        self.nivel_cliente = nivel_cliente
    
    def es_vigente(self) -> bool:
        if self.vigencia_permiso > date.today():
            return True
        else:
            return False
        
    def añadir_necesidad_especial(self):
        self.necesidades_especiales = True

    def show_clientext(self):
        super().show_cliente()
        print("VIGENCIA DEL PERMISO:", self.vigencia_permiso)
        print("NECESIDADES ESPECIALES:", self.necesidades_especiales)
        print("COMPROMISO MEDIOAMBIENTAL:", self.compromiso_medioambiental)
        print("NIVEL DEL CLIENTE:", self.nivel_cliente)

class Coche():
    def __init__(self, make, model = "", fuel_type = "", year = "", transmision = "", cylinders = ""):
        self.make = make
        self.model = model
        self.fuel_type = fuel_type
        self.year = year
        self.transmision = transmision
        self.cylinders = cylinders
        self.inform_busqueda_coche = ""

    def buscar_coche(self, en_base_a):
        api_url = 'https://api.api-ninjas.com/v1/cars?'
        try:
            for i in en_base_a:
                if i == "year":
                    api_url += '&' + i + '=' + self.year
                if i == "transmission":
                    api_url += '&' + i + '=' + self.transmission
                if i == "make":
                    api_url += '&' + i + '=' + self.make
                if i == "model":
                    api_url += '&' + i + '=' + self.model
                if i == "fuel_type":
                    api_url += '&' + i + '=' + self.fuel_type
                if i == "cylinders":
                    api_url += '&' + i + '=' + self.cylinders

            response = requests.get(api_url, headers={'X-Api-Key': 'rUOzDWFri1lB3FtYK8/GPA==Y1fB8p8RH8uO0EDt'})
            response.raise_for_status()  # Lanzar una excepción si la solicitud no fue exitosa

            if response.status_code == requests.codes.ok:
                if response.text != "[]": 
                    self.inform_busqueda_coche = json.loads(response.text)
                else:
                    raise Exception("La respuesta de la API está vacía")
            else:
                print("Error:", response.status_code, response.text)

        except requests.exceptions.RequestException as e:
            print("Error en la solicitud a la API:", str(e))

        except json.JSONDecodeError as e:
            print("Error al decodificar la respuesta JSON de la API:", str(e))

    def mostrar_inform_busqueda_coche(self):
        headers = ["Resultado", "Marca", "Modelo", "Año", "Gasolina/Diesel", "Cilindros"]
        car_data = []

        for index, coche in enumerate(self.inform_busqueda_coche):
            car_data.append([index+1, coche["make"].title(), coche["model"].title(), coche["year"],\
                              "Gasolina" if coche["fuel_type"] == "gas" else "Diesel" if coche["fuel_type"] == "diesel" else coche["fuel_type"],\
                                  coche["cylinders"]])

        print(tabulate(car_data, headers, tablefmt="grid"))

class Reserva(ClienteExt, Coche):
    def __init__(self, clientext, coche, num_resultado_reservado = 0):
        super().__init__(cliente, clientext.vigencia_permiso, clientext.necesidades_especiales, clientext.compromiso_medioambiental, clientext.nivel_cliente)
        Coche.__init__(self, coche.make, coche.model, coche.fuel_type, coche.year, coche.transmision, coche.cylinders)
        self.num_resultado_coche_reservado = num_resultado_reservado

    def realizar_reserva(self, num_resultado_reserva):
        try:
            if 1 <= num_resultado_reserva <= len(coche.inform_busqueda_coche):
                if "B" in self.permiso and self.mayoria_edad:
                    print("Reserva realizada para el coche identificado con el Nº", num_resultado_reserva)
                else:
                    print("El cliente no cumple los requisitos para realizar la reserva.")
            else:
                print("El número de resultado de reserva está fuera de rango.")
        except TypeError:
            print("Debe introducir un número que indique el número de resultado que desea reservar.")

if __name__ == "__main__":
    cliente = Cliente(23, "Duranito", "ArrigoCity")
    print(cliente.comprobacion_edad())
    print(cliente.añadir_permiso("C1"))
    #print(cliente.permiso)
    #cliente.show_cliente()
    clientext = ClienteExt(cliente, "2027-01-27", False, "Alto", "Alto")
    print(clientext.es_vigente())
    print(clientext.añadir_necesidad_especial())
    clientext.show_clientext()

    coche = Coche("audi", year = "2003")
    coche.buscar_coche(["make", "year"])
    coche.mostrar_inform_busqueda_coche()

    reserva = Reserva(clientext, coche)
    reserva.realizar_reserva(3)