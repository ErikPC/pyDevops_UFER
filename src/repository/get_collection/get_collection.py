from pymongo.errors import CollectionInvalid


def get_collection(database):
    try:
        my_col = database.collection
    except CollectionInvalid:
        print("the selected collection doesn't exists in the database")
    else:
        return my_col

