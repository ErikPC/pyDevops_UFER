
# the file name will always be the service returned when we update the price in the database
# the destiny in our app will be 'view/minimal/content/services/' if we run it from main.py
# file type will be .md cause our app consume markdown files
# the info will be a dict

def update_service_price(info, destination, file_type):

    if info is not None:

        # open file in read mode
        try:
            file = open(destination + info['name'] + file_type, "r")

        except FileNotFoundError:
            print('file not found')

        else:
            replacement = ''

            # loop through the file
            for line in file:
                line = line.strip()
                changes = line.replace(str(info['current_price']), str(info['new_price']))
                replacement = replacement + changes + "\n"

            file.close()

            # open file in write mode
            fout = open(destination + info['name'] + file_type, "w")
            fout.write(replacement)
            fout.close()
            return True
    else:
        return False



