# /
#  * Crea una función que dibuje una espiral como la del ejemplo.
#  * - Únicamente se indica de forma dinámica el tamaño del lado.
#  * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
#  *
#  * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
#  * ════╗
#  * ╔══╗║
#  * ║╔╗║║
#  * ║╚═╝║
#  * ╚═══╝
#  */
import math
def espiral(size):

    first_line = math.ceil(size / 2)

    for i in range(first_line):
        if i == 0:
            print(("=" * (size - 1)) + "╗")
        else:
            print(("║" * (i - 1) + "╔" + "=" * (size - (2 * i) - 1)) + "╗" + "║" * i)

    for i in range(first_line, size):
        print(
            "║" * (size - i - 1)
            + "╚"
            + "=" * ((2 * i) - size)
            + "╝"
            + "║" * (size - i - 1)
        )
espiral(5)