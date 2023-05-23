import numpy as np
import random
Estudiantes = np.zeros((6500, 5))


for i in range(6500):
    numero_aleatorio = random.randint(2200000, 2300000)
    Estudiantes[i,0]=numero_aleatorio
#LLENAR NOMBRES 
nombres = ["Juan_Castro", "María_Rodríguez", "Pedro_García", "Lucía_Fernández", "Carlos_González",
           "Laura_Martínez", "Jorge_Sánchez", "Ana_Pérez", "Luis_Ruiz", "Marina_Mendoza", 
           "Andrés_Carrasco", "Sofía_Gil", "Diego_López", "Luna_Díaz", "Mario_Santos", "Isabel_Alvarez",
           "Daniel_Ramírez", "Valeria_Morales", "Emilio_Torres", "Paula_Gómez", "Rubén_Navarro", 
           "Adriana_Marín", "Bruno_Castro", "Marta_Ferrer", "Antonio_Dominguez", "Lorena_Castro", 
           "Francisco_Méndez", "Alicia_Moya", "David_Rojas", "Fernanda_Cruz", "Javier_Pérez", 
           "Natalia_Pinto", "Oscar_Garrido", "Camila_Vega", "José_López", "Aurora_Rojas", 
           "Juan_Paredes", "Carmen_Sosa", "Alberto_Calvo", "Daniela_Aguilar", "Miguel_Durán", 
           "Alejandra_Benitez", "Enrique_Castro", "Carla_Martín", "Víctor_Torres", "Julia_Vargas", 
           "Luisa_García", "Santiago_Serrano", "Mariana_Cardenas", "Manuel_Lozano", "Valentina_Rivas", 
           "Felipe_Herrera", "Renata_Muñoz", "Ricardo_Vásquez", "Vanessa_Castro", "César_Torres", 
           "Esther_Salazar", "Maximiliano_Acosta", "Nataly_García", "Mateo_Carrillo", "Constanza_Rodriguez",
           "Gonzalo_Castro", "Claudia_Pacheco", "Tomás_Díaz", "Fabiana_Hernández", "Lautaro_Gómez",
           "Julieta_Ramírez", "Guillermo_Méndez", "Brenda_Velasco", "Leonardo_Campos", "Cecilia_Parra", 
           "Ramón_Martínez", "Jimena_Cortés", "Raúl_Soto", "Florencia_Vega", "Andrés_Suárez", 
           "Victoria_Rojas", "Gustavo_Guzmán", "Alma_Castro", "Federico_Hernández", "Micaela_Alvarez",
           "René_Ponce", "Luciana_Morales", "Francisco_Rodríguez", "Ana_López", "Sebastián_Martínez", 
           "Daniela_Silva", "Cristóbal_Flores", "Irene_Castro", "Agustín_Gutiérrez", "Elena_Aguilar"]
#Estudiantes[:, 1] = Estudiantes[:, 1].astype(str)
for i in range(6500):
     numero_aleatorio2 = random.randint(0, 80)
     Estudiantes[i,1]=numero_aleatorio2


#PONDERADO
for i in range(6500):
     numero_aleatorio3 = random.randint(0,5)
     Estudiantes[i,2]=numero_aleatorio3
carreras= ["SISTEMAS", "INDUSPARTY","MEDICINA"]
#CARRERA
for i in range(6500):
     numero_aleatorio3 = random.randint(0,2)
     Estudiantes[i,3]=numero_aleatorio3
#ANO EN EL QUE ENTRO
for i in range(6500):
     numero_aleatorio3 = random.randint(1970,2022)
     Estudiantes[i,4]=numero_aleatorio3

print(Estudiantes)

for i in range(1,6499):
     promed=Estudiantes[i,2]
     promed=promed.astype(int)
     if promed >= 4:
          indice1 = Estudiantes[i,1]
          indice2 = Estudiantes[i,3]
          indice0 = Estudiantes[i,0]
          indice1=indice1.astype(int)
          indice2=indice2.astype(int)
          indice0=indice0.astype(int)
          #print(carreras[indice2])
          print("1.#####--------------------------------------------------------------------#####")
          print("### CODIGO",Estudiantes[i,0] , "  EL ESTUDIANTE ", nombres[indice1], "  DE LA CARRERA ",carreras[indice2], "  TIENE PROMEDIO POND. MAYOR O IGUAL A 4 con ", Estudiantes[i,2] )
          print("####----------------------------------------------------------------------#####")


for i in range(1,6499):
     promed=Estudiantes[i,2]
     promed=promed.astype(int)
     anho=Estudiantes[i,4]
     anho=anho.astype(int)
     if promed <= 3 and anho<1990:
          indice1 = Estudiantes[i,1]
          indice2 = Estudiantes[i,3]
          indice0 = Estudiantes[i,0]
          indice1=indice1.astype(int)
          indice2=indice2.astype(int)
          indice0=indice0.astype(int)
          #print(carreras[indice2])
          print("2.--------------------------------------------------------------------------------")
          print("CODIGO",Estudiantes[i,0] , "  EL ESTUDIANTE CONDICIONAL ", nombres[indice1], "  DE LA CARRERA ",carreras[indice2], "  TIENE PROMEDIO POND. MENOR O IGUAL A 3 Y CUYO PROMEDIO ES ", Estudiantes[i,2] ," Y ESTA DESDE EL ANHO ",Estudiantes[i,4] )
          print("---------------------------------------------------------------------------------------")



print("GABRIEL DAVID CASTILLO RODRIGUEZ --- 2220055")