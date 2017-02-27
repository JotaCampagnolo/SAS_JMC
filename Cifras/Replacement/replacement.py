import math
import os
import itertools
import csv

# Cifra de Substituição:
def Replacement(func, keyFile, fileIn, fileOut):
	FileIN = open(fileIn, 'rb').read()
	Key = open(keyFile, 'rb').read()
	out = []
	if func == 'e':	
		for i in FileIN:
			new = Key[i]
			out.append(new)
	else:
		for i in FileIN:
			for j in Key:
				if Key[j] == i:
					new = j
					out.append(new)		
	open(fileOut,"wb").write(bytes(out))

# Main:
Replacement('e', "key", "in.txt", "out.txt") # Encripta o texto.
Replacement('d', "key", "out.txt", "in2.txt") # Decripta o texto.
