import math
import os
import itertools

# Cifra de Ceaser:
def Ceaser(func, key, fileIn, fileOut):
	FileIN = open(fileIn, 'rb').read()
	out = []
	for i in FileIN:
		if func == 'e':		
			new = (i+key) % 256
		else:
			new = (i-key) % 256		
		out.append(new)
	open(fileOut,"wb").write(bytes(out))

# Main:
Ceaser('e', 1, "in.txt", "out.txt") # Encripta o texto.
Ceaser('d', 1, "out.txt", "in2.txt") # Decripta o texto.
