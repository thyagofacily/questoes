# Faça um Programa que leia as idades e alturas de 10 alunos e determine quantos alunos com mais de 13 anos
# possuem altura inferior à média de altura desses alunos.

N_ALUNOS = 10

class Aluno:

    def __init__(self, idade: int , altura: float , id: int) -> None:
        self._idade = idade
        self._altura = altura
        self._id = id

    @property
    def get_idade(self):
        return self._idade

    @property
    def get_altura(self):
        return self._altura
    
    @property
    def get_id(self):
        return self._id


class App:

    def __init__(self) -> None:
        self._alunos  =  []*N_ALUNOS


    def altura_media(self) -> float:
        soma = 0
        for aluno in self._alunos:
            soma += aluno.get_altura
        
        return soma/N_ALUNOS

    def select_alunos(self, altura_media):
        selected = []
        for aluno in self._alunos:
            if aluno.get_idade > 13 and aluno.get_altura < altura_media : 
                selected.append(aluno._get_id)

        return selected

    def execute(self) -> None :

        for i in range(N_ALUNOS):
            idade = int(input("Digite a idade do aluno {}: ".format(i)))
            altura = float(input("Digite a altura do aluno {}: ".format(i)))
        
            self._alunos.append(Aluno(idade, altura, i))
 
        selected_alunos = self.select_alunos(self.altura_media()) 
        print("Os alunos maiores de 13 anos com a altura menor que a média são: {}".format(selected_alunos))
    


app = App()
app.execute()

