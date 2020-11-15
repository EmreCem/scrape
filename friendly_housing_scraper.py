from selenium import webdriver
from selenium.webdriver.common.by import By
import re
#setting up our webdriver for firefox
path_to_firefoxdriver = 'C:/Users/20175159/Desktop/GeckoDriver/geckodriver.exe'
browser = webdriver.Firefox(executable_path= path_to_firefoxdriver)
#opening the friendlyhousing website in the browser
url = 'https://friendlyhousing.nl/en/all-rentals'
browser.get(url)
#searching for the listings
mainframe = browser.find_element(By.ID, 'house-list') #flex element containing the listings
listings = mainframe.find_elements(By.CSS_SELECTOR, ".col-xs-12.col-sm-6.col-md-4.equal-col") #listing cards

#printing selected data out of listings (need to use get_attribute function because elements are hidden divs)
for listing in listings:
    address = listing.find_element(By.CSS_SELECTOR, ".query.hidden").get_attribute("textContent")
    price = listing.find_element(By.CSS_SELECTOR, ".price.hidden").get_attribute("textContent")
    #getting the string with the picture link in it
    picture = listing.find_element(By.CSS_SELECTOR, ".image.has-image").get_attribute("style")
    #extracting only the link from the string
    picture_link = re.search('"(.+?)"', picture)
    print(address)
    print(price)
    print(picture_link.group(1))
