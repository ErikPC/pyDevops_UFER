from pymongo.errors import OperationFailure


def get_values(collection, key):
    values = []
    try:
        for item in collection.find({}, {'_id': False}):
            values.append(item[key])
    except OperationFailure:
        print("operation get_values failed")
    else:
        return values
