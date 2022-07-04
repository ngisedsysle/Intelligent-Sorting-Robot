from curses import window
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time 

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("window-size=1200x600")

s = Service(r'C:\Users\kouadio\Robox\Dataset\Code\chromedriver.exe')
driver= webdriver.Chrome(service=s, options=options)
driver.get('https://images.google.com/')

refuser_button=driver.find_element( By.ID,'W0wltc').click()


box = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
box.send_keys('black shielded power inductors')

serch_button = driver.find_element(By.XPATH,'//*[@id="sbtc"]/button').click()


#To scroll down the page

last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')

    try:
        driver.find_element(By.XPATH,'//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
        time.sleep(2)
    
    except:
        pass
    if new_height == last_height:
        break

    last_height = new_height

for i in range (1,500):
    try:
        driver.find_element(By.XPATH,'//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot(r'C:\Users\kouadio\Robox\Dataset\Kaggle_inductance\inductance('+str(i+405)+').png')
    
    except:
        pass