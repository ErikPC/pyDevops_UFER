from src.model.data_validation.validate_schema import validate_schema
from pymongo.errors import OperationFailure


def load_data(collection):
    documents = []

    try:
        for item in collection.find({}, {'_id': False}):
            if validate_schema(item):
                documents.append(item)
    except OperationFailure:
        print("load_data operation failed")
    else:
        return documents
