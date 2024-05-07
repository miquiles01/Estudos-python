#SuperClass
class Animal:
    def __init__(self):
        print('Animal criado.')

    def imprimir(self):
        print('Este é um animal.')

    def comer(self):
        print('Hora de comer.')

    def emitir_som(self):
        pass

#Herança
class Cachorro(Animal):
    def __init__(self):
        super().__init__()
        print('Objeto cachorro criado.')

    def emitir_som(self):
        print('Au au')

    def brincar(self):
        print('O cachorro está brincando.')

class Gato(Animal):
    def __init__(self):
        super().__init__()
        print('Objeto gato criado')

    def emitir_som(self):
        print('Miau')

    def dormir(self):
        print('O gato está dormindo.')

# Criando instâncias das classes Cachorro e Gato
rex = Cachorro()
whiskers = Gato()

# Chamando métodos dos objetos
rex.imprimir()   
whiskers.comer() 
rex.emitir_som() 
whiskers.emitir_som() 
rex.brincar()    
whiskers.dormir() 
