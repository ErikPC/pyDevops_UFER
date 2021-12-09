def fill_string(key_name):
    while True:
        try:
            value = input(key_name + ": ").strip()
            break

        except ValueError:
            print('Invalid Input. price must be a string.')
    return value

