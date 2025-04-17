from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\SURYA B.S\AppData\Local\Google\Chrome\User Data")
options.add_argument(r"--profile-directory=Profile 19")  


driver = webdriver.Chrome(options=options)


driver.get("https://mail.google.com/mail/u/0/#inbox")

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@role='main']")))

try:
 
    checked_emails = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, "//tr[contains(@class, 'zA') and .//div[@role='checkbox' and @aria-checked='true']]"))
    )

    if checked_emails:
        print(f"Found {len(checked_emails)} checked emails.")

        
        delete_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[3]/div/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/div/div[2]/div[3]/div"))
        )

        
        if delete_button.is_displayed():
            print("Delete button is visible.")
        else:
            print("Delete button is not visible.")


        try:
            delete_button.click()
            print("Delete button clicked directly.")
        except Exception as click_error:
            print(f"Direct click failed: {click_error}")

        time.sleep(7)  


        try:
            undo_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Undo')]"))
            )
            print("Undo button appeared, clicking it.")
            undo_button.click()
            time.sleep(2) 
        except:
            print("No Undo button appeared.")

        try:
            WebDriverWait(driver, 15).until(
                EC.invisibility_of_element_located((By.XPATH, "//tr[contains(@class, 'zA') and .//div[@role='checkbox' and @aria-checked='true']]"))
            )
            print("Test Passed: Checked emails deleted successfully.")
        except:
            print("Test Failed: Checked emails still visible after deletion.")

    else:
        print("No checked emails found.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
