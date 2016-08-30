from Crypto.Cipher import AES

# Variáveis do Programa:
message = "A mensagem de 16"
IV = "Criptograficando"
key = "1234567891098765"

# Criptografando a mensagem:
obj1 = AES.new(key, AES.MODE_CBC, IV)
ciphertext = obj1.encrypt(message)
print(ciphertext)

# Descriptografando a mensagem:
obj2 = AES.new(key, AES.MODE_CBC, IV)
deciphertext = obj2.decrypt(ciphertext)
newMessage = deciphertext.decode()
print(newMessage)
