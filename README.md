# pyDevops_UFER

---

# Introducción

Tu tutor de empresa quiere aprovechar que has llegado para intentar implementar un sistema de integración y entrega contínua (CI /CD), así que se sienta contigo a hacer una documentación técnica (es decir, unos garabatos en el papel donde venían las panades de carn amb pèsols del berenar) según se le va ocurriendo la solución (ver figura). El diagrama viene a decir algo así:

- Te propone que desarrolles una aplicación Python para extraer los datos de MongoAtlas. Se hace necesario diseñar una especificación del esquema de los documentos JSON.
- Esos documentos JSON tendrás que transformarlos, también con una aplicación Python, en ficheros Markdown.
- Luego, has de situar estos ficheros en una estructura de directorios que establece el generador de sitios estáticos llamado “Hugo”, también mediante una aplicación Python que construyas.
- Hugo, al arrancar, leerá los ficheros Markdown y los transformará en documentos HTML para servirlos en la “nueva web”.Tu tutor no ha usado nunca Hugo ni ningún otro generador de sitios estáticos, pero quieren que alguien aprenda a usarlo para evaluar su implantación en la intranet de la empresa.
- Tendrás que customizar los estilos CSS que utiliza Hugo para darle la presentación adecuada.

# Metodología

La metodología usada para este proyecto fue la kanban.

Esta metodología es muy sencilla, se puede actualizar y los equipos de trabajo la pueden asumir sin problema. Al ser un método visual permite que con un simple vistazo se conozca el estado de los proyectos y se puedan asignar nuevas tareas de manera muy efectiva. Para aplicarlo, es necesario un tablero de tareas con el que poder mejorar el trabajo y tener un ritmo sostenible.

En nuestro caso, nos hemos guiado por las historias de usuario y en base a estas hemos ido desarrollando pequeñas tareas que aportaran valor a cada historia y permitieran completarlas.

Nos aprovechamos del apartado project del proyecto, ya que Github te deja gestionar el proyecto de múltiples maneras:

![kanban](readme_pictures/kanban.png)

# Análisis

## Primer diagrama

![diagrama inicial](readme_pictures/análisis%20inicial.png)

La primera idea fue la siguiente:

Desde el módulo Main, se puede realizar la conexión a la base de datos, visualizar la página web y un módulo que iba a controlar la lógica de Model.

Respecto a Model, encontramos dos bloques diferenciados:

- Generate pages: crea páginas a renderizar por el SSG Hugo
  - Read: lee los documentos json de la colección y los pasa a markdown
- Acceso a datos:
  - Delete: elimina los items de la BBDD
  - Create: crea los items de la BBDD
  - Update: actualiza los items de la BBDD

## Posibles tecnologías

La principal funcionalidad es generar archivos Markdown con los datos almacenados en la base de datos MongoAtlas en el Static site generator Hugo. A continuación se especifícan las tecnologías utilizadas.

Principalmente, la aplicación gira entorno a una base de datos (BBDD), Mongodb. Mongodb es un sistema de BBDD NoSQL, orientado a documentos y de código abierto. En lugar de guardar los datos en tablas, tal y como se hace en las bases de datos relacionales, MongoDB guarda estructuras de datos BSON. Para ser más específico, se han realizado las consultas en MongoAtlas, un servicio en la nube de Mongodb.

Los datos plasmados estaban escritos en un Static site generator, el que nos indicaron usar era Hugo. Hugo es uno de los generadores de sitios estáticos de código abierto más populares. Con su asombrosa velocidad y flexibilidad.

El editor de codigo que podiamos elegir fueron VsCode, pycharm o sublime text, aunque teniamos más opciones estas fueron las pensadas.

La aplicación ha sido desarrollada con el lenguaje de programacion python version 3.9 . Para crear el programa se han tenido que instalar las siguientes dependencias:

- Para realizar los test sobre los módulos del programa hemos usado pytest version 6.2.5.
- La conexión con la base de datos tuvimos que instalar la librería de pymongo version 3.12.1.
- Para la conexión a la BBDD con pymongo tuvimos que añadir certifi para la conexión SSL.
- Para la validación del schema se ha instalado el módulo jsonchema.

## tabla de tecnologías

https://www.tablesgenerator.com/markdown_tables

| tecnologías   | requisitos | 1 <br> almacenar datos de los items | 2 <br> extraer datos de los items | 3 <br> transformar json a markdown | 4 <br> almacenar contenido de los items | 5 renderizar páginas | 6 customizar estilos | 7 <br> testear la aplicación |
| ------------- | ---------- | ----------------------------------- | --------------------------------- | ---------------------------------- | --------------------------------------- | -------------------- | -------------------- | ---------------------------- |
| MongoDB Atlas | 1          | :heavy_check_mark:                  | :x:                               | :x:                                | :x:                                     | :x:                  | :x:                  | :x:                          |
| python        | 1          | :heavy_check_mark:                  | :heavy_check_mark:                | :heavy_check_mark:                 | :x:                                     | :x:                  | :x:                  | :x:                          |
| pymongo       | 2          | :x:                                 | :heavy_check_mark:                | :x:                                | :x:                                     | :x:                  | :x:                  | :x:                          |
| Markdown      | 4          | :x:                                 | :x:                               | :x:                                | :heavy_check_mark:                      | :x:                  | :x:                  | :x:                          |
| HTML 5        | 4          | :x:                                 | :x:                               | :x:                                | :heavy_check_mark:                      | :x:                  | :x:                  | :x:                          |
| Hugo          | 5          | :x:                                 | :x:                               | :x:                                | :heavy_check_mark:                      | :heavy_check_mark:   | :x:                  | :x:                          |
| CSS 3         | 6          | :x:                                 | :x:                               | :x:                                | :x:                                     | :x:                  | :heavy_check_mark:   | :x:                          |
| pytest        | 7          | :x:                                 | :x:                               | :x:                                | :x:                                     | :x:                  | :x:                  | :heavy_check_mark:           |

# Diseño

## Diagrama de componentes

<img src="./readme_pictures/diagrama_componentes_pydevops.png">

Nuestro programa principal de compone de tres elementos esenciales y un cuarto que es el dedicado al SSG Hugo:

- repository
- model
- controller
- view

### repository

Aquí tenemos el módulo db_conection, es el que se encarga de establecer la conexión con la base de datos.

### model

Se centra en el CRUD "Crear, Leer, Actualizar y Borrar" de la BBDD. Por eso lo vinculamos con repository. También almacenando otras utilidades que le ayuda a realizar dichas actividades.

En este módulo tenemos un módulo para verificar los datos y uno que usaremos para seleccionar los servicios.

- service_selection
- data_validation

Los módulos,que dependen de repository ya que la conexión con la BBDD es necesaria, realizarán el CRUD son:

- data_extraction: para leer los datos, aparte contiene la funcionalidad de pasar los datos para ser visualizados en el Static site generator.
- data_creation: este módulo pide al usuario los datos para crear un documento en la BBDD
- data_deletion: es el encargado de eliminar los datos del usuario.
- data_updation: se encarga de actualizar los datos de la BBDD

Aparte encontramos los módulos encargados de usar los datos de la BBDD en Hugo:

- contente_generation: depende de los datos extraidos, se encargará de generar los archivos que se visualizarán en Hugo.
- content_deletion: se encarga de cuando se eliminen los datos , actualice la página y desaparezca la página dedicada a ese item
- content_updation: es la encargada de que cuando se cambien los datos de un item sean actualizados en el archivo de Hugo.

### view

El repositorio view, contiene todo lo necesario para iniciar Hugo con su configuración correspondiente. Por este motivo View depende de todos los módulos content, ya que son los que hacen que se actualice y genere la información de la página.

### controller

El controller es totalmente dependiente de model, ya que es el encargado de crear un menu para controlar las funcionalidades que hay en model.

## Esquema de BBDD

```python
{
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "description": {"type": "string"},
        "driver": {"type": "string"},
        "passengers": {"type": "number"},
        "privacy": {"type": "string"},
        "seats": {"type": "string"},
        "propulsion": {"type": "string"},
        "top_speed": {"type": "number"},
        "price": {"type": "number"},
        "amenities": {"type": "array"}
    }
}
```
Los documentos que no cumplan el siguiente schema no serán insertados y se lanzará un mensaje al usuario por consola informando de la invalidez del documento.

## Futuras Pruebas

Las pruebas seleccionadas principalmente son sobre el CRUD de la aplicación.

Se probara como se elimina un item de la base de datos, como se actualizará un documento en la base de datos y como se creará un documento.

Además, se usarán markers personalizados para hacer tests unitarios de cada módulo.

En el fichero pytest.ini se encuentran todos los markers.

También se harán tests de regresión para comprobar que los tests ya pasados siguen pasando.

# Implementación

## Herramientas técnicas

Como hemos comentado anteriormente, hemos acabado usando vscode por su ayuda con las extensiones a la hora de escribir el código y pycharm frente a la gestión de la infraestructura y el manejo de los módulos, además de las facilidades aportadas en relación al entorno virtual y la implementación de código de calidad según PEP 8.

Los módulos python comentados en el apartado de posibles tecnologías finalmente fueron utilizados para la conexión de la base de datos y la validación del schema.

## Backend

Lo encontramos en los módulos dentro de Model.

Los referentes a content se encargan para actualizar los directorios de Hugo:

- content-deletion: en el momento en que se elimine un item de la base de datos, también lo hará en el sitio web.

```python

def delete_service(service):

    # tell the user which service wants to delete
    # input('Service to delete: ').strip().title()
    service_to_delete = service

    if file_exists(destiny, service_to_delete, file_type):
        os.remove(destiny + service_to_delete + file_type)
    else:
        print("The service doesn't exists")


```

- content_generation: genera los archivos markdown en el directorio de contenido de Hugo para que los items sean visualizados.

```python
def generate_files(collection):
    # counter for every file added
    counter = 0
    # list of dicts (ufer data)
    ufer_docs = load_data(collection)

    for index, doc in enumerate(ufer_docs):

        if not file_exists(destiny, doc['name'], file_type):

            template = generate_template(ufer_docs, index)

            with open(destiny + doc['name'] + file_type, 'w', encoding='UTF-8') as my_file:
                counter += 1
                my_file.writelines(template)

    # items added
    if counter == 0:
        print('content already up to date')
    else:
        print('items added to the website:', counter)
```

- content_updation: en este módulo se actualiza el precio del item de la pagina seleccionado

```python
def update_service_price(info, destination, file_type):

    if info is not None:

        # open file in read mode
        try:
            file = open(destination + info['name'] + file_type, "r")

        except FileNotFoundError:
            print('file not found')

        else:
            replacement = ''

            # loop through the file
            for line in file:
                line = line.strip()
                changes = line.replace(str(info['current_price']), str(info['new_price']))
                replacement = replacement + changes + "\n"

            file.close()

            # open file in write mode
            fout = open(destination + info['name'] + file_type, "w")
            fout.write(replacement)
            fout.close()
            return True
    else:
        return False
```

En cuanto a los módulos data, son los que representan el CRUD a la BBDD:

- data_creation (C):

```python
def create_service(collection):
    # generate empty_values document
    document = {
        "name": "",
        "description": "",
        "driver": "",
        "passengers": 0,
        "privacy": "",
        "seats": "",
        "propulsion": "",
        "top_speed": 0,
        'price': 0,
        "amenities": []
    }

    user_instructions = "Para crear un servicio, sigue el siguiente schema:\n" "\n \t\"name\": \"\"," \
                        "\n\t\"description\": \"\",\n\t" "\"driver\": \"\",\n\t\"passengers\": \"\"," \
                        "\n\t\"privacy\": \"\",\n\t\"seats\": \"\",\n\t\"propulsion\": ""\"\",\n\t\"top_speed\": " \
                        "0,\n\t\"amenities\": []\n\t  "

    # tell the user how to fill the values
    print(user_instructions)

    # fill document values (depending on the value type it has)
    for index in range(len(PYDEVOPS_KEYS)):
        if PYDEVOPS_VALUE_TYPES[index] == str:
            if PYDEVOPS_KEYS[index] == 'name':
                document[PYDEVOPS_KEYS[index]] = fill_string(PYDEVOPS_KEYS[index]).title()
            else:
                document[PYDEVOPS_KEYS[index]] = fill_string(PYDEVOPS_KEYS[index])
        elif PYDEVOPS_VALUE_TYPES[index] == int:
            document[PYDEVOPS_KEYS[index]] = fill_int(PYDEVOPS_KEYS[index])
        elif PYDEVOPS_VALUE_TYPES[index] == list:
            document[PYDEVOPS_KEYS[index]] = fill_array()

     # schema validation
    if validate_schema(document):

        try:
            new_document_id = collection.insert_one(document)
        except OperationFailure:
            print('the insert operation failed')
        else:
            print('insertion done successfully')
            return new_document_id
    else:
        return False
```

Se recorren las variables globales que almacenan las claves y los valores del schema y en función del tipo de dato se usan diferentes operaciones para llenar los valores del documento a enviar a la BBDD. Después se valida el schema y se inserta el documento llenado a la colección.

- data_extraction (R):

```python
def load_data(collection):
    documents = []

    try:
        for item in collection.find({}, {'_id': False}):
            if validate_schema(item):
                documents.append(item)
    except OperationFailure:
        print("load_data operation failed")
    else:
        return documents

```

En este módulo se extraen los documentos de la colección y se almacenan en una lista de diccionarios para poder ser tratados posteriormente y generar su contenido en la página si todavía no se encuentran en ella.

- data_updation (U):

```python
def get_price(collection, service):

    service_price = 0

    try:
        for doc in collection.find({}, {'_id': False}):
            if doc['name'] == service:
                service_price = doc['price']

    except OperationFailure:
        print("get_price operation failed")
    else:
        return service_price

def update_price(collection):

    # get all services
    services = get_values(collection, 'name')

    # print all services
    print('servicios disponibles:', services)

    # select service
    service = select_service(services)

    # where to do the operation
    query = {"name": service}

    # show current price
    current_price = get_price(collection, service)
    print('current price:', current_price)

    # get new price
    while True:

        try:
            input_value = int(input("select the new price: "))
            if input_value != current_price and input_value > 0:
                break
            else:
                print('Price must be diferent from the current one and greater than 0!')

        except ValueError:
            print('Invalid Input. price must be an int.')

    # what to update
    new_price = {"$set": {"price": input_value}}

    # update operation
    try:
        collection.update_one(query, new_price)
    except OperationFailure:
        print("Operation error, price not updated successfully")
        return None
    else:
        print("price updated successfully!")
        return {
            'name': service,
            'current_price': current_price,
            'new_price': input_value
        }
```

Se usan dos módulos. Uno para obtener el precio actual del item en la BBDD y otro para seleccionar el nuevo precio y actualizarlo.

- data_deletion (D):

```python
def delete_data(collection):
    # get all services
    servicios = get_values(collection,'name')

    # print all services
    print('servicios disponibles:', servicios)

    # delete document from the database
    servicio_eliminar = input("Escribe el servicio que quieres eliminar: \n").strip().title()
    confirm = input("Vuelve a escribir el servicio: \n").strip().title()

    if servicio_eliminar != confirm:
        print("Los servicios no coinciden")

    elif servicio_eliminar in servicios:

        try:
            collection.delete_one({"name": servicio_eliminar})
        except OperationFailure:
            print("La operación ha fallado")
        else:
            print("Servicio eliminado correctamente")
            return servicio_eliminar

    else:
        print("item no encontrado")
        return None
```

En este módulo se pide el item a eliminar y su confirmación. Si este no completa la confirmación, no se elimina de la base de datos.

- validación del schema:

```python
def validate_keys(schema_to_validate):
    assert isinstance(schema_to_validate, dict)
    is_valid = False
    counter = 0
    print("validating schema keys...")

    for key in schema_to_validate.keys():

        if key not in PYDEVOPS_KEYS:
            is_valid = False
            print("the schema has an invalid key")
            return is_valid
        else:
            counter += 1

    # the document doesn't have all required keys
    if counter < len(PYDEVOPS_KEYS):
        is_valid = False
        print("The schema does't have all the required keys")
    else:
        is_valid = True

    return is_valid
```

En este módulo se chequea que las claves sean las esperadas y que no se deje a ninguna de ellas.

```python
from jsonschema import validate
from jsonschema.exceptions import ValidationError

correct_schema = {

    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "description": {"type": "string"},
        "driver": {"type": "string"},
        "passengers": {"type": "number"},
        "privacy": {"type": "string"},
        "seats": {"type": "string"},
        "propulsion": {"type": "string"},
        "top_speed": {"type": "number"},
        "price": {"type": "number"},
        "amenities": {"type": "array"}
    }
}


def validate_value_types(schema_to_validate):
    print("validating schema value types...")
    try:
        validate(instance=schema_to_validate, schema=correct_schema)

    except ValidationError:
        print("invalid value type")
    else:
        return True
    return False
```

En este otro, se comprueba que los valores sean del tipo correcto. Como podemos apreciar, se ha hecho uso de la librería jsonschema.

## Arquitectura y tecnologias usadas

### Arquitectura de la app

<img src="./readme_pictures/arquitectura_por_capas_pydevops.png">

La arquitectura de la aplicación se divide en tres capas y una entidad diferenciada:

- Capa de presentación: donde se muestra la página y el usuario interactua con el controlador.

- Capa de Dominio / Negocio: donde reside la lógica de la aplicacion.

- Capa de acceso a datos: la capa que accede a los datos almacenados en una base de datos en la nube.

- MongoDB Atlas: es la base de datos en la nube sobre la cual interactua la aplicación.

los schema se ha instalado el módulo jsonchema.

## Frontend

La página web se encuentra el la carpeta src/view/minimal donde se aprecia la estructura de directorios de Hugo.

En nuestro caso, creamos el tema desde cero y todavía necesita ser mejorado.

Hicimos cambios en el config.toml para poder renderizar html dentro de los archivos markdown dentro del directorio content, además de especificar las amenities como taxonomies.

```toml
[taxonomies]
  amenity = 'amenities'
```

Esto se pudo conseguir debido a que se especificaron en el frontmatter de cada página de contenido. Como por ejemplo en la página del servicio Ufer Bus:

```yaml
title: "Ufer Bus"
draft: false
amenities: ["WiFi", "Water", "Snacks", "Beer", "TV"]
```

Respecto al esqueleto de la página, en el directorio layouts encontramos \_default, partials, services y el archivo index.html

El archivo index.html hace referencia a partials/pagecontent.html donde se muestra el contenido de la página y el título usando variables (.Cotent y .Title) de Hugo entre {{}}.

En \_default se definen los esqueletos de las páginas de tipo single y de tipo list además de la base de todos los html de las páginas de la web.

En baseof.html se definen el head, el nav, el body, el main y el footer. Donde se usan variables de Hugo para definir un title diferente en cada página. También se define el main y el footer recibe el año en que nos encontramos (particularidad de Hugo para determinar el año en que nos encontramos)

En single.html se define la base del html en cada página de contenido que no sea de servicios de ufos.
Simplemente se visualiza el contenido de la página de los archivos markdown.

En list.html se renderiza el html para las páginas que listan los servicios ofrecidos en la web, donde se aprovecha la lógica de Hugo para hacer un bucle sobre todos los títulos de los contenidos para mostrar los servicios en un menú vertical.

![menu vertical](readme_pictures/menu_services.png)

En services/single.html se enseña una lista con todos los servicios al igual que en list.html, además de enseñar el contenido de los ficheros markdown situados en la carpeta content/services

![service page](readme_pictures/service_page.png)

En la página de amenities, se generan las categorias de los items que se añaden.

![amenities list](readme_pictures/amennities.png)

Finalmente tenemos la carpeta content, donde encontramos el contenido de la web.

\_index.md hace referencia al contenido de la página index que nos aparece la primera al lanzar Hugo.

![index](readme_pictures/index.png)

En review.md la idea era hacer un formulario para enviar datos a la base de datos para valorar los servicios, por lo tanto todavía está en proceso.

Y en services encontramos todos los servicios de ufos que se ofrecen en la página en forma de ficheros markdown.

## Pruebas

Para hacer las pruebas nos creamos una colección para realizar CRUD sobre sus documentos. También usamos la librería pytest para hacer los tests unitarios de los módulos.

Con pytest usamos custom markers para lanzar los tests individualmente con su nombre representativo (unit tests) y además lanzamos los tests sin los markers para comprobar que los anteriores ya pasados seguían pasando (tests de regresión).

```ini
[pytest]
markers =
    test_create_service
    test_delete_data
    test_validate_keys
    test_validate_value_types
    test_validate_schema
    test_select_service
    test_file_exists
    test_fill_array
    test_fill_string
    test_fill_int
    test_update_price

```

aquí tenemos los markers utilizados

![collections](readme_pictures/collections.png)

y aquí la BBDD con las colecciones con las que hicimos pruebas y la definitiva para almacenar los servicios fue "ufer".

Respecto a los tests, aquí tenemos un ejemplo de uno:

```python
import pytest
from src.model.content_updation.update_price import update_service_price

# route: test_files/name_file.file_type

route = 'test_files/'
file_type = '.md'

# valid info
info1 = {
    'name': 'Ufer Bacon',
    'current_price': 30,
    'new_price': 20
}

# valid info
info2 = {
    'name': 'Ufer Spam',
    'current_price': 40,
    'new_price': 50
}

# invalid info
info_bad = {
    'name': 'Ufer Loco',
    'current_price': 40,
    'new_price': 50
}

# None info
info3 = None


@pytest.mark.test_update_price
def test_update_price():
    assert update_service_price(info1, route, file_type) == True
    assert update_service_price(info2, route, file_type) == True
    assert update_service_price(info3, route, file_type) == False
    assert update_service_price(info_bad, route, file_type) is None

```

Puntos a tener en cuenta:

- Se usan los decoradores para indicar que el test va a ser llamado desde pytest a través del marker que se le ha asignado, previamente configurado en el archivo de configuración pytest.ini

- Se usan aserciones para comprobar la validez de los tests. Si alguna no se cumple, el programa termina su ejecución indicando donde no se cumple la condición.

- Se ha creado un directorio al mismo nivel con archivos markdown para actualizar su precio. Si este se actualiza, nos devuelve un booleano True, si el archivo no existe nos devuelve el objeto None y si no se pasa ninguna información para actualizar nos devuelve el booleano False.

Para hacer las operaciones de CRUD se han usado los bloques try/except para capturas excepciones en tiempo de ejecución para poder retomar el flujo normal del programa. Como por ejemplo si falla una operación de inserción en la colección el programa no termina su ejecución:

```python
try:
            new_document_id = collection.insert_one(document)
        except OperationFailure:
            print('the insert operation failed')
        else:
            print('insertion done successfully')
            return new_document_id
```

## Pruebas sobre CRUD

### C

- Lista capturas Joan: 
    - En la base de datos , antes de la actualizacion y despues de cambiar el precio
    - En la base de datos , un item y despues de eliminarlo.

### R

La idea del read esta centrada en visualizar los datos de la BBDD en Hugo.

Funcionamiento de read:

<img src="./readme_pictures/read_pruebas_bbdd.PNG" width =45%>
<img src="./readme_pictures/read_pruebas.PNG" width = 45%>

### U

En el update lo que hacemos es modificar un precio , ya que es lo más probable de que cambie.

El código que usamos es:

Primero creamos una funcion que coge el precio de un item:

```python
def get_price(collection, service):

    service_price = 0

    try:
        for doc in collection.find({}, {'_id': False}):
            if doc['name'] == service:
                service_price = doc['price']

    except OperationFailure:
        print("get_price operation failed")
    else:
        return service_price
```

Posteriormente se usa en la que actualizaremos el precio.

```python

def update_price(collection):

    # get all services
    services = get_values(collection, 'name')

    # print all services
    print('servicios disponibles:', services)

    # select service
    service = select_service(services)

    # where to do the operation
    query = {"name": service}

    # show current price
    current_price = get_price(collection, service)
    print('current price:', current_price)

    # get new price
    while True:

        try:
            input_value = int(input("select the new price: "))
            if input_value != current_price and input_value > 0:
                break
            else:
                print('Price must be diferent from the current one and greater than 0!')

        except ValueError:
            print('Invalid Input. price must be an int.')

    # what to update
    new_price = {"$set": {"price": input_value}}

    # update operation
    try:
        collection.update_one(query, new_price)
    except OperationFailure:
        print("Operation error, price not updated successfully")
        return None
    else:
        print("price updated successfully!")
        return {
            'name': service,
            'current_price': current_price,
            'new_price': input_value
        }
```

Una vez seleccionado el servicio a modificar, nos aseguramos que el valor introducido sea un entero mayor que cero para respetar el esquema.
Con la siguiente función hacemos que cambie el dato que se acaba de actualizar en la BBDD en Hugo.

```python
def update_service_price(info, destination, file_type):

    if info is not None:

        # open file in read mode
        try:
            file = open(destination + info['name'] + file_type, "r")

        except FileNotFoundError:
            print('file not found')

        else:
            replacement = ''

            # loop through the file
            for line in file:
                line = line.strip()
                changes = line.replace(str(info['current_price']), str(info['new_price']))
                replacement = replacement + changes + "\n"

            file.close()

            # open file in write mode
            fout = open(destination + info['name'] + file_type, "w")
            fout.write(replacement)
            fout.close()
            return True
    else:
        return False
```

Funcionamiento del Update:


<img src="readme_pictures/update_pruebas_bbdd1.PNG">
<img src ="./readme_pictures/update_pruebas1.PNG">
<img src ="./readme_pictures/update_pruebas2.PNG">
<img src="./readme_pictures/update_pruebas_bbdd2.PNG">

### D

Con el delete lo que hacemos es eliminar un item de la base de datos y automaticamente eliminarlo de Hugo.

Con el siguiente modulo eliminamos de la base de datos un item de los que le enseñamos. Que son los que estan en la pagina. Pasando por una confirmacion de si es ese item , para no eliminarlo por error.

```python

def delete_data(collection):
    # get all services
    servicios = get_values(collection,'name')

    # print all services
    print('servicios disponibles:', servicios)

    # delete document from the database
    servicio_eliminar = input("Escribe el servicio que quieres eliminar: \n").strip().title()
    confirm = input("Vuelve a escribir el servicio: \n").strip().title()

    if servicio_eliminar != confirm:
        print("Los servicios no coinciden")

    elif servicio_eliminar in servicios:

        try:
            collection.delete_one({"name": servicio_eliminar})
        except OperationFailure:
            print("La operación ha fallado")
        else:
            print("Servicio eliminado correctamente")
            return servicio_eliminar

    else:
        print("item no encontrado")
        return None
```

```python
def delete_service(service):

    # tell the user which service wants to delete
    # input('Service to delete: ').strip().title()
    service_to_delete = service

    if file_exists(destiny, service_to_delete, file_type):
        os.remove(destiny + service_to_delete + file_type)
    else:
        print("The service doesn't exists")
```

Funcionamiento de Deletion:

<img src="./readme_pictures/delete_pruebas_bbdd1.PNG">
<img src="./readme_pictures/delete_pruebas1.PNG">
<img src="./readme_pictures/delete_pruebas2.PNG">
<img src="./readme_pictures/delete_pruebas3.PNG">
<img src="./readme_pictures/delete_pruebas_bbdd2.PNG">

## Comparación temporal con Clockify

En el primer momento hicimos un tiempo estimado de cuanto ibamos a invertir en cada modulo:

<img src="./readme_pictures/clockify_primer_tiempo.PNG">

En un primer momento pensabamos que solo teniamos que pasar los items de la BBDD y añadirlos a la pagina , posteriormente como añadimos el CRUD al completo, se alargaron la horas.

A continuación se mostrarán las horas invertidas en el proyecto, separada en sus respectivas asignaturas.

<img src="./readme_pictures/clockify.PNG">

## Dificultades

En cuanto a las dificultades:

- Aprender a usar Hugo e indagar en su documentación. Nos sirvió bastante el libro "Build Websites with Hugo: Fast Web Development with Markdown", además del curso de youtube de Mike Dane https://www.youtube.com/watch?v=qtIqKaDlqXo y la documentación oficial de Hugo en https://gohugo.io/

- Hacer testing de los inputs de usuario ya que era necesario mockear los inputs y desconociamos como hacerlo.

- El tiempo para realizar el proyecto no fue suficiente para cumplir todos los objetivos en mente.

- Hacer tests de integración de los módulos que juntaban varios submódulos.

## Futuras mejoras

De momento son las siguientes:

1. Añadir un formulario para mejorar la usabilidad de la app
2. Añadir una interfaz gráfica con Tkinter (librería de python) para no depender de un formulario externo
3. Añadir la funcionalidad de actualizar mas campos de los servicios, ya que solo se puede actualizar el precio
4. Automatizar la eliminación de las amenities que hagan referencia a un servicio no disponible en la página
5. Mejorar la UI de la página
6. Hacer uso de la librería 'typer' de python para manejar los inputs de usuario con mayor profesionalidad
