import pymongo
import certifi
from src.repository.db_connection.config_params import PYDEVOPS_URI as URI
from pymongo.errors import ServerSelectionTimeoutError
from pymongo.errors import ConnectionFailure
from pymongo.errors import CertificateError


def connect_db():

    # necessary ssl certificate
    ca = certifi.where()

    try:
        client = pymongo.MongoClient(URI, tlsCAFile=ca)

    except (ServerSelectionTimeoutError, ConnectionFailure):
        print("cannot connect to the database")
    except CertificateError:
        print("cannot connect to the database, valid ssl certificate needed")

    else:
        database = client.pydevops
        return database
