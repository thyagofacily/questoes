# Faça um Programa que peça duas notas de 5 alunos, calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

N_ALUNOS = 5
N_NOTAS = 2

class Aluno:

    def __init__(self, nota1: float , nota2: float) -> None:
        self._nota1 =  nota1
        self._nota2 = nota2 

    @property
    def get_media(self) :
        return (self._nota1 + self._nota2)/ N_NOTAS



class App:

    def __init__(self) -> None:
        self._alunos  =  []*N_ALUNOS

    def execute(self) -> None :

        for i in range(N_ALUNOS):
            nota1 = float(input("Digite a nota 1 do aluno {}: ".format(i)))
            nota2 = float(input("Digite a nota 2 do aluno {}: ".format(i)))
            
            self._alunos.append(Aluno(nota1, nota2))

        approved = 0
        for aluno in self._alunos:
            if aluno.get_media >= 7.0: 
                approved += 1

        print("{} Alunos tiveram média >= 7".format(approved))


app = App()
app.execute()