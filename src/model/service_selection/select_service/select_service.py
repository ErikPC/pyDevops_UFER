def select_service(services):
    while True:
        service = input("enter an existing service: ").strip().title()
        if service in services:
            break
    print('the selected service is', service)
    return service


select_service(['Ufer Gold', 'Ufer Lite', 'Ufer Bus'])
