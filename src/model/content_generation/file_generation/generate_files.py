from src.model.content_generation.template.template_config import destiny
from src.model.content_generation.template.template_config import file_type
from src.model.content_generation.existence_detection.file_exists import file_exists
from src.model.data_extraction.data_extraction import load_data


def generate_files(collection):
    # counter for every file added
    counter = 0
    # list of dicts (ufer data)
    ufer_docs = load_data(collection)

    for index, doc in enumerate(ufer_docs):

        if not file_exists(destiny, doc['name'], file_type):
            print('service not in the website')

            # generate a template for the file
            template = [
                '---\n',
                'title: ' + '"' + ufer_docs[index]['name'] + '"\n',
                'draft: false\n',
                '---\n',
                ufer_docs[index]['description'] + '\n\n',
                'driver: ' + ufer_docs[index]['driver'] + '\n\n',
                'passengers: ' + str(ufer_docs[index]['passengers']) + '\n\n',
                'privacy: ' + ufer_docs[index]['privacy'] + '\n\n',
                'seats: ' + ufer_docs[index]['seats'] + '\n\n',
                'propulsion: ' + ufer_docs[index]['propulsion'] + '\n\n',
                'top speed: ' + str(ufer_docs[index]['top_speed']) + '\n\n',
                'price: ' + str(ufer_docs[index]['price']) + '$' + '\n\n',
                'amenities: ' + ', '.join((ufer_docs[index]['amenities'])) + '\n\n'
            ]

            # create a file
            my_file = open(destiny + doc['name'] + file_type, 'w', encoding='UTF-8')
            counter += 1

            try:
                my_file.writelines(template)
            finally:
                my_file.close()
        else:
            print('service already in the website')

        if counter == 0:
            print('content already up to date')
