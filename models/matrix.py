from abstracoes.abstract_matrix import AbstractMatrix


class Matrix(AbstractMatrix):
    """
            This class was used to represent a matrix
            by:Bárbara Perina
        """

    MSG_DIFFERENT_SIZES = "The matrixs doesn't have the same size"

    def __getitem__(self, key):
        i, j = key
        return self.data[(j - 1) + (i - 1) * self.cols]

    def __setitem__(self, key, value):
        try:
            i, j = key
            self.data[(j - 1) + (i - 1) * self.cols] = value
        except:
            print(Exception, " occurred")

    def __repr__(self):
        return str(self)

    def __str__(self):
        matrix = "";
        for row in range(1,self.rows+1):
            for col in range(1,self.cols+1):
                # matrix = matrix + "(row:" + str(row+1) + " column:" + str(col+1) + "): "
                matrix = matrix +  str(self[row,col]) + "\t"
            matrix = matrix + "\n"
        return matrix

    # other + matrix
    def __radd__(self, other):
        return self + other

    # matrix + other
    def __add__(self, other):
        res = Matrix(self.rows, self.cols)
        if(type(other) == Matrix):
            # print("Add self.matrix with: \n" + str(other))
            if self.rows != other.rows or self.cols != other.cols:
                print(self.MSG_DIFFERENT_SIZES)
                return  "error __add__ matrix"
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i, j] = self[i, j] + other[i, j]
        else:
            # print("Add self.matrix with a scale number: " + other)
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i, j] = self[i, j] + other
        return res

    # other - matrix
    def __rsub__(self, other):
        return self - other

    # matrix - other
    def __sub__(self, other):
        res = Matrix(self.rows, self.cols)
        if(type(other) == Matrix):
            # print("Sub self.matrix with: \n" + str(other))
            if self.rows != other.rows or self.cols != other.cols:
                print(self.MSG_DIFFERENT_SIZES)
                return "error __sub__ matrix"
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i, j] = self[i, j] - other[i, j]
        else:
            # print("Sub self.matrix with a scale number: " + other)
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i, j] = self[i, j] - other
        return res

    # other * matrix
    def __rmul__(self, other):
        return self * other

    # matriz * other
    def __mul__(self, other):
        res = Matrix(self.rows, self.cols)
        if (type(other) == Matrix):
            # print("Mul self.matrix with: \n" + str(other))
            if self.rows != other.rows or self.cols != other.cols:
                print(self.MSG_DIFFERENT_SIZES)
                return "error __mul__ matrix"
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i, j] = self[i, j] * other[i, j]
        else:
            # print("Mul self.matrix with a scale number: " + other)
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i, j] = self[i, j] * other
        return res

    # other / matriz
    def __rtruediv__(self, other):
        return self / other
    # matriz / other
    def __truediv__(self, other):
        res = Matrix(self.rows, self.cols)
        if (type(other) == Matrix):
            # print("Truediv self.matrix with: \n" + str(other))
            if self.rows != other.rows or self.cols != other.cols:
                print(self.MSG_DIFFERENT_SIZES)
                return "error __truediv__ matrix"
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i, j] = self[i, j] / other[i, j]
        else:
            # print("Truediv self.matrix with a scale number: " + other)
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i, j] = self[i, j] / other
        return res

    # self * other
    def dot(self, other):
        if(type(other) == Matrix):
            if(self.cols != other.rows):
                return "matrix A must be the same amount of columns as amount matrix B rows amount"
            res = Matrix(self.rows, other.cols)
            for col in range(1, self.cols + 1):
                for row in range(1, self.rows + 1):
                    for othercol in range(1, other.cols + 1):
                        res[row, othercol] += self[row, col] * other[col, othercol]
            return res
        else:
            return "the dot method only works between matrixs"

    # other * self
    def rdot(self, other):
        if(type(other) == Matrix):
            if(self.rows != other.cols):
                return "matrix A must be the same amount of columns as amount matrix B rows amount"
            res = Matrix(self.rows, other.cols)
            for col in range(1, other.cols + 1):
                for row in range(1, other.rows + 1):
                    for selfcol in range(1, self.cols + 1):
                        res[row, selfcol] += other[row, col] * self[col, selfcol]
            return res
        else:
            return "the dot method only works between matrixs"

    def transpose(self):
        res = Matrix(self.cols, self.rows)

        for i in range(1, self.rows + 1):
            for j in range(1, self.cols + 1):
                res[j, i] = self[i, j]

        return res

    def gauss_jordan(self):
        """Aplica o algoritmo de Gauss Jordan na matriz

        Aplica o método de Gauss-Jordan na matriz corrente. Pode ser utilizado para resolver
        um sistema de equações lineares, calcular matrix inversa, etc.

        "Returns:
            Retorna a matrix resultante da operação, por exemplo:

            #> a = Matrix(3,4,[1, -2, 1, 0, 0, 2, -8, 8, 5, 0, -5, 10])
            #> a
                1.0000   -2.0000   1.0000   0.0000
                0.0000    2.0000  -8.0000   8.0000
                5.0000    0.0000  -5.0000   10.0000
            #> c = a.gauss_jordan()
            #> c
                1.0000    0.0000   0.0000   1.0000
                0.0000    1.0000   0.0000   0.0000
                0.0000    0.0000   1.0000  -1.0000
        """
        pass

    def inverse(self):
        """Calcula a matriz inversa da matriz corrente

        Realiza o calculo da matrix inversa utilizando o algoritmo de Gauss-Jordan.

        "Returns:
            Retorna a matrix resultante da operação, por exemplo:

            #> a = Matrix(2,2,[1, 2, 3, 4])
            #> a
                1.0000   -2.0000   1.0000   0.0000
                0.0000    2.0000  -8.0000   8.0000
                5.0000    0.0000  -5.0000   10.0000
            #> c = a.inverse()
            #> c
                -2.0000   1.0000
                1.5000   -0.5000

        """
        pass

    def translate(self, x, y, z = 0):
        if z == 0:
            T = Matrix(3, 3, [1, 0, x, 0, 1, y, 0, 0, 1])
        else:
            T = Matrix(4, 4, [1,0,0,x,0,1,0,y,0,0,1,z,0,0,0,1])

        return T
