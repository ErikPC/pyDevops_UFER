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
        collection.delete_many({"services": servicio_eliminar})
        print("Se ha eliminado correctamente")
    else:
        print("item no encontrado")

