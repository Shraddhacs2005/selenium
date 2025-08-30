from selenium import webdriver
from selenium.webdriver.chrome.service import Service
options=webdriver.ChromeOptions()
#options.add_argument('--headless')
ser=Service("C:\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser,options=options)
driver.get("https://w3schools.com")
driver.maximize_window()
driver.implicitly_wait(20)
#print(driver.page_source)
print(driver.title)
driver.quit()