#it has sha256,aes algorithm.
#a bug is not converted aes strings in multiple of 16

from Crypto.Hash import SHA256
from Crypto.Cipher import AES
#from Crypto import Random

cryp_sha256=SHA256.new()
a=input("enter your message to encrypt:")
cryp_sha256.update(bytes(a,encoding='UTF-8'))
print(cryp_sha256.digest())

'''cryp_aes = AES.new('This is a key123', AES.MODE_ECB, 'This is an IV456')
message=input("enter another text of multiple of 16:")
mess=[]
for i in message:
    if len(mess)<=16:
        mess.append(i)
ciphertext=[]
cryp_aes.encrypt(bytes(" ".join(mess),encoding="UTF_8"))'''
