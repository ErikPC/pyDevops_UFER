from src.model.content_generation.template.template_config import destiny
from src.model.content_generation.template.template_config import file_type
from src.model.content_generation.existence_detection.file_exists import file_exists
from src.model.data_extraction.data_extraction import load_data
from src.model.content_generation.template.generate_template import generate_template


def generate_files(collection):
    # counter for every file added
    counter = 0
    # list of dicts (ufer data)
    ufer_docs = load_data(collection)

    for index, doc in enumerate(ufer_docs):

        if not file_exists(destiny, doc['name'], file_type):

            template = generate_template(ufer_docs, index)

            my_file = open(destiny + doc['name'] + file_type, 'w', encoding='UTF-8')
            counter += 1

            try:
                my_file.writelines(template)
            finally:
                my_file.close()

    # items added
    if counter == 0:
        print('content already up to date')
    else:
        print('items added to the website:', counter)
