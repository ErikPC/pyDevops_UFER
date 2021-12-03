

def enseñar_items(database):
    #     keys = ['nombre', 'edad', 'deportes']
    for item in collection.find({}, {'_id': False}):
        pass
#     while selector == True:
#         key_entrada = input("Escribe la key quieres filtrar / si no quieres escribe fin")
#         if key_entrada in keys:
#             collection.find({key_entrada})
#             break
#         selector = False


def delete_data(collection):
    documentos = collection.find({"services": {"$exists": True}})
    servicios = []
    for item in documentos:
        print(item)
        servicios.append(item["services"])
    servicio_eliminar = input("Escribe el servicio que quieres eliminar: \n")
    confirm = input("Vuelve a escribir el servicio: \n")
    if servicio_eliminar != confirm:
        print("Los servicios no coinciden")
    elif servicio_eliminar in servicios:
        database.delete_many({"services": servicio_eliminar})
        print("Se ha eliminado correctamente")
    else:
        print("item no encontrado")

