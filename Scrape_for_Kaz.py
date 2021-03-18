import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import subprocess
import os
import openpyxl
from openpyxl import Workbook, load_workbook
from openpyxl.styles.borders import Border, Side
import Intro
if Intro.yes != True:
    exit()
from interface import *
if yes != True:
    exit()
import itertools

# Find a path of a driver file
driver_path = os.path.dirname(os.path.abspath(__file__))
driver_file = os.path.join(driver_path, "chromedriver.exe")
driver = webdriver.Chrome(driver_file)

url = "https://spiritleaf.ca/"

driver.get(url)

# Age selection
try:
    province = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.NAME, "country"))
    )
    province = Select(driver.find_element_by_name("country"))
    province.select_by_value(province_final)
    month = driver.find_element_by_name("month")
    month.send_keys(month_final)
    day = driver.find_element_by_name("day")
    day.send_keys(day_final)
    year = driver.find_element_by_name("year")
    year.send_keys(year_final)
    submit = driver.find_element_by_xpath('//*[@id="age-gate"]/div/div/form/button')
    submit.click()
except:
    driver.quit()

# Switching to locations page
try:
    locations = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/header/div/div[4]/a"))
    )
    locations.click()
except:
    driver.quit()

# Choosing a city
try:
    city = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "wpsl-search-input"))
    )
    city = driver.find_element_by_id("wpsl-search-input")
    city.send_keys("Kelowna")
    apply = driver.find_element_by_id("wpsl-search-btn")
    apply.click()
except:
    driver.quit()

# Choosing a specific store
if store_final == "Kelowna, British Columbia – Cannabis Store":
    store_number = "1094"
elif store_final == "West Kelowna – Cannabis Store":
    store_number = "1090"
seq_num = 0
store = WebDriverWait(driver, 5).until(
EC.presence_of_element_located((By.XPATH, '//*[@id="wpsl-stores"]/ul'))
)
sleep(5)
for i in store.find_elements_by_tag_name('li'):
    seq_num += 1
    li = i.get_attribute('data-store-id')
    if li == store_number:
        link = driver.find_element_by_xpath('//*[@id="wpsl-stores"]/ul/li[%s]/div/p[1]/strong/a'%seq_num)
        link.click()
        break

# Switching to iframe
try:
    iframe = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'dutchie--embed__iframe'))
    )
    driver.switch_to.frame(iframe)
except:
    driver.quit()

# Chossing a product type (flower, rolls etc)
if product_final == "Flower":
    product_type = '//*[@id="main-content"]/div[2]/div/div/div[2]/div/div/div/div[1]/a'
elif product_final == "Rolls":
    product_type = '//*[@id="main-content"]/div[2]/div/div/div[2]/div/div/div/div[2]/a'
elif product_final == "Vaporizers":
    product_type = '//*[@id="main-content"]/div[2]/div/div/div[2]/div/div/div/div[3]/a'
elif product_final == "Concentrates":
    product_type = '//*[@id="main-content"]/div[2]/div/div/div[2]/div/div/div/div[4]/a'
elif product_final == "Edibles":
    product_type = '//*[@id="main-content"]/div[2]/div/div/div[2]/div/div/div/div[5]/a'
elif product_final == "Tinctures":
    product_type = '//*[@id="main-content"]/div[2]/div/div/div[2]/div/div/div/div[6]/a'
elif product_final == "Topicals":
    product_type = '//*[@id="main-content"]/div[2]/div/div/div[2]/div/div/div/div[7]/a'
elif product_final == "Seeds":
    product_type = '//*[@id="main-content"]/div[2]/div/div/div[2]/div/div/div/div[8]/a'
elif product_final == "Accessories":
    product_type = '//*[@id="main-content"]/div[2]/div/div/div[2]/div/div/div/div[9]/a'

try:
    product = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, product_type))
    )
    product.click()
except:
    driver.quit()

# Scraping function (iterates through pages, products, product prices, weights and discounts)
def scrape(row):

    elems = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"desktop-product-list-item__Container")]'))
    )
    elems = driver.find_elements_by_xpath('//div[contains(@class,"desktop-product-list-item__Container")]')

    for elem in elems:
        row += 1
        html = elem.get_attribute("outerHTML")
        soup = BeautifulSoup(html, "html.parser")
        name = soup.find('span', class_ = re.compile('desktop-product-list-item__ProductName')).text
        weights = soup.find_all('span', class_ = re.compile('weight-tile__Label'))
        finance = soup.find_all('div', class_ = re.compile('desktop-product-list-item__TileContainer'))

        wb["Sheet"][f"A{row}"] = name

        for weight, prices in itertools.zip_longest(weights, finance): # weights and finance lists might be of different size, thus, in order to iterate until the longest list is exhausted, we use itertools module
            if weight != None:
                wb["Sheet"][f"G{row}"] = weight.text
            price = prices.find_all('span', class_ = re.compile('weight-tile__PriceText'))
            for i in price:
                if i != None:
                    wb["Sheet"][f"H{row}"] = i.text
            discount = prices.find_all('div', class_ = re.compile('weight-tile__DiscountLabel'))
            for i in discount:
                if i != None:
                    wb["Sheet"][f"I{row}"] = i.text
            row += 1
        wb.save(filename = f'{path}\{product_final}.xlsx')                   

    if  driver.find_elements_by_xpath('//*[@id="main-content"]/div[2]/div[2]/nav/button[2]') != []: # checks if there is a "next" button
        if driver.find_element_by_xpath('//*[@id="main-content"]/div[2]/div[2]/nav/button[2]').is_enabled(): # checks if the "next" button can be pressed
            driver.find_element_by_xpath('//*[@id="main-content"]/div[2]/div[2]/nav/button[2]').click()
            elems_presence = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"desktop-product-list-item__Container")]'))
            )
            scrape(row) # recursively calls "scrape" function with "row" as an argument in order not to overwrite previous entries in excel file
    else:
        pass

# Creating a new excel workbook
wb = Workbook()
wb["Sheet"]["A1"] = product_final
wb["Sheet"]["G1"] = "Weight"
wb["Sheet"]["H1"] = "Price"
wb["Sheet"]["I1"] = "Discount"

# Scraping function call
scrape(3)

# Quitting the driver
driver.quit()