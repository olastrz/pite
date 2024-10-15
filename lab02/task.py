class Matrix:

    def __init__(self, a, b, c, d):
       self.a = a
       self.b = b
       self.c = c
       self.d = d

    def add(self, other):
        if isinstance(other, Matrix):
            return Matrix(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)
        else:
            return Matrix(self.a + other, self.b + other, self.c + other, self.d + other)
        
    def __matmul__(self, other):
        if isinstance(other, Matrix):
            return Matrix(self.a * other.a, self.b * other.b, self.c * other.c, self.d * other.d)
        else:
            return Matrix(self.a * other, self.b * other, self.c * other, self.d * other)
        
    def __str__(self):
        return(f"[[{self.a}, {self.b}' {self.c}, {self.d}]]")

    def __repr__(self):
        return self.__str__()
    

m1 = Matrix(1,2,3,4)
m2 = Matrix(1,2,3,5)

print(m1 + m2)
print(m1 + 3)
    

  
