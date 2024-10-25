from typing import List, Tuple
# Crear una función que elimine los espacios de una cadena y devuelva una lista usando listas de comprensión

def remove_spaces(text: str) -> list:
    return [char for char in text if char != " "]

# print(
#     remove_spaces(input("Ingresa una frase: "))
# )

# Crear una función devuelva un diccionario tras contar cuantas letras repetidas hay en una cadena.
# Es decir: que cada letra individual sea una clave y su valor la cantidad de veces que aparece.

def count_chars_with_dict(text: list) -> dict:
    chars_count_dict = {}
    for char in text:
        if not char in chars_count_dict:
            chars_count_dict[char] = 1
        else:
            chars_count_dict[char] += 1

    return chars_count_dict

# print(
#     count_chars_with_dict(
#       remove_spaces(
#           input("Ingresa una frase: ")
#       )
#     )
# )

# Ordenar un diccionario por el valor de sus claves y devolver una lista que contenga tuplas con sus datos

def dict_order_by_valor(dictionary: dict) -> List[Tuple[str, int]]:
    result = []
    for key, value in dictionary.items():
        result.append((key, value))

    result.sort(key=lambda c: c[1], reverse=True)
    return result

# print(
#     dict_order_by_valor(
#         count_chars_with_dict(
#             remove_spaces(
#                 input("Ingresa una frase:")
#             )
#         )
#     )
# )

# Del return de la función anterior, devolver solo las tuplas con mayor valor en una lista

def only_higher_tuples(tuple_list: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    max_valor = tuple_list[0][1]
    new_list = [item for item in tuple_list if item[1] == max_valor]
    return new_list

# print(
#     only_higher_tuples(
#         dict_order_by_valor(
#             count_chars_with_dict(
#                 remove_spaces(
#                     input("Ingresa un frase: ")
#                 )
#             )
#         )
#     )
# )

# Usando la función anterior imprimir algo como:
# Los caráctes que más se repiten con X veces, son:
# - Primer char
# - Segundo char
# - ...

def most_repeated_char(tuple_list: List[Tuple[str, int]]) -> None:
    print(f"Los carácteres que más se repiten con {tuple_list[0][1]} veces, son:")
    for item in tuple_list:
        print(f"- {item[0]}")


most_repeated_char(
    only_higher_tuples(
        dict_order_by_valor(
            count_chars_with_dict(
                remove_spaces(
                    input("Ingresa una frase: ").lower()
                )
            )
        )
    )
)