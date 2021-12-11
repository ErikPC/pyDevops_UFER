# pyDevops_UFER

## Arquitectura y tecnologias usadas

### Tecnologias usadas

La principal funcionalidad es generar archivos markdown con los datos almacenados en la base de datos mongo atlas en el Static site generator Hugo. A continuación se especifican las tecnologias utilizadas.

Principalmente, la aplicación gira entorno a una base de datos (BBDD), Mongodb. Mongodb es un sistema de BBDD NoSQL, orientado a documentos y de código abierto. En lugar de guardar los datos en tablas, tal y como se hace en las bases de datos relacionales, MongoDB guarda estructuras de datos BSON. Para ser más específico, se han realizado las consultas en MongoAtlas, un servicio en la nube de Mongodb.

Los datos plasmados estaban escritos en un Static site generator, el que nos indicaron usar era Hugo. Hugo es uno de los generadores de sitios estáticos de código abierto más populares. Con su asombrosa velocidad y flexibilidad.

La aplicación ha sido desarrollada con el lenguaje de programacion python version 3.9 . Para crear el programa se han tenido que instalar las siguientes dependencias:
- Para realizar los test sobre los modulos del programa hemos usado pytest version 6.2.5.
- La conexion con la base de datos tuvimos que instalar la libreria de pymongo version 3.12.1.
- Para la conexion a la BBDD con pymongo tuvimos que añadir certifi para la conexion SSL.
- La validación de los schema se ha instalado el modulo jsonchema.

### Diagrama de componentes

Nuestro programa principal de compone de tres elementos esenciales y un cuarto que es el dedicado a  la Static site gen:
- repository
- model
- controller
- view

### repository

Aqui tenemos el modulo db_conection, es el que se encarga de establecer la conexion con la base de datos.

### model

Se centra en el CRUD "Crear, Leer, Actualizar y Borrar" de la BBDD. Por eso lo vinculamos con reposiroty. Tambien almacenando otras utilidade que le ayuda a realizar dichas actividades. 

En este modulo tenemos un modulo para verificar los datos y uno que usaremos para seleccionar los los servicios.
- service_selection
- data_validation

Los modulos,que dependen de repository ya que la conexion con la BBDD es necesaria, realizaran el CRUD son:
- data_extraction: para leer los datos, aparte contiene la funcionalidad de pasar los datos para ser visualizados en el Static site gen.
- data_creation: este modulo pide al usuario los datos para crear un documento en la BBDD 
- data_deletion: es el encargado de eliminar los datos del usuario.
- data_updation: se encarga de actualizar los datos de la BBDD

Aparte encontramos los modulos encargados de usar los datos de la BBDD en Hugo:
- contente_generation: depende de los datos extraidos, se encargara generar los archivos que se visualizaran en Hugo. 
- content_deletion: se encarga de cuando se eliminen los datos , actualice la pagina y se desaparezca la pagina dedicada a ese item
- content_updation: es la que cuando se cambien los datos de un item los actualizara en el archivo de Hugo.

### view 

El repositorio view, contiene todo lo necesario para iniciar Hugo con su configuracion correspondiente. Por este motivo View depende de todos los modulos content, ya que son los que hacen que se actualice y genere la informacion de la página.

### controller 

El controller es totalmente dependiente de model, ya que es el encargado de crear un menu para controlar las funcionalidades que hay en model.

<img src="./readme_pictures/diagrama_componentes_pydevops.png">

