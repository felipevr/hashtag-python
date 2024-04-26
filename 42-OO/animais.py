
class Aquatico:
    def nadar(self):
        pass

class Terrestre:
    def andar(self):
        pass

class Anfibio(Terrestre, Aquatico):
    pass



peixe = Aquatico()

gato = Terrestre()

sapo = Anfibio()

print((peixe, gato, sapo))