import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random

# Geração da Chave Privada e da Chave Pública:
randomGenerator = Random.new().read
privateKey = RSA.generate(1024, randomGenerator)
publicKey = privateKey.publickey()
