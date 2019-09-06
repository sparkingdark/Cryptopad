from cryptography.fernet import Fernet
# Put this somewhere safe!
def encrypt():
    i=input("enter some text:")
    K = Fernet.generate_key()
    print(K)
    f = Fernet(K)
    print(f)
    token = f.encrypt(bytes(i,encoding='UTF-8'))
    print(token)
    print(f.decrypt(token))

encrypt()    
