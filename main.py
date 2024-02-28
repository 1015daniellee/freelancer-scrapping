from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Create a new instance of the Chrome driver
driver = webdriver.Chrome()
# Open the freelancer.com website
driver.get("https://www.freelancer.com/")
# Find the Log In button using the link text
log_in_button = driver.find_element(By.LINK_TEXT, "Log In")
# Click the Log In button
log_in_button.click()
time.sleep(2)
input_email_element = driver.find_element(By.ID, 'emailOrUsernameInput')
input_email_element.send_keys('oskardev0112@gmail.com')
time.sleep(2)
input_email_element.send_keys(Keys.ENTER)
time.sleep(2)
input_pass_element = driver.find_element(By.ID, 'passwordInput')
input_pass_element.send_keys('12345678')
# time.sleep(2)
# eye_element = driver.find_element(By.XPATH, '//fl-icon[@class="ng-star-inserted"]')
# eye_element.click()
time.sleep(2)
input_pass_element.send_keys(Keys.ENTER)
time.sleep(2)
checkbox_element = driver.find_element(By.XPATH, '//label[@class="CheckboxLabel"]')
checkbox_element.click()
time.sleep(2)
# Close the browser
driver.quit()
