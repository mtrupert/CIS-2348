# Name: Michael Rupert
# PSID: 1855121


services = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12,}

print("Davy's auto shop services")
print('Oil change -- ${}'.format(services['Oil change']))
print('Tire rotation -- ${}'.format(services['Tire rotation']))
print('Car wash -- ${}'.format(services['Car wash']))
print('Car wax -- ${}'"\n".format(services['Car wax']))

service_one = input('Select first service:'"\n")
service_two = input('Select second service:'"\n")


total_price = services[service_one] + services[service_two]
print("\n""Davy's auto shop invoice""\n")
print('Service 1:', service_one, '${}'.format(services[service_one]))
print('Service 2:', service_two, '${}'"\n".format(services[service_two]))
print('Total: ${}'.format(total_price))
