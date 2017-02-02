import Crypto
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
publicKey = key.publicKey()

msg = open("Barney.jpg",'rb').read()
hash = SHA256.new(msg).digest()
criptHash = key.decrypt(hash)

arq = open("Message.txt", "wb")
arq.write(hash)
arq.write(criptHash)
arq.write(publickey.exportKey("DER"))
