def select_service(services):
    while True:
        service = input("enter an existing service: ").strip()
        if service in services:
            break
    print('the selected service is', service)
    return service

