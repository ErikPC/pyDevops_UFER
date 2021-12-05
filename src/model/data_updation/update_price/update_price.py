from src.main import UFER


def update_price(service):
    query = {"name": service}

    while True:

        try:
            input_value = int(input("select the new price: "))
            break

        except ValueError:
            print('Invalid Input. price must be an int.')

    new_price = {"$set": {"price": input_value}}
    UFER.update_one(query, new_price)

