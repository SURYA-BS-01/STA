from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/search?q=calculator")

# Wait for calculator to load
time.sleep(2)

# Click 7 + 5 = using button IDs (Google calculator buttons)
driver.find_element(By.XPATH, "//div[@aria-label='7']").click()
driver.find_element(By.XPATH, "//div[@aria-label='plus']").click()
driver.find_element(By.XPATH, "//div[@aria-label='5']").click()
driver.find_element(By.XPATH, "//div[@aria-label='equals']").click()

time.sleep(2)
print("Performed 7 + 5 successfully.")
driver.quit()
