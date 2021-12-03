def enseñar_items(collection):
    for item in collection.find({}, {'_id': False}):
        print(item)