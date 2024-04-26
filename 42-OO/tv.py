
class TV:

    cor = 'preta'

    def __init__(self, tamanho = 55, tipo='Tubo'):
        self.ligada = False
        self.tamanho = tamanho #polegadas
        self.canal = 'Netflix'
        self.volume = 10
        self.tipo = tipo

    def ligar(self, ligar = True):
        self.ligada = ligar

    def mudar_canal(self, canal):
        if not self.ligada:
            raise Exception('TV não está ligada!')
        self.canal = canal



class TV_Plasma(TV):

    def __init__(self, tamanho):
        super().__init__(tamanho=tamanho, tipo='Plasma')
        #self.tipo = 'plasma'


tv_sala = TV(24, tipo='LED')
tv_sala2 = TV(44)
tv_quarto = TV_Plasma(75)

tv_sala.ligar()
tv_sala.cor = 'branca'
tv_sala.mudar_canal('Disney Plus')

print(tv_sala.cor)
print(tv_sala.canal)
print(tv_sala.tamanho)
print(tv_sala.tipo)

print(tv_sala2.cor)

tv_quarto.ligar()
print(tv_quarto.cor)
print(tv_quarto.tipo)
print(tv_quarto.canal)
print(tv_quarto.tamanho)


