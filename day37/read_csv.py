import pandas as pd

def main():
    file_name = "test.csv"
    
    df = pd.read_csv(file_name) # ,sep=";" inform the separator of the data in the csv file otherwise it will be readed as ","by default")
    
    print(df)
    
    print(df.head()) #show the first 5 lines
    
    print(df.info()) #show dataframe info 
    
    print(df.shape) #show the df shape
    
if __name__ == "__main__":
    main()