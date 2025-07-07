class Person:
    name="puja"
    occupation="software dev"
    networth=130000
    def info(self):# self mane je obj call korbe  info gula dekhabe
        print(f"{self.name} is a {self.occupation}")
a=Person()
b=Person()
c=Person()
print(a.name,a.occupation)
a.name='JO'
a.occupation='bekar'
b.name='Anup'
b.occupation='business'
print(a.name,a.occupation)
a.info()
b.info()
c.info()# c er info dei nai tai by defult ja ache tai hobe
