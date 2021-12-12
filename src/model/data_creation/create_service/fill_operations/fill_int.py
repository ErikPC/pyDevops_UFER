def fill_int(key_name):
    input_valid = False
    while not input_valid:
        try:
            value = int(input(key_name + ": ").strip())
            if value > 0:
                input_valid = True
            else:
                print('Invalid input, %s must be greater than 0' % key_name)

        except ValueError:
            print('Invalid Input. %s must be an int' % key_name)
    return value
