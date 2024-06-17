import csv
lista=[]

def validar ():
    if efectividad>=0 and efectividad<=100:
        print("Porcentaje válido")
        listita.insert(2,efectividad)
    else:
        print("Porcentaje inválido")
        print("")

def interna ():
    if efectividad>=0 and efectividad<=25:
        categoria=("chiste")
        print("Categoría: Chiste")
        listita.insert(3,categoria)
        return categoria
    elif efectividad>=26 and efectividad<=50:
        categoria=("anecdota")
        print("Categoría: Anécdota")
        listita.insert(3,categoria)
        return categoria
    elif efectividad>=51 and efectividad<=75:
        categoria=("peligro")
        print("Categoría: Peligro")
        listita.insert(3,categoria)
        return categoria
    elif efectividad>=76 and efectividad<=100:
        categoria=("Esclavitud")
        print("Categoría: Esclavitud")
        listita.insert(3,categoria)
        return categoria

while (True):
    print("1.- Agregar plan")
    print("2.- Listar planes")
    print("3.- Eliminar plan por ID")
    print("4.- Generar bbdd")
    print("5.- Cargar bbdd")
    print("6.- Estadísticas")
    print("0.- Salir")
    op=int(input("Ingrese opción: "))

    if op==1:
        print("")
        print("~ Agregar Plan ~")
        print("")
        iden=int(input("Ingrese ID: "))
        nombre=input("Ingrese nombre: ")
        listita=[iden,nombre]
        efectividad=int(input("Ingrese porcentaje de efectividad: "))
        validar()
        interna()
        lista.append(listita)

    elif op==2:
        print("")
        print("~ Lista de planes ~")
        print("")
        for plan in lista:
            print("ID: ",plan[0],"Nombre: ",plan[1],"Porcentaje de efectividad: ",plan[2],"Categoría interna: ",plan[3])
        print("")

    elif op==3:
        encontrado=False
        print("")
        print("~ Eliminar Plan ~")
        print("")
        buscar=int(input("Ingrese ID a eliminar: "))
        for plan in lista:
            if buscar==plan[0]:
                print("ID: ",plan[0],"Nombre: ",plan[1],"Porcentaje de efectividad: ",plan[2],"Categoría interna: ",plan[3])
                encontrado=True
                print("¿Desea eliminar el plan?")
                print("1.- SI")
                print("2.- NO")
                respuesta=int(input("Ingrese una opción: "))
                if respuesta==1:
                    lista.remove(buscar)
                    print("Plan eliminado")
                    print("")
                elif respuesta==2:
                    print("No se ha eliminado el plan")
                    print("")
            else:
                print("Plan no encontrado")
                print("")

    elif op==4:
        print("")
        print("~ Generar base de datos ~")
        print("")
        with open ('bbdd_plan.csv','w',newline='') as bbdd_plan:
            escritor_csv=csv.writer(bbdd_plan)
            escritor_csv.writerow(['iden','nombre','efectividad','categoria'])
            escritor_csv.writerows(lista)
            print("")
            print("Archivo generado correctamente")
            print("")

    elif op==5:
        print("")
        print("~ Cargar base de datos ~")
        print("")
        with open ('bbdd_plan.csv','r',newline='') as bbdd_plan:
            lector_csv=csv.reader(bbdd_plan)
            for fila in lector_csv:
                lista.append(fila)

    elif op==6:
        print("")
        print("~ Estadísticas ~")
        print("")
        acum=0
        cantidad=len(lista)
        if cantidad>0:
            for plan in lista:
                acum=acum+plan[2]
            promedio=acum/cantidad
            #hhhhhhhh
            print("Cantidad de planes: ",cantidad)
            print("Promedio de efectividad: ",promedio)
            print("Plan con efectividad más alto: ")#hhhh)

    elif op==0:
        print("")
        print("ADIOS")
        break

    else:
        print("")
        print("Error, ingrese una opción válida")
            
        
        
