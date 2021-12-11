# pyDevops_UFER

## Arquitectura y tecnologias usadas

### Arquitectura de la app

<img src="./readme_pictures/arquitectura_por_capas_pydevops.png">

La arquitectura de la aplicación se divide en tres capas y una entidad diferenciada:

- Capa de presentación: donde se muestra la página y el usuario interactua con el controlador.

- Capa de Dominio / Negocio: donde reside la lógica de la aplicacion.

- Capa de acceso a datos: la capa que accede a los datos almacenados en una base de datos en la nube.

- MongoDB Atlas: es la base de datos en la nube sobre la cual interactua la aplicación.

### Tecnologias usadas

La principal funcionalidad es generar archivos Markdown con los datos almacenados en la base de datos MongoAtlas en el Static site generator Hugo. A continuación se especifícan las tecnologías utilizadas.

Principalmente, la aplicación gira entorno a una base de datos (BBDD), Mongodb. Mongodb es un sistema de BBDD NoSQL, orientado a documentos y de código abierto. En lugar de guardar los datos en tablas, tal y como se hace en las bases de datos relacionales, MongoDB guarda estructuras de datos BSON. Para ser más específico, se han realizado las consultas en MongoAtlas, un servicio en la nube de Mongodb.

Los datos plasmados estaban escritos en un Static site generator, el que nos indicaron usar era Hugo. Hugo es uno de los generadores de sitios estáticos de código abierto más populares. Con su asombrosa velocidad y flexibilidad.

La aplicación ha sido desarrollada con el lenguaje de programacion python version 3.9 . Para crear el programa se han tenido que instalar las siguientes dependencias:
- Para realizar los test sobre los módulos del programa hemos usado pytest version 6.2.5.
- La conexión con la base de datos tuvimos que instalar la librería de pymongo version 3.12.1.
- Para la conexión a la BBDD con pymongo tuvimos que añadir certifi para la conexión SSL.
- La validación de los schema se ha instalado el módulo jsonchema.



## Diagrama de componentes

<img src="./readme_pictures/diagrama_componentes_pydevops.png">

Nuestro programa principal de compone de tres elementos esenciales y un cuarto que es el dedicado a  la Static site gen:
- repository
- model
- controller
- view

### repository

Aquí tenemos el módulo db_conection, es el que se encarga de establecer la conexión con la base de datos.

### model

Se centra en el CRUD "Crear, Leer, Actualizar y Borrar" de la BBDD. Por eso lo vinculamos con reposiroty. También almacenando otras utilidades que le ayuda a realizar dichas actividades. 

En este módulo tenemos un módulo para verificar los datos y uno que usaremos para seleccionar los los servicios.
- service_selection
- data_validation

Los módulos,que dependen de repository ya que la conexión con la BBDD es necesaria, realizarán el CRUD son:
- data_extraction: para leer los datos, aparte contiene la funcionalidad de pasar los datos para ser visualizados en el Static site gen.
- data_creation: este módulo pide al usuario los datos para crear un documento en la BBDD 
- data_deletion: es el encargado de eliminar los datos del usuario.
- data_updation: se encarga de actualizar los datos de la BBDD

Aparte encontramos los módulos encargados de usar los datos de la BBDD en Hugo:
- contente_generation: depende de los datos extraidos, se encargará generar los archivos que se visualizarán en Hugo. 
- content_deletion: se encarga de cuando se eliminen los datos , actualice la página y se desaparezca la página dedicada a ese item
- content_updation: es la encargada de cuando se cambien los datos de un item los actualizará en el archivo de Hugo.

### view 

El repositorio view, contiene todo lo necesario para iniciar Hugo con su configuración correspondiente. Por este motivo View depende de todos los módulos content, ya que son los que hacen que se actualice y genere la información de la página.

### controller 

El controller es totalmente dependiente de model, ya que es el encargado de crear un menu para controlar las funcionalidades que hay en model.


