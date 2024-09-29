my_dict = {'name': 'Olga', 'year_of_birth': 1988}
print(my_dict)
print(my_dict.get('name'))
print(my_dict.get('Kamila'))
my_dict['year_of_birth2'] = 2010
my_dict['year_of_birth3'] = 2013
print(my_dict)
del my_dict['year_of_birth']
print(my_dict)
my_dict.pop('name')

my_set = {1, 3, 4, 5, 6, 7, 4, 7, 8, 1, 'Hello world', (3, 2, 1)}
print(my_set)
print(my_set.add(10))
print(my_set)
print(my_set.add('String'))
print(my_set)
print(my_set.discard(6))
print(my_set)