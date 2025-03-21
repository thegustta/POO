class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0
        self.combustivel = 100
        self.ligado = False

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}, Velocidade: {self.velocidade}, Combustível: {self.combustivel}, Ligado: {self.ligado}"

    def ligar(self):
        if self.combustivel > 0:
            self.ligado = True
            print(f"O Carro {self.modelo} está LIGADO!")
        else:
            print("Não há COMBUSTÍVEL suficiente para Ligar o Carro.")

    def desligar(self):
        if self.velocidade == 0:
            self.ligado = False
            print(f"O Carro {self.modelo} está DESLIGADO!")
        else:
            print("Não é possível Desligar o Carro enquanto ele estiver em MOVIMENTO!.")

    def acelerar(self):
        if self.ligado and self.combustivel > 0:
            self.velocidade += 10
            self.combustivel -= 5
            print(f"Acelerando... Velocidade: {self.velocidade} km/h. Combustível: {self.combustivel}%")
        elif self.combustivel <= 0:
            print("Não há COMBUSTÍVEL suficiente para ACELERAR!.")
        elif not self.ligado:
            print("O Carro está DESLIGADO. Ligue o Carro para ACELERAR!!!.")

    def frear(self):
        if self.velocidade >= 10:
            self.velocidade -= 10
            print(f"Freiando... Velocidade: {self.velocidade} km/h.")
        else:
            self.velocidade = 0
            print(f"Carro parado. Velocidade: {self.velocidade} km/h.")

    def abastecer(self):
        self.combustivel = 100
        print(f"O {self.modelo} foi Abastecido. Combustível atual: {self.combustivel}.")

    def buzinar(self):
        print("BEEP! BEEP!")

    def status(self):
        status_ligado = "Ligado" if self.ligado else "Desligado"
        print(f"Modelo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}, Combustível: {self.combustivel}%, Velocidade: {self.velocidade} km/h, Status: {status_ligado}")

# Instanciando dois carros
carro1 = Carro("Chevrolet", "Equinox", "2024", "Azul")
carro2 = Carro("Fiat", "Uno", "2025", "Branco")

# Chamando os Métodos
carro1.status()
carro1.ligar()
carro1.acelerar()
carro1.abastecer()
carro1.acelerar()
carro1.frear()
carro1.buzinar()
carro1.desligar()