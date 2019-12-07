class SistemaSolar:

    #diametro, vertices, distancia do sol, qtdeSatelites, r,g,b
    def __init__(self):
        self.sol = 100, 50, 0, 255, 255, 0
        self.mercurio = 2.8, 50, 58, 192, 192, 192
        self.venus = 7.0, 50, 108, 218, 165, 32
        self.terra = 7.3, 50, 150, 0, 0, 255
        self.marte = 3.9, 50, 228, 255, 0, 0
        self.jupiter = 82.3, 50, 778, 222, 184, 135
        # +60 satelites
        self.saturno = 69.4, 50, 1429, 0, 0, 0
        # 53 satelites
        self.urano = 29.4, 50, 2871, 224, 255, 255
        self.netuno = 28.5, 50, 4504, 77, 124, 241
        # 27 satelites
        self.plutao = 1.3, 50, 5914, 173, 165, 153
        self.lua = 2.2, 50, 130, 192, 192, 192
        self.planetas = [self.sol, self.mercurio, self.venus, self.terra, self.marte, self.jupiter, self.saturno, self.urano, self.netuno, self.plutao, self.lua]

    def get_planetas(self):
        return self.planetas