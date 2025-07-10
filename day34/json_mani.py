import json
from typing import Any

def save_data(archive: str, data: Any) -> None:
    """
    Save data in a JSON file 
    
    Path to the JSON file
    """
    
    with open(archive, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        
def load_data(archive: str) -> Any:
    """
    Thisa Function will load the data in the JSON file
    
    return: Loaded Data
    """
    try:
        with open(archive, 'r', encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("The JSON file was not found. File Path: {archive}")
        return {}

data_example = {"name": "Vitor", "city": "Sao Paulo", "job": "Bioinformatic"}

archive_name = "name_vitor.json"

save_data(archive_name, data_example)

loaded_data = load_data(archive_name)

print("Loaded data: ", loaded_data)    