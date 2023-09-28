def obtener_nombre_estudiante():
    nombre = input('Ingrese el nombre del estudiante: ')
    return nombre

def obtener__nombre_curso():
    curso = input('Ingrese el nombre del curso: ').upper()
    return curso

def obtener_puntos_totales():
    while True:
        try:
            puntos_totales = int(input('Ingrese los puntos totales obtenidos en el curso: '))
            return puntos_totales
            break
        except ValueError:
            print('La opción no es valida, por favor intentelo de nuevo')

def obtener_puntos_estudiante():
    while True:
        try:
            puntos_estudiante = int(input('Ingrese los puntos obtenidos por el estudiante: '))
            return puntos_estudiante
            break
        except ValueError:
            print('La opción no es valida, por favor intentelo de nuevo')

def calcular_calificacion():
    puntos_clase = obtener_puntos_totales()
    puntos_estudiante  = obtener_puntos_estudiante()

    if puntos_clase > 0:
        calificacion_final = (puntos_estudiante / puntos_clase) * 100
        print(calificacion_final)
        return calificacion_final
    else:
        print('No se puede dividir por 0')

def reiniciar():
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
    nombre = obtener_nombre_estudiante()
    curso = obtener__nombre_curso()
    calificacion = calcular_calificacion()

    print(f'El esudiante {nombre.upper()} en el curso {curso}, ha obtenido una calificación de: {calificacion}')

    reiniciar()

main()