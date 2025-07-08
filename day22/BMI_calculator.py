def calculate_bmi():
    """
    Function that calculates the bmi of a person
    
    """
    
    print("Welcome to the BMI Calculator")
    
    try: 
        weight = float(input("Please Type your Weight in Kilograms: "))
        
        height = float(input("Plaese Type you Height in Meters: "))
        
        if weight < 0 or height < 0:
            print("Weight and Height Must be higher than 0!")
            return
        
        bmi = round(weight / (height ** 2), 2)
        
        if bmi < 18.5:
            print("You are under the ideal weight for your height")
        elif 18.5 <= bmi < 24.9:
            print("You are in the ideal weight for your height")
        elif 25 <= bmi < 29.9:
            print("You are overweight for your height")
        else:
            print("You are obese")
            
    except ValueError:
        print("The entry is invalid")

#running th code internally
#only runs if i Run my script calculate_bmi        
if __name__ == "__main__":
    calculate_bmi()