#Interfaz
import datetime
import string
import random
reglas_usuario = {
    'longitud_minima': 8,  # El usuario define la longitud mínima
    'longitud_maxima': 12, # El usuario define la longitud máxima
    'incluir_mayusculas': True,  # El usuario solicita incluir mayúsculas
    'incluir_minusculas': True,  # El usuario solicita incluir minúsculas
    'incluir_numeros': True,  # El usuario solicita incluir números
    'incluir_caracteres_especiales': True,  # El usuario solicita incluir caracteres especiales
    'caracteres_especiales': '!@#$%^&*()_'  # El usuario define los caracteres especiales permitidos
    }
def contraseña():
    while True:
        print("\n¿Deseas ingresar la contraseña tú mismo o generar una aleatoria?")
        print("1: Ingresar la contraseña por ti mismo")
        print("2: Generar una contraseña aleatoria")
        opcion = input("Selecciona una opción (1 o 2): ")
        
        if opcion == '1':
            contrasena = input('Ingresa la contraseña: ')
            break
        elif opcion == '2':
            while True:
                contrasena = generar_contrasena_aleatoria(reglas_usuario)
                print(f'Contraseña generada: {contrasena}')
                opcion= print('1: Guardar\n2: Volver\nCualquiera: Generar nueva')
                if opcion==1:
                    return contrasena

        else:
            print("Opción no válida. Por favor, selecciona 1 o 2.")

def generar_contrasena_aleatoria(reglas):
    caracteres = []
    posibles_caracteres = ''

    # Añadir los tipos de caracteres según las reglas
    if reglas['incluir_mayusculas']:
        posibles_caracteres += string.ascii_uppercase
    if reglas['incluir_minusculas']:
        posibles_caracteres += string.ascii_lowercase
    if reglas['incluir_numeros']:
        posibles_caracteres += string.digits
    if reglas['incluir_caracteres_especiales']:
        posibles_caracteres += reglas['caracteres_especiales']
    
    # Asegurarse de que al menos un carácter de cada tipo requerido esté presente
    if reglas['incluir_mayusculas']:
        caracteres.append(random.choice(string.ascii_uppercase))
    if reglas['incluir_minusculas']:
        caracteres.append(random.choice(string.ascii_lowercase))
    if reglas['incluir_numeros']:
        caracteres.append(random.choice(string.digits))
    if reglas['incluir_caracteres_especiales']:
        caracteres.append(random.choice(reglas['caracteres_especiales']))
    
    # Completar la contraseña hasta la longitud mínima
    while len(caracteres) < reglas['longitud_minima']:
        caracteres.append(random.choice(posibles_caracteres))
    
    # Mezclar los caracteres para que la contraseña sea menos predecible
    random.shuffle(caracteres)
    
    contrasena = ''.join(caracteres)
    
    return contrasena

def buscar_usuario_en_archivo(nombre_archivo, nombre_usuario):
    """
    Busca un nombre de usuario en el archivo y retorna la contraseña si se encuentra.
    """
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            if ':' in linea:
                clave, valor = linea.strip().split(':', 1)
                if clave == nombre_usuario:
                    return valor
    return None


def guardar_contrasena(usuario):
    datos = {
        "Servicio": input('Servicio: '),
        "usuario": usuario,
        # Aquí se cifra la contraseña antes de guardarla
        "contrasena": hashlib.sha256(input('Contraseña: ').encode()).hexdigest(),
        "url": input('URL: '),
        "descripcion": input('Descripción (Opcional): '),
        "fecha_creacion": str(datetime.datetime.now())
    }
    
    with open(usuario + '.txt', 'a') as archivo:
        # Escribir los datos en formato clave-valor
        for clave, valor in datos.items():
            archivo.write(f'{clave}: {valor}, ')
        archivo.write('\n')  # Añadir una línea en blanco para separar entradas
        print('Contraseña registrada..')
    
def ver_contraseñas(usuario):
    with open(usuario + ".txt", "rb") as archivo:
        archivo.seek(0)
        clave_maestra = input("Clave Maestra: ")
        valor = buscar_usuario_en_archivo(nombre_archivo='Usuarios.txt', nombre_usuario=usuario)
        if valor== clave_maestra:
            if archivo.read=='':
                print(f'El archivo {usuario}.txt está vació')
            else:
                for linea in archivo:
                    linea.strip()
                    print(linea)

def interfaz(Username):
    while True:
        print('___Que desea realizar___\n1: Guardar contraseña\n2: Ver contraseñas\nenter: Salir')
        opcion= int(input('Diguite un número: '))
        try:
            if opcion==1:
                guardar_contrasena(Username)
            elif opcion==2:
                ver_contraseñas(Username)
            elif opcion=='':
                break
            else:
                print('Opción no valida')     
        except ValueError:
            print('Opción no valida')     