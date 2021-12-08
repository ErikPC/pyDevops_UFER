def select_service(services):
    while True:
        service = input("enter an existing service: ").strip().title()
        if service in services:
            break
        else:
            print("the service selected doesn't exists")
    print('the selected service is', service)
    return service

