#! /usr/bin/env python3

alumnos = []


def existeAlumno(nombre):
    posicion = -1
    for i in range(len(alumnos)):
        if (alumnos[i]['nombre'] == nombre):
            posicion = i
    return posicion

def agregarAlumno():
    nombre = input('  Indique el nombre del alumno > ')
    if existeAlumno(nombre) == -1:
        nuevoAlumno = {'nombre': nombre, 'notas': [0,0,0,0,0,0]}
        alumnos.append(nuevoAlumno)
        print('  El alumno ' + nombre + ' ha sido agregado correctamente')
    else:
        print('  ¡Ya existe un alumno con ese nombre!')

def mostrarAlumnos():
    for i in range(len(alumnos)):
        print(' - ' + alumnos[i]['nombre'])

def agregarNotas():
        nombre = input(' Indique el nombre del alumno > ')
        i = existeAlumno(nombre)
        if i > -1:
            alumnos[i]['notas'][0] = int(input('Indique la nota de Análisis forense > '))
            alumnos[i]['notas'][1] = int(input('Indique la nota de Bastionado de redes > '))
            alumnos[i]['notas'][2] = int(input('Indique la nota de Hacking ético > '))
            alumnos[i]['notas'][3] = int(input('Indique la nota de Incidentes de ciberseguridad > '))
            alumnos[i]['notas'][4] = int(input('Indique la nota de Normativa de ciberseguridad > '))
            alumnos[i]['notas'][5] = int(input('Indique la nota de Producción segura > '))
        else:
            print('¡No existe ningún alumno con ese nombre!')
            
def modificarNotas():
    print("En breve estará listo")

def mostrarNotas():
        nombre = input(' Indique el nombre del alumno > ')
        i = existeAlumno(nombre)
        if i > -1:
            print(' Notas de ' + nombre + ": ")
            print('   Análisis forense: ' + str(alumnos[i]['notas'][0] ))
            print('   Bastionado de redes: ' + str(alumnos[i]['notas'][1] ))
            print('   Hácking ético: ' + str(alumnos[i]['notas'][2] ))
            print('   Incidentes de ciberseguridad: ' + str(alumnos[i]['notas'][3] ))
            print('   Normativa de ciberseguridad: ' + str(alumnos[i]['notas'][4] ))
            print('   Producción segura: ' + str(alumnos[i]['notas'][5] ))
        else:
            print('¡No existe ningún alumno con ese nombre!')


def calcularMedias():
    for i in range(len(alumnos)):
        media = 0
        for j in range(len(alumnos[i]['notas'])):
            media += alumnos[i]['notas'][j]
        media /= 6
        print(' - ' + alumnos[i]['nombre'] + ": " + str(media))


def promociones():
    for i in range(len(alumnos)):
        suspendidas = 0
        for j in range(len(alumnos[i]['notas'])):
            if alumnos[i]['notas'][j] < 5:
                suspendidas += 1
        if suspendidas < 2:
            print(' - ' + alumnos[i]['nombre'] + ": PROMOCIONA")
        else:
            print(' - ' + alumnos[i]['nombre'] + ": No promociona")



# Menú del programa

opcion = ''

while opcion != '9':
    print('BROCHA EKADE')
    print('-------------------------')
    print()
    print('1) Mostrar alumnos')
    print('2) Mostrar notas')
    print('3) Calcular medias')
    print('4) Promociones')
    print('5) Agregar alumno')
    print('6) Agregar notas')
    print('7) Modificar notas')
    print()
    print('9) Salir')
    print()
    opcion = input('Indique su opcion > ')

    if opcion == '1':
        mostrarAlumnos()
    elif opcion == '2':
        mostrarNotas()
    elif opcion == '3':
        calcularMedias()
    elif opcion == '4':
        promociones()
    elif opcion == '5':
        agregarAlumno()
    elif opcion == '6':
        agregarNotas()

print()
print('¡Hasta otra!')