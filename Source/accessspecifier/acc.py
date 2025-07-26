class access:
    def __init__(self):
        self.publicvar = "public"
        self._protectedvar = "protected"
        self.__privatevar = "private"

    def display(self):
        print("Public ", self.publicvar)
        print("Protected ",self._protectedvar)
        print("Private ",self.__privatevar)

class dervclass(access):
    def __init__(self):
        super().__init__()

a = access()
d = dervclass()


a.display()
d.display()