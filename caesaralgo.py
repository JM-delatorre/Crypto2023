
def encrypt(text:str, k:int):
    text = text.upper().strip().replace(' ', '')
    if not text.isalpha():
        print("No es posible encriptar: El mensaje solo debe tener caracteres del alfabeto")
        return
    ciphertext = " "
    for i in text:
        num = ((ord(i)-65)+ k) % 26
        ciphertext += chr(num+65)
        if(len(ciphertext) % 5 == 0 ):
            ciphertext += " "
    print("\n=============================")
    print(" Tu mensaje cifrado es: ")
    print(ciphertext)

def decrypt(text:str, k:int):
    text = text.upper().strip().replace(' ', '')
    if not text.isalpha():
        print("No es posible desencriptar: El mensaje solo debe tener caracteres del alfabeto")
        return
    message = " "
    for i in text:
        num = ((ord(i)-65)- k) % 26
        message += chr(num+65)
        if(len(message) % 5 == 0 ):
            message += " "
    print("\n=============================")
    print(" Tu mensaje descifrado es: ")
    print(message)

user = int(input("Desea encriptar o desencriptar\n 1.Encriptar\n 2.Desencriptar\n -> "))
if int(user) == 1:
    message = input("Ingrese el mensaje para cifrar: ")
    k = int(input("Ingrese el parametro k: "))
    encrypt(message, k)
elif int(user) == 2:
    message = input("Ingrese el mensaje para descifrar: ")
    k = int(input("Ingrese el parametro k: "))
    decrypt(message, k)
else:
    print("Porfavor ingrese una opcion valida")






'''
OTRA FORMA DE ALGORITMO

x = input().upper().strip().replace(' ', '')
k = int(input())
new = ""
for i in x:
    if ord(i) + k > ord('Z'):
        num = ord('A') + ((k-1) -(ord('Z')- ord(i)))
        new += chr(num)
    else:
        new += chr(ord(i)+k)

print(new)
'''