from cryptography import fernet

class Fernet:
    def encrypt():
        i = input("Enter some text:")
        key = fernet.Fernet.generate_key()
        print('Key: ', key)
        
        f = fernet.Fernet(key)
        token = f.encrypt(bytes(i,encoding='UTF-8'))

        return [key, token]

    def decrypt(key, token):
        print('Key: ', key)
        print('Token: ', token)

        f = fernet.Fernet(key)

        print(f.decrypt(token))
        return (f.decrypt(token))

arr = Fernet.encrypt()
Fernet.decrypt(arr[0], arr[1])
