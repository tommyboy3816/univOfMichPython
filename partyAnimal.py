class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, z):
        #print("EAT SHIT {}".format
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)
#        print("So far", self.x, " - {}".format(self))

    def __del__(self):
        print("EATEN!!")

class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)


an = PartyAnimal("Peter")
an.party()
an2 = FootballFan("Emily")

an.party()
an2.party()
an.party()
an2.touchdown()
an2.party()
an2.touchdown()



print("type", type(an))
print("dir", dir(an2))
