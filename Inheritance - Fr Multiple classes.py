#parent class 1
class Father:
    def __init__(self,name, eyecolor):
        self.name =name
        self.eyecolor = eyecolor
    def hobby(self): # child not have, but will inherit
        print("Likes soccer")

#parent class2:
class Mother:
    def __init__(self,name, eyecolor,height):
        self.name =name
        self.eyecolor = eyecolor
        self.height=height

class Child(Father, Mother):
    #new traits but still inherit
    def __init__(self,name,eyecolor):
        super().__init__(name,eyecolor)
    def talents(self):
        print("Sports and Debate")

halo = Child('Jack', 'Green')
#have talents method and can do it
halo.talents()
#doesn't have hobby method but still can do because inherit from father
halo.hobby()

