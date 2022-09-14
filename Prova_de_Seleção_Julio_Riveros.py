def crear_matriz():
	lineas, columnas = map(int,input().split())
	matriz = []
	for i in range(lineas):
		matriz.append(list(input()))
	return matriz, lineas, columnas

def salir_del_laberinto(matriz, lineas, columnas):
	l_actual, c_actual = 1,1
	pasos_totales = []
	pasos = [[1,1]]
	pasos_totales += pasos[:]
	
	while not (l_actual == (lineas-2) and c_actual == (columnas-2)):
		matriz[l_actual][c_actual] = "."
		if matriz[l_actual][c_actual+1] == "_":  #este
			c_actual += 1
			pasos.append([l_actual,c_actual])
			pasos_totales.append([l_actual,c_actual])
			
		elif matriz[l_actual+1][c_actual] == "_":  #sur
			l_actual += 1
			pasos.append([l_actual,c_actual])
			pasos_totales.append([l_actual,c_actual])
			
		elif matriz[l_actual][c_actual-1] == "_":  #oeste
			c_actual -= 1
			pasos.append([l_actual,c_actual])
			pasos_totales.append([l_actual,c_actual])
			
		elif matriz[l_actual-1][c_actual] == "_":  #norte
			l_actual -= 1
			pasos.append([l_actual,c_actual])
			pasos_totales.append([l_actual,c_actual])
			
		else:  #retroceder
			l_actual, c_actual = pasos.pop()
			if matriz[l_actual][c_actual+1] == "_" or matriz[l_actual+1][c_actual] == "_" or matriz[l_actual][c_actual-1] == "_" or matriz[l_actual-1][c_actual] == "_":
				pasos.append([l_actual,c_actual])
	return pasos, pasos_totales
			
_ = int(input())
matriz, lineas, columnas = crear_matriz()
pasos, _ = salir_del_laberinto(matriz, lineas, columnas)
for i in range(len(pasos)):
	print(pasos[i][0],pasos[i][1])