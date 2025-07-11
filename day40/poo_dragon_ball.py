class CharacterDB: 
    #Self make sure that every class has its own values, without interfering in the others
    def __init__(self, name, power, level, transformation="Base"):
        """
        Inicialize characteres attributes
        self garanti that the attributes are unique
    
        """
        self.name = name
        self.power = power
        self.level = level
        self.transformation = transformation 
    
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Power: {self.power}")
        print(f"Level: {self.level}")
        print(f"Transformation: {self.transformation}")
        
    def training(self, hours):
        """
        it will level up the characters based on the amount of hours trained
        """
        powerup = hours * 10 
        self.power += powerup
        print(f"{self.name}, trained for {hours} and powerup his power level in {powerup}!")
        
    def transform(self, new_transformation):
        
        self.transformation = new_transformation
        print(f"{self.name} transformed in {new_transformation}")
  
#Testing the code with Goku and Vegeta with some info      
goku = CharacterDB(name="Goku", power="9000", level="Super Saiyajin")
goku.show_info
        
vegeta = CharacterDB(name="Vegeta", power="8500", level="Saiyajin")
vegeta.training(hours=10)
vegeta.transform(new_transformation="Super Saiyajin 2")
vegeta.show_info