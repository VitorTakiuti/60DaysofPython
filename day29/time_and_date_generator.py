from datetime import datetime
#pip install pytz
#python3 -m pip install pytz
import pytz

def current_date_time():
    """
    Display the date and the time of the moment that someone runs the code
    """
    
    timezone = pytz.timezone("America/Sao_Paulo")
    
    date_time = datetime.now(timezone)
    
    date_format = date_time.strftime("%d/%m/%Y, %H:%M:%S")
    
    print(f"Date and time now: {date_format}")
    
if __name__ == "__main__":
    current_date_time()