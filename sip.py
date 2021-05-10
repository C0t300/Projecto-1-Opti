from random import randint, uniform

#Lectura de parametros
n = int(input('Cantidad de Plantas: '))
d = int(input("Cantidad de Centros de Distribucion: "))

capacidadPlanta = [] # [3, 2, 10]
demandaCentro = []	# [5, 3]
# ---
usoPlanta = [] # [0, 0, 0]
usoCentro = [] # [0, 0]

restrCapacidad = []
restrDemanda = []

for i in range(n):
	cap = randint(1000, 15000)
	capacidadPlanta.append(cap)
	usoPlanta.append(0)

for i in range(d):
	dem = randint(1000, 10000)
	demandaCentro.append(dem)
	usoCentro.append(0)

# Oferta/capacidad
for i in range(n):
	s = ""
	cap = capacidadPlanta[i]
	for i2 in range(d):
		caso = "X" + str(i) + str(i2) + " + "
		s += caso
	s = s[:-2]
	s += "<= " + str(cap)
	restrCapacidad.append(s)

# Demanda	
for i in range(d):
	s = ""
	dem = demandaCentro[i]
	for i2 in range(n):
		caso = "X" + str(i2) + str(i) + " + "
		s += caso
	s = s[:-2]
	s += "= " + str(dem)
	restrDemanda.append(s)

#print(restrCapacidad)
#print(restrDemanda)

minimizacion = "Min "
for i in range(n):
	for i2 in range(d):
		costo = randint(1, 10)
		minimizacion += str(costo) + "X" + str(i) + str(i2) + " + "

minimizacion = minimizacion[:-2]

fin = open("modelo_LINDO.ltx","w")

fin.write(minimizacion)
fin.write("\n")
fin.write("st \n")
for c in restrCapacidad:
	fin.write(c)
	fin.write("\n")
for d in restrDemanda:
	fin.write(d)
	fin.write("\n")

fin.close()