def encrypt(text:str, key:str):
    text = text.upper().strip().replace(' ', '')
    key = key.upper().strip().replace(' ', '')
    if len(text) != len(key):
        print("No es posible encriptar con esta llave: no tiene la misma longitud del mensaje")
        return
    elif not text.isalpha():
        print("No es posible encriptar: El mensaje solo debe tener caracteres del alfabeto")
        return
    elif not key.isalpha():
        print("No es posible encriptar: La llave solo debe tener caracteres del alfabeto")
        return
    ciphertext = " "
    for i in range(len(text)):
        x = ((ord(text[i])-65) + (ord(key[i])-65)) % 26
        ciphertext += chr(x+65)
        if(i % 5 == 0 and i != 0):
            ciphertext += " "
    print("\n=============================")
    print(" Tu mensaje cifrado es: ")
    print(ciphertext)

def decrypt(text, key):
    text = text.upper().strip().replace(' ', '')
    key = key.upper().strip().replace(' ', '')
    if len(text) != len(key):
        print("No es posible desencriptar con esta llave: no tiene la misma longitud del mensaje")
        return
    elif not text.isalpha():
        print("No es posible desencriptar: El mensaje solo debe tener caracteres del alfabeto")
        return
    elif not key.isalpha():
        print("No es posible desencriptar: La llave solo debe tener caracteres del alfabeto")
        return
    message = " "
    for i in range(len(text)):
        x = ((ord(text[i])-65) - (ord(key[i])-65)) % 26
        message += chr(x+65)
        if(i % 5 == 0 and i != 0):
            message += " "
    print("\n=============================")
    print(" Tu mensaje descifrado es: ")
    print(message)

user = int(input("Desea encriptar o desencriptar\n 1.Encriptar\n 2.Desencriptar\n -> "))
if int(user) == 1:
    message = input("Ingrese el mensaje para cifrar: ")
    key = input("Ingrese la llave: ")
    encrypt(message, key)
elif int(user) == 2:
    message = input("Ingrese el mensaje para descifrar: ")
    key = input("Ingrese la llave: ")
    decrypt(message, key)
else:
    print("Porfavor ingrese una opcion valida")


