def fill_array():
    array = list()
    finish = False
    print("Add amenities. Press 'exit' to stop")
    while not finish:
        user_input = input("amenity: ")
        if user_input == 'exit':
            finish = True
        else:
            array.append(user_input)
    return array
