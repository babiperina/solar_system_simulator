class SistemaSolar:

    #diametro, vertices, distancia do sol, qtdeSatelites
    def __init__(self):
        self.STACKS = 50
        self.sol = 42, self.STACKS, 0, 0
        self.mercurio = 1.4, self.STACKS, 58, 0
        self.venus = 3.5, self.STACKS, 108, 0
        self.terra = 3.65, self.STACKS, 150, 1 # 1
        self.marte = 1.7, self.STACKS, 228, 2 # 2
        self.jupiter = 41.15, self.STACKS, 778, 63 # 63
        self.saturno = 34.7, self.STACKS, 1429, 49  #49
        self.urano = 14.7, self.STACKS, 2871, 27 #27
        self.netuno = 14.25, self.STACKS, 4504, 13 #13
        self.plutao = 0.65, self.STACKS, 5914, 0
        self.lua = 1.1, self.STACKS, 130, -1
        self.planetas = [self.mercurio, self.venus, self.terra, self.marte, self.jupiter, self.saturno, self.urano, self.netuno, self.plutao]
        self.satelites = []

    def get_sol(self):
        return self.sol

    def get_planetas(self):
        return self.planetas

    def get_satelites(self):
        tamanho = self.lua[0]
        for p in self.get_planetas():
            distancia = p[2]
            # print(p)
            satelites = p[3]
            if satelites > 3:
                satelites = 3
            for x in range(satelites):
                self.satelites.append([tamanho, self.STACKS, distancia+(x*10)])
        return self.satelites

    def get_sistema_solar(self):
        sistema = []
        sistema.append(self.sol)
        # sistema.append(self.lua)
        for x in self.planetas:
            sistema.append(x)
        # for x in self.get_satelites():
        #     sistema.append(x)
        return sistema