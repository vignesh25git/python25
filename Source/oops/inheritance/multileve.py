#a->B->C
#multileverl inheritance

class grandfather:
    def __init__(self):
        print("Grand - Const")

    def villagehouse(self):
        print("Old Village house")

class dad(grandfather):
    def __init__(self):
        super().__init__()
        print("dad - Const")

    def cityhouse(self):
        print(" city house")

class son(dad):
    def __init__(self):
        super().__init__()
        print("son - Const")

    def apartmenthouse(self):
        print(" Aparment house")


g = grandfather()
print(" ")
d = dad()
print(" ")
s = son()
print(" ")
g.villagehouse()
d.cityhouse()
s.apartmenthouse()