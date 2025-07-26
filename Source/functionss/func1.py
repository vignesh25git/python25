def add(a=0,b=0):
    c = a+b
    return c

def add1(*args):
    total  = 0
    for num in args:
        total += num
    return total

def createprofile(**kwargs):
    for key,value in kwargs.items():
        print(f'key is {key} and value is {value} ')



#print(add(10,10))
#print(add(1))
#print(add())