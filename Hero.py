import random
class general:
    def __init__(self):
        self.numb = id(self)
        self.team = random.randint(1,2)
 
class soldier(general):
    def follow_hero(self, hero = 0):
        print(f'Soldier with id {id(self)} follows Hero with id{id(hero)}')
        return(id(hero), id(self))

class hero(general):
    level = 0
    def __init__(self, team):
        general.__init__(self)
        self.team = team
    def level_up(self):
        self.level += 1
Ironman = hero(1)
Copperman = hero(2)
Ironman_team = []
Copperman_team = []
for i in range(int(input("Enter the number of soldiers "))):
    i = soldier()
    if i.team == 1:
        Ironman_team .append(i)
    else:
        Copperman_team.append(i)
if len(Ironman_team) > len(Copperman_team):
    Ironman.level_up()
    print('Ironman levels up')
elif len(Ironman_team) < len(Copperman_team):
    Copperman.level_up()
    print('Copperman levels up')
else:
    print("Same number of soldiers")

print(Ironman_team[0].follow_hero(Ironman))


  