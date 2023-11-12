
#(api ninjas) api key: rUOzDWFri1lB3FtYK8/GPA==Y1fB8p8RH8uO0EDt

from datetime import datetime, date
import requests
import json
from tabulate import tabulate

class Cliente:
    """Representa un cliente con información básica."""

    def __init__(self, edad, nombre, residencia, permiso=[]):
        """
        Inicializa una instancia de la clase Cliente.

        :param edad: La edad del cliente.
        :param nombre: El nombre del cliente.
        :param residencia: La residencia del cliente.
        :param permiso: Una lista de permisos del cliente (opcional).
        """
        self.edad = edad
        self.mayoria_edad = self.comprobacion_edad()
        self.nombre = nombre
        self.residencia = residencia
        self.permiso = permiso

    def comprobacion_edad(self):
        """
        Comprueba si el cliente es mayor de edad.

        :return: True si el cliente es mayor de edad, False en caso contrario.
        """
        if self.edad >= 18:
            return True
        else:
            return False

    def añadir_permiso(self, permiso_nuevo):
        """
        Añade un permiso a la lista de permisos del cliente.

        :param permiso_nuevo: El permiso a añadir.
        """
        self.permiso.append(permiso_nuevo)

    def show_cliente(self):
        """
        Muestra los datos del cliente en la consola.

        :return: None
        """
        print("Datos del cliente:\nNOMBRE: {}\nEDAD: {}\nRESIDENCIA: {}\nPERMISO(S): {}\nMAYOR DE EDAD: {}".format(
            self.nombre, self.edad, self.residencia, self.permiso, "SI" if self.mayoria_edad else "NO"))

class ClienteExt(Cliente):
    """Representa un cliente extendido con información adicional."""

    def __init__(self, cliente, vigencia_permiso, necesidades_especiales, compromiso_medioambiental, nivel_cliente):
        """
        Inicializa una instancia de la clase ClienteExt.

        :param cliente: Un objeto de la clase Cliente que se extiende.
        :param vigencia_permiso: La vigencia del permiso del cliente (en formato "YYYY-MM-DD").
        :param necesidades_especiales: Indica si el cliente tiene necesidades especiales (True o False).
        :param compromiso_medioambiental: El nivel de compromiso medioambiental del cliente.
        :param nivel_cliente: El nivel del cliente.
        """
        super().__init__(cliente.edad, cliente.nombre, cliente.residencia, cliente.permiso)
        self.vigencia_permiso = datetime.strptime(str(vigencia_permiso), "%Y-%m-%d").date()
        self.necesidades_especiales = necesidades_especiales
        self.compromiso_medioambiental = compromiso_medioambiental
        self.nivel_cliente = nivel_cliente

    def es_vigente(self) -> bool:
        """
        Comprueba si el permiso del cliente está vigente.

        :return: True si el permiso está vigente, False en caso contrario.
        """
        if self.vigencia_permiso > date.today():
            return True
        else:
            return False

    def añadir_necesidad_especial(self):
        """Añade necesidades especiales al cliente."""
        self.necesidades_especiales = True

    def show_clientext(self):
        """
        Muestra los datos del cliente extendido en la consola.

        :return: None
        """
        super().show_cliente()
        print("VIGENCIA DEL PERMISO:", self.vigencia_permiso)
        print("NECESIDADES ESPECIALES:", self.necesidades_especiales)
        print("COMPROMISO MEDIOAMBIENTAL:", self.compromiso_medioambiental)
        print("NIVEL DEL CLIENTE:", self.nivel_cliente)

class Coche:
    """Representa un coche deseado y proporciona funciones para buscar información de coches a través de una API."""

    def __init__(self, make, model="", fuel_type="", year="", transmission="", cylinders=""):
        """
        Inicializa una instancia de la clase Coche.

        :param make: La marca del coche.
        :param model: El modelo del coche (opcional).
        :param fuel_type: El tipo de combustible del coche (opcional).
        :param year: El año del coche (opcional).
        :param transmission: El tipo de transmisión del coche (opcional).
        :param cylinders: El número de cilindros del coche (opcional).
        """
        self.make = make
        self.model = model
        self.fuel_type = fuel_type
        self.year = year
        self.transmission = transmission
        self.cylinders = cylinders
        self.inform_busqueda_coche = ""

    def buscar_coche(self, en_base_a):
        """
        Realiza una búsqueda de coches en una API en función de los criterios especificados.

        :param en_base_a: Una lista de criterios de búsqueda (p. ej., ["year", "make"]).
        :return: None
        """
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
        """
        Muestra los resultados de la búsqueda de coches en forma de tabla.

        :return: None
        """
        headers = ["Resultado", "Marca", "Modelo", "Año", "Gasolina/Diesel", "Cilindros"]
        car_data = []

        for index, coche in enumerate(self.inform_busqueda_coche):
            car_data.append([index+1, coche["make"].title(), coche["model"].title(), coche["year"],\
                              "Gasolina" if coche["fuel_type"] == "gas" else "Diesel" if coche["fuel_type"] == "diesel" else coche["fuel_type"],\
                                  coche["cylinders"]])

        print(tabulate(car_data, headers, tablefmt="grid"))

class Reserva(ClienteExt, Coche):
    """Representa una reserva de un coche realizada por un cliente extendido."""

    def __init__(self, clientext, coche, num_resultado_reservado = 0):
        """
        Inicializa una instancia de la clase Reserva.

        :param clientext: Un objeto de la clase ClienteExt que realiza la reserva.
        :param coche: Un objeto de la clase Coche que se va a reservar.
        :param num_resultado_reservado: El número de resultado de la búsqueda de coche a reservar (opcional).
        """
        super().__init__(cliente, clientext.vigencia_permiso, clientext.necesidades_especiales, clientext.compromiso_medioambiental, clientext.nivel_cliente)
        Coche.__init__(self, coche.make, coche.model, coche.fuel_type, coche.year, coche.transmision, coche.cylinders)
        self.num_resultado_coche_reservado = num_resultado_reservado

    def realizar_reserva(self, num_resultado_reserva):
        """
        Realiza una reserva de un coche en función del número de resultado de búsqueda.

        :param num_resultado_reserva: El número de resultado de la búsqueda de coche a reservar.
        :return: None
        """
        try:
            num_resultado_reserva = int(num_resultado_reserva)
        except ValueError:
            print("El número de resultado de reserva debe ser un número entero válido.")
            return
        
        try:
            if 1 <= int(num_resultado_reserva) <= len(coche.inform_busqueda_coche):
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