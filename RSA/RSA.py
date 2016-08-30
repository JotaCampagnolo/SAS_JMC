import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random

# Geração da Chave Privada e da Chave Pública:
randomGenerator = Random.new().read
privateKey = RSA.generate(1024, randomGenerator)
publicKey = privateKey.publickey()

# Criptografando com a Chave Pública:
encrypted = publicKey.encrypt(str.encode('Mensagem a ser criptografada!'),1024)
print ('Encrypted Message:', encrypted)

# Descriptografando com a Chave Privada:
decrypted = privateKey.decrypt(encrypted)
print ('Decrypted Messsage:', decrypted.decode())
