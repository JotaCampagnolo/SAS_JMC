base = 5
modulus = 23

pvtKey = int(input("Informe uma Chave Privada: "))

print((base ** pvtKey) % modulus)

intKey = int(input("Informe a Chave Intermediaria: "))

print("Chave Compartilhada:", (intKey ** pvtKey) % modulus)

input("Precione ENTER para continuar!")
