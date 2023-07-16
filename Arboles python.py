class Nodo:
    def __init__(self, datos):
        self.datos = datos
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, datos):
        nuevo_nodo = Nodo(datos)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar(nuevo_nodo, self.raiz)

    def _insertar(self, nuevo_nodo, nodo_actual):
        if nuevo_nodo.datos < nodo_actual.datos:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = nuevo_nodo
            else:
                self._insertar(nuevo_nodo, nodo_actual.izquierda)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = nuevo_nodo
            else:
                self._insertar(nuevo_nodo, nodo_actual.derecha)

    def obtener_peso(self):
        if self.raiz is None:
            return 0
        else:
            return self._obtener_peso(self.raiz)

    def _obtener_peso(self, nodo_actual):
        if nodo_actual is None:
            return 0
        else:
            return 1 + self._obtener_peso(nodo_actual.izquierda) + self._obtener_peso(nodo_actual.derecha)

    def obtener_orden(self):
        if self.raiz is None:
            return 0
        else:
            return self._obtener_orden(self.raiz)

    def _obtener_orden(self, nodo_actual):
        if nodo_actual is None:
            return 0
        else:
            return 1 + max(self._obtener_orden(nodo_actual.izquierda), self._obtener_orden(nodo_actual.derecha))

    def obtener_altura(self):
        if self.raiz is None:
            return 0
        else:
            return self._obtener_altura(self.raiz)

    def _obtener_altura(self, nodo_actual):
        if nodo_actual is None:
            return 0
        else:
            return 1 + max(self._obtener_altura(nodo_actual.izquierda), self._obtener_altura(nodo_actual.derecha))
    def recorrer_orden(self):
        self._recorrer_orden(self.raiz, "")

    def _recorrer_orden(self, nodo_actual, indent=""):
        if nodo_actual:
            self._recorrer_orden(nodo_actual.izquierda, indent + "    ")
            print(indent + "└──", "\033[92m" + str(nodo_actual.datos) + "\033[0m")
            self._recorrer_orden(nodo_actual.derecha, indent + "    ")

arbol = Arbol()
datos = input("Ingresa los datos para el árbol: ")
while datos != "SALIR" and datos != "":
    arbol.insertar(int(datos))
    datos = input("Ingresa los datos para el árbol: ")
print("EL PESO ES:", arbol.obtener_peso())
print("EL ORDEN ES:", arbol.obtener_orden())
print("LA ALTURA ES:", arbol.obtener_altura())

#RECORRIDO CON RECURSIVIDAD
print("Recorrido en orden:")
arbol.recorrer_orden()
