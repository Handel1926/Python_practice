from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
path = "C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(path)
sleep(1)
driver.get("https://www.amazon.com")

