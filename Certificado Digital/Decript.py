import Crypto
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

arq = open("Message.txt", "rb")
hash = arq.read(32)
criptHash = arq.read(128)
publicKey = arq.read(162)
key = RSA.importKey(publicKey)

if key.encrypt(criptHash,1024)[0] == hash:
    print("Chave OK!")
    print()
else:
    print("Chave Fail!")
    print()

# Teste com outra chave gerada aleatoriamente:
print("Teste com outra Chave:")
print()

random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
publicKey = key.publickey()

if publicKey.encrypt(criptHash,1024)[0] == hash:
    print("Chave valida!")
    print()
else:
    print("Chave invalida!")
    print()
