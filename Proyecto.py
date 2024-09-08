#Proyecto
import Interfaz

def verificar_contrasena(contrasena):
    reglas_usuario = {
    'longitud_minima': 8,  # El usuario define la longitud mínima
    'longitud_maxima': 12, # El usuario define la longitud máxima
    'incluir_mayusculas': True,  # El usuario solicita incluir mayúsculas
    'incluir_minusculas': True,  # El usuario solicita incluir minúsculas
    'incluir_numeros': True,  # El usuario solicita incluir números
    'incluir_caracteres_especiales': True,  # El usuario solicita incluir caracteres especiales
    'caracteres_especiales': '!@#$%^&*()_'  # El usuario define los caracteres especiales permitidos
    }
    if len(contrasena) < reglas_usuario['longitud_minima']:
        return False
    if len(contrasena) > reglas_usuario['longitud_maxima']:
        return False
    if reglas_usuario['incluir_mayusculas'] and not any(c.isupper() for c in contrasena):
        return False
    if reglas_usuario['incluir_minusculas'] and not any(c.islower() for c in contrasena):
        return False
    if reglas_usuario['incluir_numeros'] and not any(c.isdigit() for c in contrasena):
        return False
    if reglas_usuario['incluir_caracteres_especiales']:
        if not any(c in reglas_usuario['caracteres_especiales'] for c in contrasena):
            return False
    return True


def verificar_usuario(nombre_usuario):
    """
    Verifica si un nombre de usuario está en el archivo 'Usuarios.txt'.
    """
    try:
        with open("Usuarios.txt", 'r') as archivo:
            for linea in archivo:
                linea = linea.strip()  # Elimina espacios en blanco al principio y al final
                # Ignora líneas vacías
                if not linea:
                    continue
                # Asegúrate de que la línea contenga al menos un delimitador ':'
                if ':' in linea:
                    clave, valor = linea.split(':', 1)
                    if clave == nombre_usuario:
                        return True
                else:
                    print(f"Formato incorrecto en línea: '{linea}'")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    
    return False

def registrar_usuario():
    while True:
        username = input("Nombre de Usuario: ")
        if verificar_usuario(username):
            print(f'El usuario {username} ya se encuentra registrado.')
        else:
            password = input("Contraseña (debe tener entre 8 y 12 caracteres, incluir mayúsculas, minúsculas, números y caracteres especiales válidos): ")
            if verificar_contrasena(password):
                with open('Usuarios.txt', "a") as archivo:
                     archivo.write(f'{username}:{password}\n')
                
                with open(username+'.txt', 'w') as archivo:
                    print("Usuario registrado con éxito")
                break

            else:
                print("Contraseña no válida, ingrese una nueva.")


def iniciar_secion():
    while True:
        cont = 3
        username = input("Nombre de Usuario: ")
        if username == "":
            break
        password = input("Password: ")
        resultado = Interfaz.buscar_usuario_en_archivo('Usuarios.txt', username)
        if resultado:
            if resultado == password:
                Interfaz.interfaz(username)
                break
            else:
                print("Contraseña incorrecta")
                cont -= 1
        else:
            print("Usuario no encontrado, inténtalo de nuevo o presiona enter para salir")

        if cont == 0:
            print("Número máximo de intentos alcanzado.")
            break  

while True:
    print("__Menú de incio__\n1: Iniciar seción\n2: Registrarse\notro: Salir")
    opción = int(input("Ingrese un número: "))
    if opción ==1:
        iniciar_secion()
    elif opción == 2:
        registrar_usuario()
    else: 
        print("Cerrando...")
        break