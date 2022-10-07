import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#url of the page to scrape
url = "https://www.takealot.com/russell-hobbs-2200w-crease-control-iron/PLID34147865"
# initiating the webdriver
driver = webdriver.Chrome('./chromedriver') 
driver.get(url)

html = driver.page_source
#Apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")
#Finding elements
div_availability  = soup.find('div', {'class' : 'cell shrink stock-availability-status'})
availability = div_availability .find('span')

div_seller = soup.find('div',{'class': 'seller-information'})
seller= div_seller.find('span')

div_price = soup.find('div',{'class': 'buybox-module_price_2YUFa'})
price = div_price.find('span')

next_offer_price = soup.find('span', {'class' : 'currency plus currency-module_currency_29IIm'}) 

next_offer_availability = soup.find('div',{'class': 'cell shrink stock-availability-status'})
next_availability = next_offer_availability.find('span')



print("Availability: ", availability.text)
print("Seller : ", seller.text)
print("Price: ", price.text)
print("Next offer price: ", next_offer_price.text)
print("Next offer availability: ", next_offer_availability.text)


driver.close()