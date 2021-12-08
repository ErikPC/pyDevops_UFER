from src.model.data_extraction.values_extraction import get_values
from src.model.service_selection.select_service.select_service import select_service
from pymongo.errors import OperationFailure


def update_price(collection):

    # get all services
    services = get_values(collection, 'name')

    # print all services
    print('servicios disponibles:', services)

    # select service
    service = select_service(services)

    # where to do the operation
    query = {"name": service}

    while True:

        try:
            input_value = int(input("select the new price: "))
            break

        except ValueError:
            print('Invalid Input. price must be an int.')

    # filter
    new_price = {"$set": {"price": input_value}}

    # operation to the collection
    try:
        collection.update_one(query, new_price)
    except OperationFailure:
        print("Operation error, price not updated successfully")
        return False
    else:
        print("price updated successfully!")
        return True
