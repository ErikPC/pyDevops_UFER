from src.model.data_validation.validate_schema import validate_schema


def load_data(collection):
    documents = []
    for item in collection.find({}, {'_id': False}):
        if validate_schema(item):
            documents.append(item)
    return documents

