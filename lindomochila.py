from random import randint, uniform

#Lectura de parametros
n = int(input('Cantidad de Productos: '))
utilidad = []
disponibilidad = []

#Generacion Aleatoria de parametros (Beneficio y Disponibilidad)
w = randint(30,50)

print ('\nDisponibilidad')
for i in range(n):
    value = randint(5,15)
    disponibilidad.append(value)
    print ("d_" + str(i+1), "=" , value)

print ('\nUtilidad')
for i in range(n):
    value = randint(4, 10)
    utilidad.append(value)
    print ("u_" + str(i+1), "=" , value)


#Generación del Modelo
print ('\n-LINDO-Modelo')

##Funcion Objetivo
objective_function = "max "
for i in range(n):
    objective_function += str(utilidad[i]) + "x" + str(i+1)
    if i<n-1:
        objective_function+=" + "
    else:
        objective_function += "\n"
print (objective_function)


#Restricciones  (st: subject to)
constraints = "st\n"
for i in range(n):
    constraints += "x" + str(i+1)
    if i<n-1:
        constraints+=" + "
constraints += " <= " + str(w) + "\n"

for i in range(n):
    constraints += "x" + str(i+1) + " <= " + str(disponibilidad[i]) + "\n"

constraints += "\n"

for i in range(n):
    constraints += "x" + str(i+1) + " >= 0\n"

print (constraints)

#Generacion de archivo .lp (para LPsolve)
fin = open("modelo_LINDO.ltx","w")

fin.write(objective_function)
fin.write("\n")
fin.write(constraints)

fin.close()