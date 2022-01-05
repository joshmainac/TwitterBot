from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

PATH="D:\Github\Twitter-bot\chromedriver.exe"
driver = webdriver.Chrome(PATH)
sleep(5)
driver.get("https://twitter.com//login")

sleep(5)

#Enter Your username
Myusername="XXX"
#Enter Your password
Mypassword="XXX"
#Enter your tweet
Mytweet = "XXX"
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input'))).send_keys(Myusername)
sleep(3)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input'))).send_keys(Keys.RETURN)
sleep(3)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input'))).send_keys(Mypassword)
sleep(3)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input'))).send_keys(Keys.RETURN)

driver.find_element_by_xpath("//a[@data-testid='SideNav_NewTweet_Button']").click()
sleep(1)
driver.find_element_by_class_name("notranslate").click()
sleep(2)
driver.find_element_by_class_name("notranslate").send_keys(Mytweet)
sleep(2)
driver.find_element_by_xpath("//div[@data-testid='tweetButton']").click()



