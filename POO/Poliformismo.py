class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def acelerar(self):
        pass

    def frear(self):
        pass

class Carro(Veiculo):
    def acelerar(self):
        print('O carro está acelerado')

    def frear(self):
        print('O carro está freando')

class Moto(Veiculo):
    def acelerar(self):
        print('A moto está acelerada')

    def frear(self):
        print('A moto está freando')

class Aviao(Veiculo):
    def acelerar(self):
        print('O avião está acelerando')

    def frear(self):
        print('O avião está freando')

    def decolar(self):
        print('O avião está decolando')

# Definição da lista de veículos
lista_veiculos = [Carro("Porsche", "911 turbo"), Moto("Honda", "CB 1000R Black Edition"), Aviao("Boeing", "757")]

# Iteração sobre a lista de veículos
for veiculo in lista_veiculos:
    veiculo.acelerar()
    veiculo.frear()

    if isinstance(veiculo, Aviao):
        veiculo.decolar()
        print("---")

# Verificando o tipo da lista
print(type(lista_veiculos))
