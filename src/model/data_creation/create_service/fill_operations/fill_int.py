def fill_int(key_name, value):
    while True:
        try:
            value = int(input(key_name + ": ").strip())
            break

        except ValueError:
            print('Invalid Input. %s must be an int' % key_name)
    return value

