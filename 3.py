
#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no
# vetor PAR e os números ÍMPARES no vetor ímpar. Imprima os três vetores.

N_INT = 20

class App: 

    def __init__(self) -> None:
        self._numbers =  []*N_INT
        self._pair = Pair()
        self._odd = Odd()

    def execute(self):
        i = 1 
        while i <= N_INT:
            number  = int(input("Digite o numero {} :".format(i)))
            self._numbers.append((number))
            pair = self._pair.is_par(number)
            if not pair :
                self._odd.set_number(number)

            i += 1
        print("Todos os numeros são >> {}".format(self._numbers))
        print("Os numeros pares são >>> {}".format(self._pair.get_vector))
        print("Os numeros impares são >>>> {}".format(self._odd.get_vector))
        
class Pair():

    def __init__(self) -> None:
        self._pair = []

    def is_par(self, number:int) -> bool:
        if number %2 == 0:
            self._pair.append(number)

            return True
        
        return False

    @property
    def get_vector(self):
        return self._pair

class Odd:

    def __init__(self) -> None:
        self._odd = []

    def set_number(self, number: int) -> None :
        self._odd.append(number)

    @property
    def get_vector(self):
        return self._odd


aplication = App()
aplication.execute()