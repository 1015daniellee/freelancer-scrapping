from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from login import *

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open the freelancer.com website
driver.get("https://www.freelancer.com/")

# desplayLogin(driver)

# Hover find job using ActionChains
hoverable = driver.find_element(By.LINK_TEXT, " Find Jobs ")
ActionChains(driver).move_to_element(hoverable).perform()
time.sleep(3)

# Close the browser
driver.quit()
