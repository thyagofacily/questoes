N_NOTAS = 4

def media(notas) -> float:
    soma = 0
    for nota in notas:
        soma += nota
    
    return soma/N_NOTAS

if __name__ == '__main__': 
    notas = [0]*N_NOTAS 

    for i in range(len(notas)):
        notas[i] = float(input("Digite a nota {}:".format(i + 1)))

    resultado = media(notas)
    print("A média do aluno é de {}".format(resultado))