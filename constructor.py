
class europe:
    '''its a default consturctor no argument'''
    def __init__(self):
        print(" Its my childhood dream to study aborad")
puja=europe()
joy=europe()
# this is perameterised
class USA:
    '''its a default consturctor no argument'''
    def __init__(self,name,occ):
        print(" Its my childhood dream to take my bapi ma to USA ")
        self.na=name
        self.o=occ
    def info(self):
        print(f"{self.na} dreams profession is {self.o}")
        money=20
p=USA("monty","engineer")
p.info()
y=USA("Anup","business")
y.info()
