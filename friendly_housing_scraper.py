from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import os
#setting up our webdriver for firefox (must have geckodriver as an env variable called geckodriver)
path_to_firefoxdriver = os.environ['geckodriver']
browser = webdriver.Firefox(executable_path= path_to_firefoxdriver)
#opening the friendlyhousing website in the browser
url = 'https://friendlyhousing.nl/en/all-rentals'
browser.get(url)
#searching for the listings
mainframe = browser.find_element(By.ID, 'house-list') #flex element containing the listings
#creates a list of elements which are buttons for switching pages
pages = mainframe.find_elements(By.CLASS_NAME, "page") 
#picks the last element of that list (the final page number) and gets its number
last_page = int(pages[-1].text)
#list of ignored exceptions for waiting until elements are loaded
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
#loop over every page
for i in range(last_page):
    #wait until buttons are not stale
    WebDriverWait(browser, 10,ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'page')))
    #updates buttons list (they change upon click)
    pages = mainframe.find_elements(By.CLASS_NAME, "page") 
    #click next button
    pages[i].click()
    #create the list of listings on new page
    new_page_list = mainframe.find_elements(By.CSS_SELECTOR, ".col-xs-12.col-sm-6.col-md-4.equal-col")
    for listing in new_page_list:
        #wait until listings are loaded
        WebDriverWait(browser, 10,ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".query.hidden")))
        address = listing.find_element(By.CSS_SELECTOR, ".query.hidden").get_attribute("textContent")
        price =listing.find_element(By.CSS_SELECTOR, ".price.hidden").get_attribute("textContent")
        #getting the string with the picture link in it
        picture = listing.find_element(By.CSS_SELECTOR, ".image.has-image").get_attribute("style")
        #extracting only the link from the string
        picture_link = re.search('"(.+?)"', picture)
        listing_link = listing.find_element(By.CSS_SELECTOR, ".btn.btn-secondary").get_attribute("href")
        print("address: "+address)
        print("price: "+price)
        print("picture link: "+ picture_link.group(1))
        print("listing link: "+ listing_link)
        print("---------------------")
