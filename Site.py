from msilib.schema import Class
from typing import KeysView
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome('C:\Aplic\chromedriver.exe')
driver.maximize_window()

#ABRINDO LINKELN
urlLkdn = driver.get("https://www.linkedin.com/")
sleep(1)


