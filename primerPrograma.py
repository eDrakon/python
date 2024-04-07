
# fav_plant = "Estapifilo"

# user_input = input("¿Cuál es tu planta favorita? ")

# if user_input == fav_plant:
#     print("Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!")
# elif user_input == fav_plant.lower():
#     print("No, ¡quiero un gran Espatifilo!")
# else:
#     print("¡Espatifilo! ¡No", user_input +'!')

# blocks = int(input("Ingresa el número de bloques: "))
# height = 0
# block_in_level = 1
# #
# # Escribe tu código aquí.
# #
# while blocks >= block_in_level:
#     height += 1
#     blocks -= block_in_level
#     block_in_level += 1
# print("La altura de la pirámide:", height)

# c0 = int(input("Ingresa un número positivo distinto de cero: "))
# counter = 0
# while c0 != 1:
#     if c0 % 2 == 0:
#         c0 = c0 // 2
#     else:
#         c0 = 3 * c0 + 1
#     print(c0)
#     counter += 1
# print("Pasos =", counter)
# mail_user = ''
# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         # Línea de código.
#         break
#     mail_user += ch
# print(mail_user)
#     # Línea de código.
# true_digit = ''
# for digit in "0165031806510":
#     if digit == "0":
#         true_digit += "x"
#         continue
#     true_digit += digit
# print(true_digit)
# flag_register = 0b11111111111111111111111111110111
# the_mask = 2 ** 3
# flag_register &= ~the_mask
# if flag_register & the_mask:
#     print("El bit estaba encendido.")
# else:
#     print("El bit estaba apagado.")

# def is_prime(num):
#     #
#     # Escribe tu código aquí.
#     #
#     div_nums = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             div_nums.append(i)
#     if len(div_nums) > 2:
#         return False
#     else:
#         return True

# for i in range(1, 4000):
#     if is_prime(i + 1):
#         print(i + 1, end=" ")
# print()

# def liters_100km_to_miles_gallon(liters):
#     #
#     # Escribe tu código aquí.
#     #
#     return (liters/3.785411784) * (1.609344/100)
# def miles_gallon_to_liters_100km(miles):
#     #
#     # Escribe tu código aquí.
#     #
#     return (100/miles) * (3.785411784/1.609344)
# print(liters_100km_to_miles_gallon(3.9))
# print(liters_100km_to_miles_gallon(7.5))
# print(liters_100km_to_miles_gallon(10.))
# print(miles_gallon_to_liters_100km(60.3))
# print(miles_gallon_to_liters_100km(31.4))
# print(miles_gallon_to_liters_100km(23.5))

# def even_num_lst(ran):
#     lst = []
#     for num in range(ran):
#         if num % 2 == 0:
#             lst.append(num)
#     return lst

# print(even_num_lst(11))

# tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
# duplicates = tup.count(2)# Escribe tu código aquí.

# print(duplicates) # salida: 4

# d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
# d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
# d3 = {}

# for item in (d1, d2):
#     d3.update(item)
#     # Escribe tu código aquí.

# print(d3)

# my_list = ["car", "Ford", "flower", "Tulip"]

# t = tuple(my_list)
# print(t)

# colors = (("green", "#008000"), ("blue", "#0000FF"))

# # Escribe tu código aquí.
# colors_dictionary = dict(colors)

# print(colors_dictionary)

# my_dictionary = {"A": 1, "B": 2}
# copy_my_dictionary = my_dictionary.copy()
# my_dictionary.clear()

# print(my_dictionary)

# dictionary = {}
# my_list = ['a', 'b', 'c', 'd']

# for i in range(len(my_list) - 1):
#     dictionary[my_list[i]] = (my_list[i], )

# for i in sorted(dictionary.keys()):
#     k = dictionary[i]
#     # Inserta tu código aquí.
#     print(k[0])
# tup = (1, 2, 4, 8)
# tup = tup[-2:-1]
# tup = tup[-1]
# print(tup)