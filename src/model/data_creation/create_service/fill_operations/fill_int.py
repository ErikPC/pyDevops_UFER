def fill_int(key_name):
    input_valid = False
    while not input_valid:
        try:
            value = int(input(key_name + ": ").strip())
            input_valid = True

        except ValueError:
            print('Invalid Input. %s must be an int' % key_name)
    return value
