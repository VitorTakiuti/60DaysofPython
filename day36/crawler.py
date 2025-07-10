from bs4 import BeautifulSoup #pick informations of urls 

import requests

url = "https://pt.wikipedia.org/wiki/Star_Wars"

response = requests.get(url)

if response.status_code == 200:
    print("Acess Succeeded" )
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    title = soup.title.string
    print(title)
    
    paragraph_one = soup.find("p").text
    print(paragraph_one) # first paragraph
    print("------------------------------------------------")
    
    paragraphs = soup.find_all("p")
    
    if len(paragraphs) > 1:
        print(paragraphs[1].text) #second paragraph
    
    else:
        print("There is no more paragraphs")
    
    #<a href="url">click here</a>
    
    links = soup.find_all("a", href=True)[:5] #get 5 links of the url page
    
    for link in links:
        print(link["href"])
    
   