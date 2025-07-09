def write_file(file_name, content):
    """
    Write the content in a txt file
    
    Arg: 
    name_file(str): The name for the file created 
    content(str): The text writed in the file
    """
    
    with open(file_name, 'w') as archive: 
        archive.write(content)
        
    print(f"The content was saved in the file: {file_name}")
    
def file_read(file_name):
    """
    Let me read the file
    """
    try:
        with open(file_name, 'r') as archive: 
            content = archive.read()
        print(f"Content of the file: {content}")
    
    except FileNotFoundError:
        print("File was not found, try again")
        
def main(file_name, content):
    """
    Main function that shows what is writed in the file
    
    Arg:
    name_file(str): The name for the file created 
    content(str): The text writed in the file
    """
    
    print("Welcome to my program that writes and reads files")
    
    write_file(file_name, content)
    
    print("Reading file...")
    file_read(file_name)
    
if __name__ == "__main__":
    archive = "example.txt"
    text = "@vtr_ot on Instagram, Follow me !"
    
    main(archive, text)