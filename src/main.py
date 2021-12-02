from src.repository.db_connection.connect_db import connect_db

# get the database
database = connect_db()

# get the collections
UFER = database.ufer
REVIEWS = database.reviews
