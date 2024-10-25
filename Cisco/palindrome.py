import time
from rich import print
from rich.prompt import Prompt, Confirm
from rich.panel import Panel

msg = {
    "welcome": {
        "title": "[bold cyan]PALINDROMO[/bold cyan]",
        "text": ('Holi :waving_hand:\n'
                 '\n'
                 'Este pequeño programa, comprueba si una cadena dada por el usuario forma un palíndromo o no\n'
                 '\n'
                 'No es gran cosa, pero estoy empezando...\n'
                 '\n'
                 'Así que plis, no me lo tengan en cuenta.'),
        "subtitle": "[bold red]Atte. Erika y Tina :smile_cat:[/bold red]",
    },
    "again": "¡Prueba todas las veces que quieras! :smiling_face_with_3_hearts:",
    "bye": ":waving_hand: Bye, Bye :waving_hand:",
}


def welcome():
    print(
        Panel(
            f"{msg['welcome']['text']}",
            title=msg["welcome"]["title"],
            subtitle=msg["welcome"]["subtitle"],
            title_align="left",
            subtitle_align="right",
            width=64,
            border_style="orchid1",
            style="medium_spring_green",
            padding=(1, 0),
        )
    )


def sepparator(message: str = ""):
    print(
        Panel(
            f"{message}",
            width=64,
            border_style="orchid1",
            style="medium_spring_green",
        )
    )


def ask_user_string():
    while True:
        try:
            user_string = Prompt.ask(
                "¡Di tu frase! ¡En seguida comprobaremos si es o no un palíndromo!"
            )
            if user_string == "":
                raise Exception("Por favor, debes escribir algo.")
            return user_string
        except Exception as error:
            print(f"[red]{error}[/red]")


def is_palindrome(user_string: str):
    reverse_string = user_string[::-1]
    if reverse_string.upper().replace(" ", "") == user_string.upper().replace(" ", ""):
        message = f"¡Muy bien! :D, {user_string} es un palíndromo."
    else:
        message = f"¡Qué pena! :(, {user_string} no es un palíndromo.)"
    print(
        Panel(
            f"{message}",
            width=64,
            border_style="orchid1",
            style="medium_spring_green",
        )
    )


def main():
    first_time = True
    while True:
        if first_time:
            first_time = False
            welcome()
        is_palindrome(ask_user_string())
        if not Confirm.ask(
            "[medium_spring_green]¿Quieres probar de nuevo?[/medium_spring_green]"
        ):
            sepparator(msg["bye"])
            time.sleep(1)
            break
        sepparator(msg["again"])


main()
