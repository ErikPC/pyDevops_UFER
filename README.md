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

Nuestro programa principal de compone de tres elementos esenciales y un cuarto que es el dedicado a la Static site gen:

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

## Clockify

A continuación se mostrarán las horas invertidas en el proyecto, separada en sus respectivas asignaturas.

<img src="./readme_pictures/clockify.PNG">

## Frontend

La página web se encuentra el la carpeta src/view/minimal donde se aprecia la estructura de directorios de Hugo.

En nuestro caso, creamos el tema desde cero y todavía necesita ser mejorado.

Hicimos cambios en el config.toml para poder renderizar html dentro de los archivos markdown dentro del directorio content, además de especificar las amenities como taxonomies.

Respecto al esqueleto de la página, en el directorio layouts encontramos _default, partials, services y el archivo index.html

El archivo index.html hace referencia a partials/pagecontent.html donde se muestra el contenido de la página y el título usando variables (.Cotent y .Title) de Hugo entre {{}}.

En _default se definen los esqueletos de las páginas de tipo single y de tipo list además de la base de todos los html de las páginas de la web.

En baseof.html se definen el head, el nav, el body, el main y el footer. Donde se usan variables de Hugo para definir un title diferente en cada página. También se define el main y el footer recibe el año en que nos encontramos (particularidad de Hugo para determinar el año en que nos encontramos)

En single.html se define la base del html en cada página de contenido que no sea de servicios de ufos. 
Simplemente se visualiza el contenido de la página de los archivos markdown.

En list.html se renderiza el html para las páginas que listan los servicios ofrecidos en la web, donde se aprovecha la lógica de Hugo para hacer un bucle sobre todos los títulos de los contenidos para mostrar los servicios en un menú vertical.

En services/single.html se enseña una lista con todos los servicios al igual que en list.html, además de enseñar el contenido de los ficheros markdown situados en la carpeta content/services

En la página de amenities, 

Finalmente tenemos la carpeta content, donde encontramos el contenido de la web.

_index.md hace referencia al contenido de la página index que nos aparece la primera al lanzar Hugo.

En review.md la idea era hacer un formulario para enviar datos a la base de datos para valorar los servicios, por lo tanto todavía está en proceso.

Y en services encontramos todos los servicios de ufos que se ofrecen en la página en forma de ficheros markdown.


