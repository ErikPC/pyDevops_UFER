from pymongo import MongoClient
from src.repository.db_connection.connect_db import connect_db
import pymongo
database = connect_db()
collection = database['pruebas']
# Cuenado esto funcione , hay que cambiar 'pruebas' por el nombre de de la coleccion definitiva
collection.insert_one(
    {
        'nombre': 'Joan',
        'edad': 20,
        'deportes': ['padel', 'futbol', 'boxeo']
    }
)


def enseñar_items(database):
    #     keys = ['nombre', 'edad', 'deportes']
    for item in collection.find({}, {'_id': False}):
        print(item)


#     while selector == True:
#         key_entrada = input("Escribe la key quieres filtrar / si no quieres escribe fin")
#         if key_entrada in keys:
#             collection.find({key_entrada})
#             break
#         selector = False
items = enseñar_items(database)


def delete_data(database):
    # items (funcion)
    # funcion de seleccionar servicio
    # comparar que el input esta bien escritos
    # eliminar item por servicio
