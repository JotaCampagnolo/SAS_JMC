import math
import os
import itertools

# Cifra de Vigenere:
def Vigenere(func, key, fileIn, fileOut):
	FileIN = open(fileIn, 'rb').read()
	out = []
	vKey = key
	vKey = vKey.encode()
	count = 0
	for i in FileIN:
		if func == 'e':		
			out.append((i + vKey[count]) % 256)
		else:
			out.append((i - vKey[count]) % 256)
		count += 1
		if count >= len(vKey):
			count = 0
	open(fileOut,"wb").write(bytes(out))

# Main:
Vigenere('e', "key", "in.txt", "out.txt") # Encripta o texto.
Vigenere('d', "key", "out.txt", "in2.txt") # Decripta o texto.
