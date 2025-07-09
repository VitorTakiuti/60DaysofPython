def celsius_to_fahrenheit(celsius):
    """
    Convert the temperature from Celsius to Fahrenheit
    
    Arg:
        celsius(float): Temperature C
    
    return;
        float: Temperature F
    """
    
    return round((celsius * 9/5) + 32, 2)

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert the temperature from Fahrenheit to Celsius
    
    Arg:
        Fahreinheit(float): Temperature F
    
    return;
        float: Temperature C
    """
    return round((fahrenheit - 32) * 5/9, 2)

def main(temperature, conversion_type):
    """
    Arg:
        temperature(float):
        conversion_type(str):
        
    Returns:
        float: converted temperature
    """
    if conversion_type == "celsius":
        print(celsius_to_fahrenheit(temperature))
    elif conversion_type == "fahrenheit":
        print(fahrenheit_to_celsius(temperature))
    else:
        return print("Conversion type invalid")
    
if __name__ == "__main__":
    main(20, "celsius")
    main(30, "fahrenheit")
        