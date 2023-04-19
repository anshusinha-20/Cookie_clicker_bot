# ---------------- MODULES ---------------- #
# imported webdriver class from selenium module
from selenium import webdriver

# import service class from selenium module
from selenium.webdriver.chrome.service import Service

# import By class from selenium module
from selenium.webdriver.common.by import By

# import time module
import time


# ---------------- WORKING WITH SELENIUM DRIVER ---------------- #
# variable to store chrome diver path
chromeDriverPath = "/Users/anshusinha/Documents/Python/Angela Yu/chromedriver_mac64/chromedriver"

# created a driver object
driver = webdriver.Chrome(service=Service(chromeDriverPath))


# ---------------- SCRAPPING DATA FROM AMAZON ---------------- #
# # get method to launch the URL
# driver.get("https://www.amazon.in/Logitech-Master-Advanced-Wireless-Mouse/dp/B084TFH4BN/?_encoding=UTF8&pd_rd_w=denFQ&content-id=amzn1.sym.b5b6da36-128a-4deb-abfd-563ae12c2d96&pf_rd_p=b5b6da36-128a-4deb-abfd-563ae12c2d96&pf_rd_r=A0H30T6P9D47K9AKFJ5Z&pd_rd_wg=7RE1e&pd_rd_r=3ba085bc-a147-47d9-b384-ab88776e0db2&ref_=pd_gw_ci_mcx_mr_hp_atf_m")

# # find the element by class name
# price = driver.find_element(By.CLASS_NAME, "a-price-whole").text

# # print the price
# print(price)

# # find the element by xpath  
# helpLink = driver.find_element(By.XPATH, "//*[@id='navFooter']/div[1]/div/div[7]/ul/li[6]/a").get_attribute("href")

# # print the help link
# print(helpLink)


# ---------------- SCRAPPING DATA FROM PYTHON.ORG ---------------- #
# get method to launch the URL
driver.get("https://www.python.org")

eventDict = {}

for i in range(1, 6):
    # find the element by xpath
    eventDate = driver.find_element(By.XPATH, f"//*[@id='content']/div/section/div[2]/div[2]/div/ul/li[{i}]/time").text

    # find the element by xpath
    eventName = driver.find_element(By.XPATH, f"//*[@id='content']/div/section/div[2]/div[2]/div/ul/li[{i}]/a").text

    # add the event date and event name to the dictionary
    eventDict[i] = {"time": eventDate, "name": eventName}

# print the event dictionary
print(eventDict)

# quit the browser
driver.quit()