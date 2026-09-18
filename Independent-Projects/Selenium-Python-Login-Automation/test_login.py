from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/login"
USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"

def test_valid_login():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    try:
        driver.get(URL)
        wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(USERNAME)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        flash = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
        assert "You logged into a secure area!" in flash.text
    finally:
        driver.quit()

if __name__ == "__main__":
    test_valid_login()
    print("Login automation test completed successfully.")
