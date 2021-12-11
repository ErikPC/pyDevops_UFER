from src.model.content_generation.template.template_config import destiny
from src.model.content_generation.template.template_config import file_type
from src.model.content_generation.existence_detection.file_exists import file_exists
from src.model.data_extraction.data_extraction import load_data
from src.main import UFER


def generate_files():

    # counter for every file added
    counter = 0
    # list of dicts (ufer data)
    ufer_docs = load_data(UFER)

    for index, doc in enumerate(ufer_docs):

        if not file_exists(destiny, doc[index]['name'], file_type):
            print('service not in the website')

            # generate a template for the file
            template = [
                '---',
                'title: ' + '"' + ufer_docs[index]['name'] + '"',
                'draft: false',
                '---',
                ufer_docs[index]['description'],
                'driver: ' + ufer_docs[index]['driver'],
                'passengers: ' + ufer_docs[index]['passengers'],
                'privacy: ' + ufer_docs[index]['privacy'],
                'seats: ' + ufer_docs[index]['seats'],
                'propulsion: ' + ufer_docs[index]['propulsion'],
                'top speed: ' + ufer_docs[index]['top_speed'],
                'price: ' + ufer_docs[index]['price'] + '$',
                'amenities: ' + ufer_docs[index]['amenities']
            ]

            # create a file
            my_file = open(destiny + doc[index]['name'] + file_type, 'w', encoding='UTF-8')
            counter += 1

            try:
                my_file.writelines(template)
            finally:
                my_file.close()
        else:
            print('service already in the website')

        if counter == 0:
            print('content already up to date')
