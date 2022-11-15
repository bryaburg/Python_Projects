from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
import datetime
import time
import calendar
import keyboard
import random

#Good Catch near miss options
Near_miss = [
(" Slipped on stairway.", "Could have fallen and broke ankle", "Continued to watch my steps and have 3 points of contact"), 
("Found some straps on the floor","Could have tripped over straps", "Picked up straps"),
("Cardboard fallen off decant line", "Could have tripped over fallen clutter", "Put box back on line"),
(" Pallet not in 5s area", "Could have tripped over pallet", "Got a associate to move it correctly")
]

#Pick from random list
random_near_miss = random.choice(Near_miss)

#start webdriver.
options = Options()
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(chrome_options = options, executable_path=r"C:\Users\bryaburg\Desktop\Python Projects\Python_Projects\Good Catch Near Miss\chromedriver.exe")

#Pull we address.
driver.get("https://app.smartsheet.com/b/form/f9293e40f29343108d1b37a5fb831bca")

#wait 3 secs 
time.sleep(5)

#Find Date Element and click.
current_day = datetime.date.today()
Todays_Date = datetime.date.strftime(current_day, "%m/%d/%Y")
Date_Form = driver.find_element(By.XPATH,'//*[@id="date_DATE"]').send_keys(Todays_Date)

#Check box Good Catch
Observation_Box = driver.find_element(By.XPATH,'//*[@id="983lwNM"]/div[2]/div/div[2]/span[1]').click()
keyboard.press_and_release("down")
keyboard.press_and_release("enter")

#Selecting Site
Site = driver.find_element(By.XPATH,'//*[@id="pJEjXL0"]/div[2]/div/div[1]').click()
keyboard.write("DSM5")
keyboard.press_and_release("enter")

#Find Submitter Name box and put first and last name.
Name = "Burgess, Bryan"
First_Last_Name = driver.find_element(By.XPATH,'//*[@id="text_box_SUBMITTER NAME (OPTIONAL)"]').send_keys(Name)

#DISCOVERY TYPE
DISCOVERY_TYPE = driver.find_element(By.XPATH,'//*[@id="JyNbA1q"]/div/div/div[1]').click()
keyboard.press_and_release("down")
keyboard.press_and_release("enter")

#UNSAFE ACT OR CONDITION*
UNSAFE_ACT_OR_CONDITION = driver.find_element(By.XPATH,'//*[@id="mJNyPvd"]/div[2]/div/div[1]').click()
keyboard.press_and_release("down")
keyboard.press_and_release("enter")

#DESCRIPTION OF HAZARDOUS SITUATION
DESCRIPTION_OF_HAZARDOUS_SITUATION = driver.find_element(By.XPATH,'//*[@id="textarea_DESCRIPTION OF HAZARDOUS SITUATION"]').click()
keyboard.write(random_near_miss[0])

#STATE OF MIND*
STATE_OF_MIND = driver.find_element(By.XPATH,'//*[@id="nJeQzLz"]/div[2]/div/div[1]').click()
keyboard.press_and_release("down")
keyboard.press_and_release("enter")

#CRITICAL ERROR*
CRITICAL_ERROR = driver.find_element(By.XPATH,'//*[@id="AMvqn9w"]/div[2]/div/div[1]').click()
keyboard.press_and_release("down")
keyboard.press_and_release("enter")

#CRITICAL ERROR REDUCTION
CRITICAL_ERROR_REDUCTION = driver.find_element(By.XPATH,'//*[@id="Pn23l0G"]/div[2]/div/div[1]').click()
keyboard.press_and_release("down")
keyboard.press_and_release("enter")

#HOW IT COULD BE WORSE
HOW_IT_COULD_BE_WORSE = driver.find_element(By.XPATH,'//*[@id="textarea_HOW IT COULD BE WORSE"]').click()
keyboard.write(random_near_miss[1])

#IMMEDIATE ACTION RESULT
IMMEDIATE_ACTION_RESULT = driver.find_element(By.XPATH,'//*[@id="WAJn6wQ"]/div[2]/div/div[1]').click()
keyboard.press_and_release("down")
keyboard.press_and_release("enter")

#IMMEDIATE ACTION
IMMEDIATE_ACTION = driver.find_element(By.XPATH,'//*[@id="textarea_IMMEDIATE ACTION"]').click()
keyboard.write(random_near_miss[2])

#Summit 
Summit = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/section[2]/div/div/form/div[27]/button/span').click()