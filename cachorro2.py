class Cachorro:
    def __init__(self):
        self.energia = 100 # Inicializa a energia com 100

        def brincar(self):
            if self.energia >= 20:
                self.energia -= 20 # Reduz 20 pontos de energia
                print("O cachorro brincou! Energia restante: ", self.energia)
            else:
                print("O cachorro está muito cansado para brincar")

        def dormir(self):
            self.energia = 100 # Restaura a energia para 100
            print("O cachorro dormiu e recuperou a energia!")

# Exemplo de uso:
dog = Cachorro()
dog.brincar()  # brinca e reduz energia
dog.brincar