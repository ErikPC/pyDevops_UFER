from pymongo.errors import CollectionInvalid


def get_collection(database, my_col):
    try:
        my_col = database.mycol
    except CollectionInvalid:
        print("the selected collection doesn't exists in the database")
    else:
        return my_col

