from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\SURYA B.S\AppData\Local\Google\Chrome\User Data")
options.add_argument(r"--profile-directory=Profile 19")  


driver = webdriver.Chrome(options=options)


driver.get("https://mail.google.com/mail/u/0/#inbox")

# Try to click Compose button (may change based on Gmail updates)
try:
    compose_btn = driver.find_element(By.XPATH, "//div[text()='Compose']")
    compose_btn.click()
    print("Compose button clicked successfully.")
except Exception as e:
    print("Failed to click compose:", e)

driver.quit()
