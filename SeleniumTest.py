from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="E:\\CHEEKO BOYEE\\Programs\\2Python\\chromedriver.exe")

driver.get("https://www.google.com")


driver.implicitly_wait(0.5)

search_box = driver.find_element(By.NAME, "q")
search_button = driver.find_element(By.NAME, "btnK")

search_box.send_keys("Selenium")
search_button.click()



driver.find_element(By.NAME, "q").get_attribute("value")  # => "Selenium"

driver.quit()
