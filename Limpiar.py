#Limpiar
import os
import platform


def limpiar_terminal():
    """
    Limpia la pantalla de la terminal según el sistema operativo.
    """
    sistema = platform.system()

    if sistema == "Windows":
        os.system('cls')
    elif sistema in ["Linux", "Darwin"]:  # 'Darwin' es para macOS
        os.system('clear')
    else:
        print("Sistema operativo no soportado para limpiar la pantalla.")