def fill_string(key_name):
    input_valid = False
    while not input_valid:
        try:
            value = input(key_name + ": ").strip()
            input_valid = True

        except ValueError:
            print('Invalid Input. price must be a string.')
    return value

