class Livro():
    def __init__(self):
        self.titulo = "Sapiens - Uma Breve História da Humanidade"
        self.isbn = 99888888
        print("Construtor chamado para criar um objeto desta classe.")

    def imprime(self):
        print("Foi criado o livro {} com ISBN {}".format(self.titulo, self.isbn))

Livro1 = Livro()
Livro1.imprime()
