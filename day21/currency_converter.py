def converter(value, exchange_rate, type_convertion):
    """
    This function will convert dollar in real and real in dollar
    
    arg: 
        value: float: Value
        exchange_rate: Current Exchange rate
        type_conversion: dollar -> real and real -> dollar
        
    return: 
        float: converted number rounded 
        
    raise: 
        ValueError: wrong type_convertion
    """
    
    if type_convertion == 'dollar_real':
        return round(value * exchange_rate, 2)
    elif type_convertion == 'real_dollar':
        return round(value / exchange_rate, 2)
    else:
        return ValueError("Wrong convertion type")
    
# 07/07/25 1USD = 5.49 reais
print(converter(12, 5,49, 'dollar_real'))

#from forex_python.converter import CurrencyRates

#c = CurrencyRates()
#valor = c.get_rate('USD', 'BRL')
#print(f"1 USD = R$ {valor:.2f}")
