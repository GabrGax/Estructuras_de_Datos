class Monticulo:
    def __init__(self):
        self.heap = [0]
        self.tamano = 0

    def flotar(self, k):
        while True:
            if k // 2 > 0:
                if self.heap[k] < self.heap[k // 2]:
                    self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]
                k = k // 2
            else:
                break

    def insertar(self, elemento):
        self.heap.append(elemento)
        self.tamano += 1
        self.flotar(self.tamano)

    def hundir(self, k):
        while True:
            if k * 2 <= self.tamano:
                mc = self.hijoMin(k)
                if self.heap[k] > self.heap[mc]:
                    self.heap[k], self.heap[mc] = self.heap[mc], self.heap[k]
                k = mc
            else:
                break

    def hijoMin(self, k):
        if k * 2 + 1 > self.tamano:
            return k * 2
        else:
            if self.heap[k * 2] < self.heap[k * 2 + 1]:
                return k * 2
            else:
                return k * 2 + 1

    def eliminarMin(self):
        valor = self.heap[1]
        self.heap[1] = self.heap[self.tamano]
        self.tamano -= 1
        self.heap.pop()
        self.hundir(1)
        return valor

    def construirMonticulo(self, lista):
        i = len(lista) // 2
        self.tamano = len(lista)
        self.heap = [0] + lista[:]
        while i > 0:
            self.hundir(i)
            i -= 1

    def preorden(self, i=1):
        if i <= self.tamano:
            print(self.heap[i])
            self.preorden(i*2)
            self.preorden(i*2+1)

    def porNiveles(self):
        for i in range(1, len(self.heap)):
            print(self.heap[i])
#implementacion de gatitos
class Gatito:
    def __init__(self, nombre, ternura):
        self.nombre = nombre
        self.ternura = ternura

    def __lt__(self, other):
        return self.ternura < other.ternura

    def __str__(self):
        return f"{self.nombre} ({self.ternura})"

gatitos = Monticulo()
gatitos.insertar(Gatito("Pelusa", 8))
gatitos.insertar(Gatito("Bigotes", 9))
gatitos.insertar(Gatito("Manchas", 7))
gatitos.insertar(Gatito("Tigre", 6))

print("Gatitos en orden de ternura:")
gatitos.porNiveles()
