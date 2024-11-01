class CmplxNumber:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def __str__(self):   # This magic method will be called when object prints
        if (self.real==0):
            return f"{self.img}i"
        if (self.img<0):
            s = f"({self.real} {self.img}i)"
        else:
            s = f"({self.real} + {self.img}i)"
        return s

    def __add__(self, other):
        resultReal = 0
        resultImg = 0

        resultReal = self.real + other.real
        resultImg = self.img + other.img

        ad = CmplxNumber(resultReal,resultImg)
        return ad

    def __sub__(self, other):
        resultReal = self.real - other.real
        resultImg = self.img - other.img

        su = CmplxNumber(resultReal, resultImg)
        return su

    def __eq__(self, other):
        return (self.real==other.real) and (self.img==other.img)

    def conjugate(self):
        return CmplxNumber(self.real,-1*self.img)



cn1 = CmplxNumber(3,5)
cn2 = CmplxNumber(6,7)

print(cn1+cn2)
print(cn1-cn2)
print(cn1==cn2)
#print(cn1.conjugate())

