# Ejemplo 1-4: Verificar si un elemento está presente en una lista

def contiene(data, objetivo = 0):
	for item in data:
		if item == objetivo:
			return True
	return False
