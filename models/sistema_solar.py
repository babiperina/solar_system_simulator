class SistemaSolar:

    #diametro, vertices, distancia do sol, qtdeSatelites, r,g,b
    def __init__(self):
        self.sol = 400, 50, 0, 255, 255, 0
        self.mercurio = 1.4, 50, 58, 192, 192, 192
        self.venus = 3.5, 50, 108, 218, 165, 32
        self.terra = 3.65, 50, 150, 0, 0, 255
        self.marte = 1.7, 50, 228, 255, 0, 0
        self.jupiter = 41.15, 50, 778, 222, 184, 135
        # +60 satelites
        self.saturno = 34.7, 50, 1429, 0, 0, 0
        # 53 satelites
        self.urano = 14.7, 50, 2871, 224, 255, 255
        self.netuno = 14.25, 50, 4504, 77, 124, 241
        # 27 satelites
        self.plutao = 0.65, 50, 5914, 173, 165, 153
        self.lua = 1.1, 50, 130, 192, 192, 192
        self.planetas = [self.sol, self.mercurio, self.venus, self.terra, self.marte, self.jupiter, self.saturno, self.urano, self.netuno, self.plutao, self.lua]

    def get_planetas(self):
        return self.planetas