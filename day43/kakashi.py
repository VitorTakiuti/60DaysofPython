class Ninja:
    def __init__(self, name, chakra):
        self.name = name
        self.chakra = chakra
        
    def jutsu(self, chakra_cost):
        try:
            if chakra_cost > self.chakra:
                raise ValueError("Not enough Chakra!")
            self.chakra -= chakra_cost
            print(f"{self.nome} used the jutsu and succeeded")
        
        except ValueError as Error:
            print(f"Error: {Error} was detected. {self.name} needs to recover chakra!")
            
if __name__ =="__main__":
    kakashi = Ninja(name="Kakashi", chakra=100)
    kakashi.jutsu(50)