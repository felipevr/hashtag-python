
class Aquatico:
    def __init__(self):
        super().__init__()
        print("1 nada")

    def nadar(self):
        pass

class Terrestre:
    def __init__(self):
        super().__init__()
        print("2 anda")

    def andar(self):
        pass

class Anfibio(Terrestre, Aquatico):

    def __init__(self):
        super().__init__()
        print("3 nada e anda")

    pass

class Mamifero():
    def mamar(self):
        pass
    def amamentar(self):
        pass

class Aves():
    def __init__(self):
        super().__init__()
        print("4 voa")
        
    def voar(self):
        pass

class Cachorro(Mamifero, Terrestre):
    pass

peixe = Aquatico()

gato = Terrestre()

sapo = Anfibio()

auau = Cachorro()

print((peixe, gato, sapo, auau))