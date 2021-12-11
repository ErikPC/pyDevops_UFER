
def load_data(collection):
    documents = []
    for item in collection.find({}, {'_id': False}):
        documents.append(item)
    return documents

