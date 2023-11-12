.. PyPiston documentation master file, created by
   sphinx-quickstart on Mon Nov 10 16:48:24 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

¡Bienvenido a la documentación de PyPiston!
===========================================

La librería proporciona una interfaz para interactuar con una API de búsqueda de información sobre coches, gestionando datos de clientes, coches y reservas.

.. toctree::
   :maxdepth: 4
   :caption: Contents:

.. automodule:: PyPiston


==================
Cliente
==================

La clase Cliente representa clientes con información básica

.. autoclass:: Cliente
   :members:
   :special-members: __init__, comprobacion_edad, añadir_permiso, show_cliente

      Representa un cliente con información básica.

   .. automethod:: __init__
      :noindex:

         Inicializa una instancia de la clase Cliente.

   .. automethod:: comprobacion_edad
      :noindex:

         Comprueba si el cliente es mayor de edad.

   .. automethod:: añadir_permiso
      :noindex:

         Añade un permiso a la lista de permisos del cliente.

   .. automethod:: show_cliente
      :noindex:

         Muestra los datos del cliente en la consola.


=====================
ClienteExt
=====================

ClienteExt extiende esta información con detalles adicionales de Cliente.

.. autoclass:: ClienteExt
   :members:
   :special-members: __init__, es_vigente, añadir_necesidad_especial, show_clientext

      Representa un cliente extendido con información adicional.

   .. automethod:: __init__
      :noindex:

         Inicializa una instancia de la clase ClienteExt.

   .. automethod:: es_vigente
      :noindex:

         Comprueba si el permiso del cliente está vigente.

   .. automethod:: añadir_necesidad_especial
      :noindex:

         Añade necesidades especiales al cliente.

   .. automethod:: show_clientext
      :noindex:

         Muestra los datos del cliente extendido en la consola.


=====================
Coche
=====================

La clase Coche permite buscar información de coches en la API.

.. autoclass:: Coche
   :members:
   :special-members: __init__, buscar_coche, mostrar_inform_busqueda_coche

      Representa un coche deseado y proporciona funciones para buscar información de coches a través de una API.

   .. automethod:: __init__
      :noindex:

         Inicializa una instancia de la clase Coche.

   .. automethod:: buscar_coche
      :noindex:

         Realiza una búsqueda de coches en una API en función de los criterios especificados.

   .. automethod:: mostrar_inform_busqueda_coche
      :noindex:

         Muestra los resultados de la búsqueda de coches en forma de tabla.


======================
Reserva
======================

La clase Reserva facilita la reserva de coches, verificando la vigencia del permiso del cliente.

.. autoclass:: Reserva
   :members:
   :special-members: __init__, realizar_reserva

      Representa una reserva de un coche realizada por un cliente extendido.

   .. automethod:: __init__
      :noindex:

         Inicializa una instancia de la clase Reserva.

   .. automethod:: realizar_reserva
      :noindex:

         Realiza una reserva de un coche en función del número de resultado de búsqueda.
