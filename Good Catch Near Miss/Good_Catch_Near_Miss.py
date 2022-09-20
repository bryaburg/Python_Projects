from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import datetime
import time
import calendar
import keyboard

#start webdriver.
driver = webdriver.Chrome()

#Pull we address.
driver.get("https://app.smartsheet.com/b/form/f9293e40f29343108d1b37a5fb831bca")

#wait 3 secs 
time.sleep(3)

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
keyboard.write("I slipped on stairs walking down them")

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
keyboard.write("I could have broken my leg")

#IMMEDIATE ACTION RESULT
IMMEDIATE_ACTION_RESULT = driver.find_element(By.XPATH,'//*[@id="WAJn6wQ"]/div[2]/div/div[1]').click()
keyboard.press_and_release("down")
keyboard.press_and_release("enter")

#IMMEDIATE ACTION
IMMEDIATE_ACTION = driver.find_element(By.XPATH,'//*[@id="textarea_IMMEDIATE ACTION"]').click()
keyboard.write("Proceeded to watch my steps and be more slow")

#Summit 
Summit = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/section[2]/div/div/form/div[27]/button/span').click()
