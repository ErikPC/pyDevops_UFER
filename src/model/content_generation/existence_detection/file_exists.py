import os.path


def file_exists(route, file_name, file_type):
    if os.path.isfile(route + file_name + file_type):
        print(file_name, 'service already in the website')
        return True
    else:
        print(file_name, 'service not in the website')
        return False

