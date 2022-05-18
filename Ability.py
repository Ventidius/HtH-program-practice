import random
class Ability:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
  def __init__(self, name, max_damage):
    

     self.name = name
    
     self.ma_damage = max_damage
  
  def attack(self):
      dps = random.randrange(0, self.max_damage)
      print(dps)
      return dps
ability = Ability("",)


   
   
