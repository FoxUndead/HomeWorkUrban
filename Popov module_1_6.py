# Словарь
my_dict = {'Boris': 1809, 'Moris': 1903, 'Ivan': 1533, 'Xander': 2002}
print(my_dict)
print(my_dict.get('Xander'))
print(my_dict.get('Uriy'))
my_dict.update({'Page': 1997, 'Nikodim': 1887})
del my_dict['Nikodim']
print(my_dict.get('Page', 'Nikodim'))
print(my_dict)

# Множества
my_set = {3, 5, 66, "Mix", 66, 3, 5}
print(my_set)
print(my_set.update([55, 666]))
my_set.discard(5)
print(my_set)
