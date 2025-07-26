from abc import ABC,abstractmethod

class absclass(ABC):

    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass


class dervclass(absclass):
    def method1(self):
        print("method 1 from abs")

    def method2(self):
        print("method 2 from abs")


drv = dervclass()

drv.method2()
drv.method1()