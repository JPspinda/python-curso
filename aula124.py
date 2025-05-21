class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
        
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando...')
            return
        
        print(f'{self.nome} está filmando...')
        self.filmando = True
        
    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} nãp está filmando...')
            return
        
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False
        
    def fotografar(self):
        if self.filmando:
            print(f'Não pode fotografar filmando.')
            return
        
        print(f'{self.nome} está fotografando')

camera_1 = Camera('Canon')
camera_2 = Camera('Sony')
camera_1.filmar()
camera_1.parar_filmar()
camera_1.fotografar()
print()
camera_2.parar_filmar()
camera_2.fotografar()
camera_2.filmar()
camera_2.fotografar()