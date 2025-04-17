from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.google.com")
print("Page Title:", driver.title)
driver.quit()