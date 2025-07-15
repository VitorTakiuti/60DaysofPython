from bs4 import BeautifulSoup #python3 pip install beautifulsoup4 
import requests 

url = "https://books.toscrape.com" # A book site

response = requests.get(url)
if response.status_code == 200:
    print("The Site was Successfully Connected!" )
else:
    print("Connection Error")
    exit()
    
soup = BeautifulSoup(response.text, "html.parser") # parser the info of the url

# you get the info in the html of the url
#prices = soup.find_all("p", class_= "price_color" ) 

books = soup.find_all("article", class_="product_pod")
for book in books:
    title = book.find("h3").find("a")['title']
    price = book.find("p", class_="price_color")
    stars = book.find("p", class_="star-rating")['class'][1] #this make the code get just the number of stars of each book
    print(f"Title: {title}/ Price: {price}/ Stars: {stars}")

