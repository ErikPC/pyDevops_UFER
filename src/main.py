from src.repository.db_connection.connect_db import connect_db
from src.controller.controller import controller

# represents the current documents in the db as dicts in a list
documents = list()

# represents the current names of the services as dicts in a list
services = list()

# get the database
database = connect_db()

# get the collections
UFER = database.ufer
REVIEWS = database.reviews

# here the user specify the operation to perform
controller(UFER)