from pymongo.errors import OperationFailure


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
