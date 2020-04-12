import requests
import bs4



url = 'https://www.jumia.com.ng/watches-sunglasses/?q=ladies+watch&page=1'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.content,'html.parser')
html = soup.find_all('div',class_='sku -gallery')
#ENDS HERE    
#f = open('watches.csv','w')
for i in html:
    links  = i.a['href']
    print(links)
    name = i.h2.text
    print(name)
    try:
        price = i.find('div',class_ ='card-sku--price_box js-prices')
        print(price)
    except:
        pass 