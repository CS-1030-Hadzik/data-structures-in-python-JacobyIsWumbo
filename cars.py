print('Jacob Christensen')
cars = [ 'Ford', 'Chrysler', 'Dodge', 'Ram', 'Jeep', 'Chevy', 'GMC']
print(cars)
print(len(cars))
cars.append('Buick')
print(cars)
print(cars[5])
cars.insert(4, 'Toyota')
print(cars)
cars.pop(6)
cars.sort()
print(cars)
cars.sort(reverse= True)
print(cars)
my_array_length = len(cars)
array_string = 'The length of my array is '
print(array_string + str(my_array_length))