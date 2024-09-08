#Interfaz
import datetime

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
        "Servicio":input('Servicio: '),
        "usuario": usuario,
        "contrasena": input('contrasena: '),
        "url": input('url: '),
        "descripcion": input('descripcion(Opcional): '),
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