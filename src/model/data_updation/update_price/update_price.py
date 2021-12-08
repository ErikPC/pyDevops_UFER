from src.model.data_extraction.values_extraction import get_values
from src.model.service_selection.select_service.select_service import select_service
from src.model.data_updation.update_price.get_price import get_price
from pymongo.errors import PyMongoError


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
    except PyMongoError:
        print("Operation error, price not updated successfully")
        return False
    else:
        print("price updated successfully!")
        return True
