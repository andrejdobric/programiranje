import math

class kvadrat:

    def __init__(self, stran):
        self.stran = stran

    def povrsina(self):
        return f"Povrsina kvadrata je:{self.stran*self.stran}"

    def obim(self):
        return f"Obim kvadrata je:{self.stran+self.stran}\n"


class krug:

    def __init__(self, polp):
        self.polp = polp

    def povrsina(self):
        return f"Povrsina kruga je:{round(self.polp*self.polp*math.pi,2)}"

    def obim(self):
        return f"Obim kruga je:{round(2*self.polp*math.pi,2)}\n"


class pravougaonik:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def obim(self):
        return f"Obim pravougaonika je:{2*self.a+2*self.b}\n"

    def povrsina(self):
        return f"Povrsina pravougaonika je:{self.a*self.b}"


if __name__ == '__main__':
    kvad = kvadrat(5)
    krg = krug(5)
    prv = pravougaonik(5,10)
    print(kvad.povrsina())
    print(kvad.obim())
    print(krg.povrsina())
    print(krg.obim())
    print(prv.povrsina())
    print(prv.obim())
