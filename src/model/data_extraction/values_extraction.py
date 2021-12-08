from pymongo.errors import PyMongoError


def get_values(collection, key):
    values = []
    try:
        for item in collection.find({}, {'_id': False}):
            values.append(item[key])
    except PyMongoError:
        print("operation get_values failed")
    else:
        return values
