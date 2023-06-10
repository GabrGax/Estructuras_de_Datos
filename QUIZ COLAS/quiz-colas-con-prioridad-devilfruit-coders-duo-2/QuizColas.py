class Paciente:
    def __init__(self,nom,edad,sinto,grav,pos):
        self.nombre=nom 
        self.edad=edad
        self.sintomas=sinto
        self.gravedad=grav
        self.anterior=None
        self.siguiente=None
        self.posicion=pos
        if(edad<12):
            self.prioridad=10
        elif(edad>65):
            self.prioridad=20
        else:
            self.prioridad=40
            
        self.coeficiente=100*(self.gravedad)+ (1+self.prioridad)+(0.001*pos)
    
    def imprimir(self):
        print("Nombre: ",self.nombre,"Edad: ",self.edad,"Sintomas: ",self.sintomas,"Gravedad: ",self.gravedad)

class Cola:
    def __init__(self):
        self.primero=None
        self.tamano=0
        self.ultimo=None
        self.list=[]
        self.ColaPrioridad=[]

    def vacia(self):
        a=True
        if(self.tamano!=0):
            a=False
        return a
            
    
    def push(self,nom,edad,sinto,grav):
        newNodo=Paciente(nom,edad,sinto,grav,self.tamano)
        if(self.vacia()):
            self.primero=newNodo
            self.ultimo=newNodo
        else:
            actNodo=self.ultimo
            """
            while(actNodo.anterior!=None):
                if(actNodo.gravedad<newNodo.gravedad):
                   if(actNodo.siguiente==None):
                        newNodo.siguiente=None
                   else:
                        newNodo.siguiente=actNodo.siguiente
                   actNodo.siguiente.anterior=newNodo
                   newNodo.anterior=actNodo
                   actNodo.siguiente=newNodo
                actNodo=actNodo.anterior
            """
            if(actNodo.anterior != None):   
                Nodo_temporal= actNodo
                actNodo.siguiente= newNodo
                newNodo.anterior=actNodo
                self.ultimo= newNodo
            elif(actNodo.anterior ==None):
                actNodo.siguiente = newNodo
                newNodo.anterior= actNodo
                self.ultimo = newNodo
                self.primero = actNodo
        self.tamano+=1    
        #if(self.tamano>=2):
        #    self.ordenar()
    def ingresarPaciente(self,nom,edad,sinto,grav):
        Paciente_agregar= Paciente(nom,edad,sinto,grav,self.tamano)
        self.list.append(Paciente_agregar)
        self.tamano=self.tamano+1
        self.ColaPrioridad=sorted(self.list, key=lambda Coef : Coef.coeficiente)
        print("\033[4;35;42m"+"SE HA AÑADIDO CORRECTAMENTE A "+nom+'\033[0;m')
        self.imprimir_cola()
       

    def ordenar(self):
        actNodo=self.primero
        
        if(self.vacia()):
            print("LISTA VACIA")
        else:
            Nodo_inicial= actNodo
            Inicial_tentativo=Nodo_inicial
            Inicial_temporal=None
            Siguiente_temporal=None
            if(self.tamano>=2):
                for i in range(self.tamano-1):
                    print("NODO NUMERO "+ str(i))
                    print("NODO INICIAL PARA EL NÚMERO 1 "+ Nodo_inicial.nombre)
                    for v in range(self.tamano-1):
                        print("######################################################")
                        if(v==0):
                            Inicial_temporal=Nodo_inicial
                        
                        print("ENTRO CON INICIAL "+ Inicial_temporal.nombre)
                        Siguiente_temporal= Inicial_temporal.siguiente
                        print("ENTRO CON SIGUIENTE "+ Siguiente_temporal.nombre)
                        #Fase de comparación por burbujas
                        if(Inicial_temporal.gravedad>Siguiente_temporal.gravedad):
                            BufferIn= Inicial_temporal
                            BufferSi= Siguiente_temporal
                            BufferSisi=BufferSi.siguiente
                            Buffer_anterior_inicial=Inicial_temporal.anterior
                            #Buffer_siguiente_inicial=Inicial_temporal.siguiente
                            Inicial_temporal.anterior=Inicial_temporal.siguiente
                            Inicial_temporal.siguiente=Inicial_temporal.siguiente.siguiente
                            Siguiente_temporal.anterior= Buffer_anterior_inicial
                            Siguiente_temporal.siguiente=Inicial_temporal
                            Bufferv23= Siguiente_temporal
                            Siguiente_temporal=BufferSisi
                            Inicial_temporal= Bufferv23
                            print("///**/*/EL PRE INICIAL TEMPORAL ES "+ Inicial_temporal.nombre)
                            print("///**/*/EL PRE SIGUIENTE TEMPORAL ES "+ Siguiente_temporal.nombre)
                            if(v==0):
                                Inicial_tentativo=Inicial_temporal
                                Nodo_inicial= Inicial_tentativo
                                self.primero=Nodo_inicial
                            print("____Apartado____")
                            self.imprimir()
                            print("____FINApartado____")
                        #elif(Inicial_temporal.gravedad>Siguiente_temporal)
                        
                        #Inicial_temporal=Siguiente_temporal   
                        print("///**/*/EL INICIAL TEMPORAL ES "+ Inicial_temporal.nombre)
                        print("///**/*/EL SIGUIENTE TEMPORAL ES "+ Siguiente_temporal.nombre)
                    print("IMPRESIONNNNNNN ")
                    self.imprimir()
                    print("-------------------------------- "+ Nodo_inicial.nombre)
                    #Nodo_inicial= Inicial_temporal
                 
             
    def imprimir(self):
        actNodo=self.primero
        
        if(self.vacia()):
            print("LISTA VACIA")
        else:
            
            while(actNodo.siguiente!=None):
                actNodo.imprimir()
                actNodo=actNodo.siguiente
            if(actNodo.siguiente == None):
                actNodo.imprimir()    
        print("TAMAÑO DE LA LISTA :",self.tamano)
    def imprimir_cola(self):
        print("\033[1;34m"+"            COLA DE HOSPITAL                "+'\033[0;m')
        for i in range(self.tamano):
            print("         "+"\033[4;31;45m"+self.ColaPrioridad[i].nombre +'\033[0;m'+ " ESTÁ EN LA POSICIÓN "+ str(i+1)+ " DE COLA ")
        print("\033[1;33m"+"---------------------------------------------------"+'\033[0;m')
    def pasar_paciente(self):
        print("SE PASARÁ AL PACIENTE         "+ "\033[4;31;41m"+self.ColaPrioridad[0].nombre +'\033[0;m')
        for i in range(self.tamano):
            if(self.ColaPrioridad[0] == self.list[i-1]):
                self.list.pop(i-1)
                self.tamano= self.tamano-1
        self.ColaPrioridad.pop(0)
        print("\033[1;33m"+"    Imprimir nueva lista con el paciente pasado:"+'\033[0;m')
        self.imprimir_cola()

    
    def eliminar(self):
        self.primero=self.primero.anterior
        self.tamano-=1
    
    def valorsiguiente(self):
        return self.primero
    
cola=Cola()
cola.ingresarPaciente("ADELARDO DE LA ESPRIELLA",23,"RINITIS",3)
cola.ingresarPaciente("PRMANDO BIN LADEN",34,"INFLUENZA",2)
cola.ingresarPaciente("JANSUS KARKOS LOAIZA",17,"BALAZO",1)
cola.ingresarPaciente("ELVIS NIETO",67,"INTOXICACIÓN",4)
cola.ingresarPaciente("JUAN JOSE CALDERON ROJAS",11,"INTOXICACIÓN POR TRAMADOL",4)
cola.ingresarPaciente("FARID CAMILO ROJAS VARGAS",33,"INTOXICACIÓN POR DOLEX",4)
cola.ingresarPaciente("WILSON ACOSTA CHAPARRO",37,"TRANSITO",1)
cola.pasar_paciente()
cola.pasar_paciente()
cola.pasar_paciente()
cola.pasar_paciente()
#METODO PARA IMPRIMIR COLA
print("ESTE ES EL METODO PARA IMPRIMIR LA COLA ACTUAL")
cola.imprimir_cola()

