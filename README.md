# MarkelUnaiProgra

# Librería PyPiston

Esta librería Python facilita la interacción con una API de búsqueda de información sobre coches, permitiendo gestionar datos de clientes, coches y reservas. Aquí se presenta un resumen de las clases clave y sus funciones.

## Clase Cliente
La clase `Cliente` representa clientes con información básica, incluyendo edad, nombre, residencia y una lista opcional de permisos. Proporciona métodos para comprobar la mayoría de edad, añadir permisos y mostrar los datos del cliente en la consola.

## Clase ClienteExt
La clase `ClienteExt` extiende la información de la clase `Cliente`, agregando detalles como la vigencia del permiso, necesidades especiales, compromiso medioambiental y nivel del cliente. Además, ofrece funciones para verificar la vigencia del permiso, añadir necesidades especiales y mostrar los datos del cliente extendido.

## Clase Coche
La clase `Coche` representa un coche deseado y proporciona funciones para buscar información sobre coches en una API. Permite la especificación de criterios de búsqueda como marca, modelo, año, etc. Los resultados se presentan en una tabla.

## Clase Reserva
La clase `Reserva` permite realizar reservas de coches por parte de clientes extendidos. Hereda funcionalidades de las clases `ClienteExt` y `Coche`, y su método `realizar_reserva` verifica la elegibilidad del cliente antes de confirmar la reserva.

## Ejemplo de Uso
El script al final del archivo ejemplifica la funcionalidad completa de la librería, desde la creación de instancias hasta la realización de reservas, demostrando la interacción efectiva con la API de búsqueda de coches.

*Nota*: Se incluye la clave de la API necesaria para acceder a la funcionalidad de búsqueda de coches en la API correspondiente. Asegúrese de mantener la confidencialidad de esta clave.

¡Disfrute utilizando esta librería para gestionar fácilmente reservas de coches y explorar información detallada sobre vehículos!
