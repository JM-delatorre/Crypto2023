import random

def checkIJ(string):
    if string == "IJ":
        return random.choice(["I","J"])
    else:
        return string

def imprimirMatriz(A):
    fila = len(A)
    col = len(A[0])
    for i in range(fila):
        print("| ", end = "")
        for j in range(col):
            print(A[i][j], end = "\t")
        print("|")
    print()

def createMatrix(keyword) -> list:
    keyword = keyword.upper().strip().replace(' ', '')
    M = []
    for i in range(5):
        M.append([0]*5)
    added = []
    i = 0
    j = 0
    for letter in keyword:
        if not(letter in added):
            if letter == "I" or letter == "J":
                M[i][j] = "IJ"
                added.append("I")
                added.append("J")
            else:
                M[i][j] = letter
                added.append(letter)
            if j == 4:
                j = 0
                i+=1
            else:
                j+= 1
            
        if i==4 and j==4:
            break
    abc = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    added = set(added)
    defini = abc.difference(added)
    defini = sorted(list(defini))
    for mislet in defini:
        M[i][j] = mislet
        if j == 4:
            j = 0
            i+=1
        else:
            j+= 1
    return M

def separateEquals(message) -> list:
    newmsg = ""
    i = 0
    while i < len(message)-1:
        newmsg+= message[i]
        if message[i] == message[i+1]:
            newmsg+= 'X'
            i+=1
        else:
            newmsg+= message[i+1]
            i+=2
    
    newmsg+= message[-1]
    if (len(newmsg) % 2 != 0):
        newmsg+= 'X'
    
    newmsg = [newmsg[i:i+2] for i in range(0, len(newmsg), 2)]
    return newmsg

def search(letter1, letter2, matriz):
    point1 = None
    point2 = None
    if letter1 == "I" or letter1 == "J":
        letter1="IJ"
    if letter2 == "I" or letter2 == "J":
        letter2="IJ"
    for i in range(5):
        for j in range(5):
            if matriz[i][j] == letter1:
                point1 = [i,j]
            
            if matriz[i][j] == letter2:
                point2 = [i,j]

            if point1 != None and point2 != None:
                break
    return (point1, point2)


def encrypt(text:str, k:str):
    text = text.upper().strip().replace(' ', '')
    if not text.isalpha():
        print("No es posible encriptar: El mensaje solo debe tener caracteres del alfabeto")
        return
    if not k.isalpha():
        print("No es posible encriptar: La llave solo debe tener caracteres del alfabeto")
        return
    text = separateEquals(text)
    M = createMatrix(k)
    ciphertext = []
    for i in text:
        p1,p2 = search(i[0], i[1], M)
        if p1[0] == p2[0]:
            colp1 = (p1[1]+1) % 5
            colp2 = (p2[1]+1) % 5
            ciphertext.append(checkIJ(str(M[p1[0]][colp1])) + checkIJ(str(M[p2[0]][colp2])))
        elif p1[1] == p2[1]:
            rowp1 = (p1[0]+1) % 5
            rowp2 = (p2[0]+1) % 5
            ciphertext.append(checkIJ(str(M[rowp1][p1[1]])) + checkIJ(str(M[rowp2][p2[1]])))
        else:
            ciphertext.append(checkIJ(str(M[p1[0]][p2[1]])) + checkIJ(str(M[p2[0]][p1[1]])))
        
    print("\n=============================")
    print(" Tu mensaje cifrado es: ")
    print(" ".join(ciphertext))

def decrypt(text:str, k:str):
    text = text.upper().strip().replace(' ', '')
    if not text.isalpha():
        print("No es posible desencriptar: El mensaje solo debe tener caracteres del alfabeto")
        return
    if len(text) % 2 != 0:
        print("No es posible desencriptar: El mensaje encriptado debe tener longitud par")
        return
    if not k.isalpha():
        print("No es posible desencriptar: La llave solo debe tener caracteres del alfabeto")
        return
    text = [text[i:i+2] for i in range(0, len(text), 2)]
    M = createMatrix(k)
    unciphertext = []
    for i in text:
        p1,p2 = search(i[0], i[1], M)
        if p1[0] == p2[0]:
            colp1 = (p1[1]-1) % 5
            colp2 = (p2[1]-1) % 5
            unciphertext.append(checkIJ(str(M[p1[0]][colp1])) + checkIJ(str(M[p2[0]][colp2])))
        elif p1[1] == p2[1]:
            rowp1 = (p1[0]-1) % 5
            rowp2 = (p2[0]-1) % 5
            unciphertext.append(checkIJ(str(M[rowp1][p1[1]])) + checkIJ(str(M[rowp2][p2[1]])))
        else:
            unciphertext.append(checkIJ(str(M[p1[0]][p2[1]])) + checkIJ(str(M[p2[0]][p1[1]])))

    print("\n=============================")
    print(" Tu mensaje descifrado es: ")
    print(" ".join(unciphertext).strip())
    imprimirMatriz(M)


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