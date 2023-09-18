def fillWordToLen(word:str, n:int):
    if len(word) % n == 0:
        return word * int(n/len(word))
    else:
        finalstr = word * int(n/len(word))
        for i in range(n-len(finalstr)):
            finalstr += word[i]
        return finalstr

def encrypt(text:str, key:str, t: int):
    text = text.upper().strip().replace(' ', '')
    key = key.upper().strip().replace(' ', '')
    if not text.isalpha():
        print("No es posible encriptar: El mensaje solo debe tener caracteres del alfabeto")
        return
    elif not key.isalpha():
        print("No es posible encriptar: La llave solo debe tener caracteres del alfabeto")
        return
    if len(text) > len(key):
        key = fillWordToLen(key, len(text))
    else:
        key = key[0:len(text)]
    ciphertext = ""
    for i in range(len(text)):
        if i % t == 0 and i != 0:
            ciphertext += " "
        x = (ord(text[i])-65 + ord(key[i])-65) % 26
        ciphertext += chr(x+65)
    print("\n\t=============================")
    print("\tTu mensaje cifrado es: ")
    print("\t",ciphertext, sep="")
    print("\t=============================")

def decrypt(text:str, key:str, t: int):
    text = text.upper().strip().replace(' ', '')
    key = key.upper().strip().replace(' ', '')
    if not text.isalpha():
        print("No es posible desencriptar: El mensaje solo debe tener caracteres del alfabeto")
        return
    elif not key.isalpha():
        print("No es posible desencriptar: La llave solo debe tener caracteres del alfabeto")
        return
    if len(text) > len(key):
        key = fillWordToLen(key, len(text))
    else:
        key = key[0:len(text)]
    message = ""
    for i in range(len(text)):
        if i % t == 0 and i != 0:
            message += " "
        x = (ord(text[i])-65 - ord(key[i])-65) % 26
        message += chr(x+65)

    print("\n\t=============================")
    print("\tTu mensaje descifrado es: ")
    print("\t",message, sep="")
    print("\t=============================")

while(True):
    user = int(input("Desea encriptar o desencriptar\n 1.Encriptar\n 2.Desencriptar\n 3.Salir\n-> "))
    if int(user) == 1:
        message = input("Ingrese el mensaje para cifrar: ")
        key = input("Ingrese la llave: ")
        espace = int(input("Ingrese el parametro t(tamaño de los bloques): "))
        encrypt(message, key, espace)
    elif int(user) == 2:
        message = input("Ingrese el mensaje para descifrar: ")
        key = input("Ingrese la llave: ")
        espace = int(input("Ingrese el parametro t(tamaño de los bloques): "))
        decrypt(message, key, espace)
    elif int(user) ==3:
        print("Bye")
        break
    else:
        print("Porfavor ingrese una opcion valida")
