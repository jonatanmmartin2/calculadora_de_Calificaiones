def obtener_nombre_estudiante():
    """
    Función para obtener el nombre del estudiante
    """
    nombre = input('Ingrese el nombre del estudiante: ')
    return nombre

def obtener_nombre_curso():
    """
    Función para obtener el nombre del curso
    """
    curso = input('Ingrese el nombre del curso: ').upper()
    return curso

def obtener_puntos_totales():
    """
    Función obtener los puntos totales del curso, maneja entrada de errores
    para evitar que el programa se rompa
    """
    while True:
        try:
            puntos_totales = int(input('Ingrese los puntos totales obtenidos en el curso: '))
            return puntos_totales
        except ValueError:
            print('La opción no es valida, por favor intentelo de nuevo')

def obtener_puntos_estudiante():
    """
    Función obtener los puntos obtenido del estudiante, maneja entrada de errores
    para evitar que el programa se rompa
    """
    while True:
        try:
            puntos_estudiante = int(input('Ingrese los puntos obtenidos por el estudiante: '))
            return puntos_estudiante
        except ValueError:
            print('La opción no es valida, por favor intentelo de nuevo')

def calcular_calificacion():
    """
    Función para calcular la nota final del curso, cuenta con manejo de errores en caso 
    que se llegue a dividir entre 0 y si el estudiante tiene más puntos que del curso.
    Nota la calificación total del curso es entera, es decir no da el resultado en 
    decimales.
    """
    while True:
        puntos_clase = obtener_puntos_totales()
        puntos_estudiante  = obtener_puntos_estudiante()

        if puntos_clase == 0:
            print('No se puede dividir por 0')
        elif puntos_clase < puntos_estudiante:
            print('El estudiante cuenta con más puntos de los que hay en curso\nPor Favor verifique los datos')
        else:
            calificacion_final = (puntos_estudiante // puntos_clase) * 100
            return calificacion_final

def reiniciar():
    """
    Función para reiniciar si el usuario desea calcular de nuevo la nota final
    de un estudiante
    """
    while True:
        reiniciar = input('¿Desea ingresar otro estudiante? (Si o No) ').lower()

        if reiniciar == 'si':
            main()
            break
        elif reiniciar == 'no':
            print('Muchas Gracias por usar nuestros servicios')
            break
        else:
            print('Opción no valida ')

def main():
    """
    Función principal del programa que llama a las otras funciones
    para que se ejecure correctamente el código
    """
    nombre = obtener_nombre_estudiante()
    curso = obtener_nombre_curso()
    calificacion = calcular_calificacion()

    print(f'El esudiante {nombre.upper()} en el curso {curso.upper()}, ha obtenido una calificación de: {calificacion}')

    reiniciar()

main() # Corre el programa