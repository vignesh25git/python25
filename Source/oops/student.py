class student:
    def __init__(this,name,age):
        this.name = name
        this.age = age

    def say_hello(self):
        print("Welcome to class")

    def display(this):
        print(f'name is {this.name} and age is {this.age}')

s1 = student("Vignesh",42)
s1.say_hello()
s1.display()