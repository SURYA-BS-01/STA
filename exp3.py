from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the Chrome driver with WebDriver Manager
service = Service(ChromeDriverManager().install())
chrome_driver_path = service.path

# Print the path
print(f"Chrome WebDriver path: {chrome_driver_path}")

# Optional: Create a driver instance and close it
driver = webdriver.Chrome(service=service)
driver.quit()