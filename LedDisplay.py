#!/usr/bin/python3
import time
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.columns import Columns

msg = {
    "welcome": {
        "title": "[bold cyan]LED DISPLAY[/bold cyan]",
        "text": "Holi :waving_hand:\n\nEste pequeño programa, imprime números simulando un display led que lee de un input dado por el usuario.\n\nNo es gran cosa, pero estoy empezando...\n\nAsí que plis, no me lo tengan en cuenta.\n\n[red bold]Reglas:[/red bold]\n\n:cross_mark: No decimales.\n:cross_mark: No más de nueve cifras.\n:cross_mark: Nada de caracteres que no sean números.",
        "subtitle": "[bold red]Atte. Erika y Tina :smile_cat:[/bold red]",
    },
    "ask_numbers": "[medium_spring_green]Por favor, escribe un número no mayor de nueve cifras[/medium_spring_green]",
    "again": "¡Prueba todas las veces que quieras! :smiling_face_with_3_hearts:",
    "bye": ":waving_hand: Bye, Bye :waving_hand:",
    "errors": {
        "so_much_nums": ":exclamation: No se aceptan números de más de nueve cifras.",
        "negative_num": ":exclamation: No se aceptan números negativos.",
        "only_int": ":exclamation: Por favor, solo números enteros.",
        "only_digits": ":exclamation: Por favor, solo números.",
    },
}

display = [[] for x in range(7)]
led_numbers = {
    9: ["#####", "#   #", "#   #", "#####", "    #", "    #", "    #"],
    8: ["#####", "#   #", "#   #", "#####", "#   #", "#   #", "#####"],
    7: ["#####", "    #", "    #", "    #", "    #", "    #", "    #"],
    6: ["#####", "#    ", "#    ", "#####", "#   #", "#   #", "#####"],
    5: ["#####", "#    ", "#    ", "#####", "    #", "    #", "#####"],
    4: ["#   #", "#   #", "#   #", "#####", "    #", "    #", "    #"],
    3: ["#####", "    #", "    #", "#####", "    #", "    #", "#####"],
    2: ["#####", "    #", "    #", "#####", "#    ", "#    ", "#####"],
    1: ["    #", "    #", "    #", "    #", "    #", "    #", "    #"],
    0: ["#####", "#   #", "#   #", "#   #", "#   #", "#   #", "#####"],
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


def ask_nums():
    while True:
        try:
            user_num = Prompt.ask(f"{msg['ask_numbers']}")
            if not user_num.isdigit():
                raise Exception(f"{msg['errors']['only_digits']}")
            if "." in user_num:
                raise Exception(f"{msg['errors']['only_int']}")
            if "-" in user_num:
                raise Exception(f"{msg['errors']['negative_num']}")
            if len(user_num) > 9:
                raise Exception(f"{msg['errors']['so_much_nums']}")
            break
        except Exception as error:
            print(f"[red]{error}[/red]")
    return str(user_num)


def led_print(user_nums):
    print(
        Panel(
            f"{user_nums}",
            title="[cyan]Numero a imprimir[/cyan]",
            title_align="left",
            width=64,
            border_style="orchid1",
            style="medium_spring_green",
            padding=(1, 1),
        )
    )
    for num in user_nums:
        for i in range(7):
            display[i].append(f"{led_numbers[int(num)][i]} ")
    [print(Columns(display[row])) for row in range(len(display))]


def clear_display():
    global display
    del display[:]
    display = [[] for i in range(7)]


def sepparator(msg=""):
    print(
        Panel(
            f"{msg}",
            width=64,
            border_style="orchid1",
            style="medium_spring_green",
        )
    )


first_time = True

while True:
    if first_time:
        first_time = False
        welcome()
    led_print(ask_nums())
    sepparator()
    if not Confirm.ask(
        "[medium_spring_green]¿Quieres hacerlo con otro número?[/medium_spring_green]"
    ):
        sepparator(msg["bye"])
        time.sleep(1)
        break
    clear_display()
    sepparator(msg["again"])
