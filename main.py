def obtener_curso():
    curso = input('Inserte el nombre del curso: ').upper()
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
            calcular_calificacion()
            break
        elif reiniciar == 'no':
            print('Muchas Gracias por usar nuestros servicios')
            break
        else:
            print('Opción no valida ')
