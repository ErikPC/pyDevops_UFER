def generate_template(ufer_docs, index):

    assert isinstance(ufer_docs, list)

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

    return template
