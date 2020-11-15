from selenium import webdriver
from selenium.webdriver.common.by import By
#setting up our webdriver for firefox
path_to_firefoxdriver = 'C:/Users/20175159/Desktop/GeckoDriver/geckodriver.exe'
browser = webdriver.Firefox(executable_path= path_to_firefoxdriver)
#opening the friendlyhousing website in the browser
url = 'https://friendlyhousing.nl/en/all-rentals'
browser.get(url)
#searching for the listings
mainframe = browser.find_element(By.ID, 'house-list')
listings = mainframe.find_elements(By.CSS_SELECTOR, ".col-xs-12.col-sm-6.col-md-4.equal-col")

#finding the data out of hidden divs
for listing in listings:
    address = listing.find_element(By.CSS_SELECTOR, ".query.hidden").get_attribute("textContent")
    price = listing.find_element(By.CSS_SELECTOR, ".price.hidden").get_attribute("textContent")
    print(address, price)