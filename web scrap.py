#import libraries
import requests
from bs4 import BeautifulSoup

#base url which you want to scrap
base_url = ('https://www.politifact.com/subjects/marriage/')

#Make a get request to server
r = requests.get(base_url)

#check the server response
print(r)

#initialize the soup object
soup = BeautifulSoup(r.text, 'html.parser')

#define the HTML table and class
table=soup.find('section', class_="scoretable")


text = table.findAll('p',class_="statement__text")
text1 = table.findAll('a',class_="link")
for item in text1:
    tex = item.contents[0]
    print(tex)
    
