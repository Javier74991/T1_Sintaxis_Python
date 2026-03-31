
def ingresar_calificaciones():
    continuar = True
    lista_materias = []
    lista_calificaciones = []
    while continuar:
        materia = input("Ingrese la materia: ")
        lista_materias.append(materia)
        try:
            calificacion = float(input("Ingrese la calificacion: "))
            if 0 <= calificacion <= 10:
                lista_calificaciones.append(calificacion)
            else:
                print("La calificacion introducida no es valida")
                lista_materias.pop(len(lista_materias) - 1)
        except:
            print("La calificacion introducida no es valida")
            lista_materias.pop(len(lista_materias) - 1)

        respuesta = input("Desea continuar ingresando más materias? (s/n)")
        if respuesta == "n":
            continuar = False
        elif respuesta == "s":
            continuar = True

    return lista_materias, lista_calificaciones


def calcular_promedio(calificaciones):
    promedio = sum(calificaciones) / len(calificaciones)
    return promedio

def determinar_estado(calificaciones, umbral=5.0):
    materias_aprobadas = []
    materias_reprobadas = []
    for i in range(len(calificaciones)):
        if calificaciones[i] >= umbral:
            materias_aprobadas.append(i)
        else:
            materias_reprobadas.append(i)

    return materias_aprobadas, materias_reprobadas



def encontrar_extremos(calificaciones):
    indice_max = calificaciones.index(max(calificaciones))
    indice_min = calificaciones.index(min(calificaciones))
    return indice_max, indice_min


def main():
    lista_materias, lista_calificaciones = ingresar_calificaciones()
    if len(lista_calificaciones) == 0:
        print("No hay materias")
    else:
        promedio = calcular_promedio(lista_calificaciones)
        materias_aprobadas, materias_reprobadas = determinar_estado(lista_calificaciones)
        indice_max, indice_min = encontrar_extremos(lista_calificaciones)
        print (f"Estas han sido la lista de materias y calificaciones introducidas")
        for i in range (len(lista_materias)):
            print(f"{lista_materias[i]}: {lista_calificaciones[i]}")

        print(f"El promedio de las calificaciones ha sido: {promedio}")
        print(f"La nota más baja ha sido en la materia {lista_materias[indice_min]}, con una nota de {lista_calificaciones[indice_min]}")
        print(f"La nota más alta ha sido en la materia {lista_materias[indice_max]}, con una nota de {lista_calificaciones[indice_max]}")
        print("Estas han sido las materias aprobadas")
        for i in range(len(materias_aprobadas)):
            print(lista_materias[materias_aprobadas[i]])
        print("Estas han sido las materias reprobadas")
        for i in range(len(materias_reprobadas)):
            print(lista_materias[materias_reprobadas[i]])

    print("Gracias por utilizar este programa")



if __name__ == "__main__":
    main()