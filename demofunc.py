class Dog():
    def __init__(self,breed,name):
        self.breed=breed
        self.name=name
    def fam(self):
        print("I am "+self.name)
obj=Dog("Lab","tommy")
obj.fam()
print(obj.breed)
print(obj.name)
