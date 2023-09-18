from layout import DECRYPT_LAY
from layout import ENCRYPT_LAY
from random import choice

def encrypt(text:str):
    text = text.upper().strip().replace(' ', '')
    if not text.isalpha():
        print("No es posible encriptar: El mensaje solo debe tener caracteres del alfabeto")
        return
    ciphertext = ""
    for i in text:
        num = choice(ENCRYPT_LAY[i])
        ciphertext += "{} ".format(num)
    print("\n\t=============================")
    print("\tTu mensaje cifrado es: ")
    print("\t",ciphertext, sep="")
    print("\t=============================")

def decrypt(text:str):
    text = text.upper().strip().split()
    if not all(el.isdigit() for el in text):
        print("No es posible desencriptar: El mensaje solo debe tener numeros")
        return
    message = ""
    for i in text:
        letter = DECRYPT_LAY[int(i)]
        message += letter

    print("\n\t=============================")
    print("\tTu mensaje descifrado es: ")
    print("\t",message, sep="")
    print("\t=============================")

user = int(input("Desea encriptar o desencriptar\n 1.Encriptar\n 2.Desencriptar\n -> "))
if int(user) == 1:
    message = input("Ingrese el mensaje para cifrar: ")
    encrypt(message)
elif int(user) == 2:
    message = input("Ingrese el mensaje para descifrar: ")
    decrypt(message)
else:
    print("Porfavor ingrese una opcion valida")

