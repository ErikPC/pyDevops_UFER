def get_values(collection, key):
    values = []
    for item in collection.find({}, {'_id': False}):
        values.append(item[key])
    return values

