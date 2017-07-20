class Enemy:
      def __init__(self, x): 
          self.energy = x

      def get_energy(self):
          print(self.energy)

jason = Enemy(5)
jason2= Enemy(50)

jason.get_energy()
jason2.get_energy()
