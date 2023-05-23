# ----------------------------------------------principal
import time
def esperar(tiempo):
    time.sleep(tiempo)
# Llamar a la función y esperar 5 segundos


class Nodo:
    # Constructor Nodo
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = "NULL"
        self.pos = 0

    # Metodo Ver el valor
    def devolver_valor(self):
        print(self.valor)

    # Metodo Asignar el siguiente
    def asignar_siguiente(self, nodo):
        self.siguiente = nodo

    # Metodo Cambiar el valor
    def cambiar_valor(self, nuevo_valor):
        self.valor = nuevo_valor

    # Metodo IMPRIMIR el siguiente
    def imprimir_siguiente(self):
        if self.siguiente == "NULL":
            print("----->  NULL   ||FIN||")
        else:
            print(self.siguiente.valor, end=" ")
            print("\033[45m" +" POSICION [", end=" ")
            print(self.siguiente.pos, end=" ")
            print(" ] "+ "\033[0m")


class ListaEnlazada:
    def __init__(self, Nodo):
        self.cabeza = Nodo

    def calc_siguiente(self):
        self.cabeza.imprimir_siguiente()

    def ciclo_sigue(self):
        print(
            "\033[41m" + "------------IMPRESION DE VALORES----------------" + "\033[0m"
        )
        if self.cabeza.siguiente != "NULL":
            print(self.cabeza.valor, end=" ")
            print("\033[45m" + " POSICION [", end=" ")
            print(self.cabeza.pos, end=" ")
            print(" ] "+ "\033[0m")

            Nodotemp = self.cabeza.siguiente
            print(Nodotemp.valor, end=" ")
            print("\033[45m"+" POSICION [", end=" ")
            print(Nodotemp.pos, end=" ")
            print(" ] "+ "\033[0m")

            while Nodotemp.siguiente != "NULL":
                print("------->")
                Nodotemp.imprimir_siguiente()
                Nodotemp = Nodotemp.siguiente

            if Nodotemp.siguiente == "NULL":
                print("\033[44m"+"\033[32m"+ "---->" + Nodotemp.siguiente+"\033[0m")
        else:
            print(self.cabeza.valor, end=" ")
            print("\033[45m"+" POSICION [", end=" ")
            print(self.cabeza.pos, end=" ")
            print(" ] "+ "\033[0m")

            print("\033[45m"+ "NULL [final]"+ "\033[0m")
        time.sleep(1)
    def agregar_Nodo_Inicio(self, Nodo):
        cabeza_temp = self.cabeza
        Nodo.asignar_siguiente(self.cabeza)
        self.cabeza = Nodo

    def agregar_Nodo_Final(self, Nodo):
        # print("------------IMPRESION DE VALORES----------------");
        if self.cabeza.siguiente != "NULL":
            # print(self.cabeza.valor)
            Nodotemp = self.cabeza.siguiente
            # print(Nodotemp.valor)

            while Nodotemp.siguiente != "NULL":
                # print("*/iTer**")
                # Nodotemp.imprimir_siguiente()
                Nodotemp = Nodotemp.siguiente

            if Nodotemp.siguiente == "NULL":
                # print(Nodotemp.siguiente)
                Nodotemp.asignar_siguiente(Nodo)

        else:
            self.cabeza.asignar_siguiente(Nodo)

        self.indexar()

    def indexar(self):
        # print("------------IMPRESION DE VALORES----------------");
        if self.cabeza.siguiente != "NULL":
            # print(self.cabeza.valor)
            self.cabeza.pos = 0
            Nodotemp = self.cabeza.siguiente
            # print(Nodotemp.valor)
            # Nodotemp.pos = 1
            i = 1
            while Nodotemp.siguiente != "NULL":
                # print("*/iTer**")
                # Nodotemp.imprimir_siguiente()
                Nodotemp.pos = i
                Nodotemp = Nodotemp.siguiente
                i = i + 1

            if Nodotemp.siguiente == "NULL":
                # print(Nodotemp.siguiente)
                # Nodotemp.asignar_siguiente(Nodo)
                Nodotemp.pos = i

        else:
            # print(self.cabeza.valor)
            self.cabeza.pos = 0

    def añadirpos(self, nodo, posi):
        # print("------------IMPRESION DE VALORES----------------");
        if self.cabeza.pos != posi:
            if self.cabeza.siguiente != "NULL":
                # print(self.cabeza.valor)

                Nodotemp = self.cabeza.siguiente
                if Nodotemp.pos == posi:
                    nodo.asignar_siguiente(Nodotemp)
                    self.cabeza.asignar_siguiente(nodo)

                # print(Nodotemp.valor)
                # Nodotemp.pos = 1
                Nodoant = self.cabeza
                while Nodotemp.siguiente != "NULL":
                    # print("*/iTer**")
                    # Nodotemp.imprimir_siguiente()
                    Nodoant = Nodotemp
                    Nodotemp = Nodotemp.siguiente
                    if Nodotemp.pos == posi:
                        nodo.asignar_siguiente(Nodotemp)
                        Nodoant.asignar_siguiente(nodo)

                if Nodotemp.siguiente == "NULL":
                    # print(Nodotemp.siguiente)
                    if Nodotemp.pos == posi:
                        nodo.asignar_siguiente(Nodotemp)
                        Nodoant.asignar_siguiente(nodo)

                if Nodotemp.siguiente == "NULL" and Nodotemp.pos == posi - 1:
                    self.agregar_Nodo_Final(nodo)
                elif Nodotemp.siguiente == "NULL" and Nodotemp.pos < posi - 1:
                    print(
                        "################### INGRESE UNA POSICIÓN VÁLIDA ##########################################"
                    )
                    esperar(4)

            else:
                # print(self.cabeza.valor)
                if posi == 1:
                    self.cabeza.asignar_siguiente(nodo)

        else:
            self.agregar_Nodo_Inicio(nodo)
        self.indexar()

    def contabilizar(self):
        # print("------------IMPRESION DE VALORES----------------");
        if self.cabeza.siguiente != "NULL":
            # print(self.cabeza.valor)
            # self.cabeza.pos = 0
            Nodotemp = self.cabeza.siguiente
            # print(Nodotemp.valor)
            # Nodotemp.pos = 1
            i = 1
            while Nodotemp.siguiente != "NULL":
                # print("*/iTer**")
                # Nodotemp.imprimir_siguiente()
                # Nodotemp.pos = i
                Nodotemp = Nodotemp.siguiente
                i = i + 1

            if Nodotemp.siguiente == "NULL":
                res = i + 1
                print("Hay en total ", res, " elementos en la lista ")
                time.sleep(5)

        else:
            print(" Hay un único elemento en la lista ")
            time.sleep(5)

    def eliminar_ultimo(self):
        # print("------------IMPRESION DE VALORES----------------");
        if self.cabeza.siguiente != "NULL":
            # print(self.cabeza.valor)
            Nodotemp = self.cabeza.siguiente
            # print(Nodotemp.valor)
            Nodoant = self.cabeza
            while Nodotemp.siguiente != "NULL":
                # print("*/iTer**")
                # Nodotemp.imprimir_siguiente()
                Nodoant = Nodotemp
                Nodotemp = Nodotemp.siguiente

            if Nodotemp.siguiente == "NULL":
                # print(Nodotemp.siguiente)
                Nodoant.asignar_siguiente("NULL")

        else:
            print("NO ES POSIBLE ELIMINAR EL NODO INICIAL")
            time.sleep(2)

        self.indexar()

    def eliminarpos(self, posi):
        # print("------------IMPRESION DE VALORES----------------");
        if self.cabeza.pos != posi:
            if self.cabeza.siguiente != "NULL":
                # print(self.cabeza.valor)

                Nodotemp = self.cabeza.siguiente
                if Nodotemp.pos == posi and Nodotemp.siguiente != "NULL":
                    self.cabeza.asignar_siguiente(Nodotemp.siguiente)
                    Nodotemp.asignar_siguiente("NULL")
                elif Nodotemp.pos == posi and Nodotemp.siguiente == "NULL":
                    self.cabeza.asignar_siguiente("NULL")

                # print(Nodotemp.valor)
                # Nodotemp.pos = 1
                Nodoant = self.cabeza
                while Nodotemp.siguiente != "NULL":
                    # print("*/iTer**")
                    # Nodotemp.imprimir_siguiente()
                    Nodoant = Nodotemp
                    Nodotemp = Nodotemp.siguiente
                    if Nodotemp.pos == posi and Nodotemp.siguiente != "NULL":
                        Nodoant.asignar_siguiente(Nodotemp.siguiente)
                        Nodotemp.siguiente = "NULL"
                    elif Nodotemp.pos == posi and Nodotemp.siguiente == "NULL":
                        Nodoant.asignar_siguiente("NULL")
            else:
                if self.cabeza.pos == posi:
                    print("NO ES POSIBLE ELIMINAR EL NODO INICIAL")
                    time.sleep(2)
        else:
            if self.cabeza.pos == posi and self.cabeza.siguiente == "NULL":
                print("NO ES POSIBLE ELIMINAR EL NODO INICIAL")
                time.sleep(2)
            elif self.cabeza.pos == posi and self.cabeza.siguiente != "NULL":
                Siguiente = self.cabeza.siguiente
                self.cabeza = Siguiente
                #print(" aca estoy BAUTISTA ME VA A MATAR")
            else:
                print("ERROR FATAL!")
        self.indexar()

    def contarnum(self, num):
        # print("------------IMPRESION DE VALORES----------------");
        self.indexar()
        contador = 0
        if self.cabeza.siguiente != "NULL":
            # print(self.cabeza.valor)
            if self.cabeza.valor == num:
                contador = contador + 1

            Nodotemp = self.cabeza.siguiente
            # print(Nodotemp.valor)
            # Nodotemp.pos = 1
            if Nodotemp.valor == num:
                #print("POS ENCO " + Nodotemp.pos)
                contador = contador + 1
            while Nodotemp.siguiente != "NULL":
                #print("*/iTer**")

                # Nodotemp.imprimir_siguiente()
                Nodotemp = Nodotemp.siguiente
                #print("COMPARA " + str(Nodotemp.pos))
                if int(Nodotemp.valor) ==int(num):
                    #print("POS ENCO " + str(Nodotemp.pos))
                    contador = contador + 1
                #else:
                    #print(str(Nodotemp.valor) + " ES DISTINTO DE " + str(num))
                    

        else:
            if self.cabeza.valor == num:
                contador = contador + 1
        print("El numero " + str(num) + " apareció " + str(contador) + " VECES ")
        time.sleep(2)
        # print(self.cabeza.valor)

    def posicion(self, num):
        # print("------------IMPRESION DE VALORES----------------");
        self.indexar()
        
        if self.cabeza.siguiente != "NULL":
            # print(self.cabeza.valor)
            if self.cabeza.valor == num:
                print("NUMERO" + str(num) + "SE ENCUENTRA EN LA POSICION " + str(self.cabeza.pos))

            Nodotemp = self.cabeza.siguiente
            # print(Nodotemp.valor)
            # Nodotemp.pos = 1
            if Nodotemp.valor == num:
                #print("POS ENCO " + Nodotemp.pos)
                print("NUMERO" + str(num) + "SE ENCUENTRA EN LA POSICION " + str(Nodotemp.pos))
            while Nodotemp.siguiente != "NULL":
                #print("*/iTer**")

                # Nodotemp.imprimir_siguiente()
                Nodotemp = Nodotemp.siguiente
                #print("COMPARA " + str(Nodotemp.pos))
                if int(Nodotemp.valor) ==int(num):
                    #print("POS ENCO " + str(Nodotemp.pos))
                    print("NUMERO" + str(num) + "SE ENCUENTRA EN LA POSICION " + str(Nodotemp.pos))
                    

        else:
            if self.cabeza.valor == num:
                print("NUMERO" + str(num) + "SE ENCUENTRA EN LA POSICION " + str(self.cabeza.pos))
        
        time.sleep(2)
        # print(self.cabeza.valor)




####APARTADO DE PRUEBA DEL CODIGO---------------------------------------
#
arreglo_objetos = []
cantidad_objetos = 100
for _ in range(cantidad_objetos):
    objeto = Nodo(0)
    arreglo_objetos.append(objeto)

#
Nodo1 = Nodo(0)

Lista = ListaEnlazada(Nodo1)
# Nodo1.devolver_valor()
# Nodo1.imprimir_siguiente()
# Nodo2.imprimir_siguiente()
Lista.ciclo_sigue()
"""
Nodo2 = Nodo(56)
Lista.agregar_Nodo_Final(Nodo2)
Lista.ciclo_sigue()
Nodo3 = Nodo(75)
Lista.agregar_Nodo_Final(Nodo3)
Lista.ciclo_sigue()
Nodo4 = Nodo(1233)
Lista.agregar_Nodo_Final(Nodo4)
Nodo5 = Nodo(777)
Lista.agregar_Nodo_Final(Nodo5)

Lista.ciclo_sigue()

# print("##############")
# print(Nodo4.imprimir_siguiente())
# print("##############")
# PONER NODOS VOLANDO, AGREGAR AL INICIO
"""
# AGREGAR AL INICIO


# AGREGAR AL FINAL


# ----------------------------------------------------

i = 0
while True:
    print(
        "\033[43m"
        + "\033[34m"
        + "\033[4m"
        + "--------------------------------------------------"
        + "\033[0m"
    )
    print(
        "\033[34m" + "\033[4m" + "       MENU DE OPCIONES                 " + "\033[0m"
    )
    print(
        "\033[43m"
        + "\033[34m"
        + "\033[4m"
        + "--------------------------------------*****---------"
        + "\033[0m"
    )
    print(
        "1. Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista."
    )

    print(
        "2. Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1)."
    )
    print("3.Longitud de la lista: te muestra el número de elementos de la lista.")
    print(
        "4. Eliminar el último número: Muestra el último número de la lista y lo borra."
    )
    print(
        "5. Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1)."
    )
    print(
        "6. Contar números: Te pide un número y te dice cuantas apariciones hay en la lista."
    )
    print(
        "7. Posiciones de un número: Te pide un número y te dice en qué posiciones está (contando desde 1)."
    )
    print("8. Mostrar números: Muestra los números de la lista")
    print("9. Salir")

    choice = input("\033[34m" + "\033[4m" + "Ingrese la opción " + "\033[0m")

    if choice == "1":
        nume = input("Ingresa el número: ")
        arreglo_objetos[i].cambiar_valor(int(nume))
        Lista.agregar_Nodo_Final(arreglo_objetos[i])
        Lista.ciclo_sigue()
        pass
    elif choice == "2":
        nume = input("Ingresa el número  ")
        arreglo_objetos[i].cambiar_valor(nume)
        pose = int(input("Ingresa la posicion  "))
        Lista.añadirpos(arreglo_objetos[i], pose)
        Lista.ciclo_sigue()
        pass
    elif choice == "3":
        Lista.contabilizar()
        time.sleep(5)
        pass
    elif choice == "4":
        Lista.eliminar_ultimo()
        Lista.ciclo_sigue()
        pass
    elif choice == "5":
        pose = int(input("Ingresa la posicion  "))
        Lista.eliminarpos(pose)
        Lista.ciclo_sigue()
        pass
    elif choice == "6":
        pose = int(input("Ingresa EL NUMERO  "))
        Lista.contarnum(pose)
        pass
    elif choice == "7":
        pose = int(input("Ingresa EL NUMERO  "))
        Lista.posicion(pose)


        pass
    elif choice == "8":
        Lista.ciclo_sigue()
        
        pass
    elif choice == "9":
        break
    i = i + 1
print("Saliendo del menú.")
