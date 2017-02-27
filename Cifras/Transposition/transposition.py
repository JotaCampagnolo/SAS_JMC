import math
import os
import itertools

# Cifra de Transposição:
def Transposition(func, key, fileIn, fileOut):
	FileIN = open(fileIn, 'rb').read()
	fileSize = os.path.getsize(fileIn)
	cols = math.ceil(fileSize / key)
	if func == 'e':	
		matrix = [ [] for x in range(key)]
	else:
		matrix = [ [] for x in range(cols)]
	count = 0
	if func == 'e':		
		left = cols - (fileSize % cols)
		FileIN = list(FileIN) + [0] * left
	for i in FileIN:
		matrix[count].append(i)
		count += 1
		if func == 'e':		
			if count >= key:
				count = 0
		else:
			if count >= cols:
				count = 0
	out = []
	for i in matrix:
		for j in i:
			out.append(j)
	open(fileOut,"wb").write(bytes(out))

# Main:
Transposition('e', 15, "in.txt", "out.txt") # Encripta o texto.
Transposition('d', 15, "out.txt", "in2.txt") # Encripta o texto.
