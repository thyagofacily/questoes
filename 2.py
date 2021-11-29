# Faça um Programa que leia uma string e diga quantas consoantes foram lidas. Imprima as consoantes

if __name__ == '__main__':

    vogal = {"a","e","i","o","u"}

    word  = input("Digite a palavra: ").lower()
    consoantes = ""

    for letter in word:
        if letter not in vogal:
            consoantes += letter 

    print("Foram lidos {} consoantes:".format(len(consoantes)))
    print("A palavra possui as seguintes consoantes: {}".format(consoantes))