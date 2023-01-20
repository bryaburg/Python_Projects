from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import datetime
import time
import calendar
import keyboard
import random
import chromedriver_binary



#Good Catch near miss options
Near_miss = [
{"DESCRIPTION_OF_HAZARDOUS_SITUATION" : "Found some straps on the floor", "HOW_IT_COULD_BE_WORSE" : "Could have tripped over straps", "IMMEDIATE_ACTION" : "Picked up straps"},
{"DESCRIPTION_OF_HAZARDOUS_SITUATION" : "Cardboard fallen off decant line", "HOW_IT_COULD_BE_WORSE" : "Could have tripped over fallen clutter", "IMMEDIATE_ACTION" : "Put box back on line"},
{"DESCRIPTION_OF_HAZARDOUS_SITUATION" : "Pallet not in 5s area", "HOW_IT_COULD_BE_WORSE" : "Could have tripped over pallet", "IMMEDIATE_ACTION" : "Got a associate to move it correctly"},
{"DESCRIPTION_OF_HAZARDOUS_SITUATION" : "Water was dripping from the ceiling, creating a slip hazard.", "HOW_IT_COULD_BE_WORSE" : "Someone could have walked through it without noticing and slipped.", "IMMEDIATE_ACTION" : "Put a bucket in place to catch the water and notified Safety Dept."},
{"DESCRIPTION_OF_HAZARDOUS_SITUATION" : "Associate was walking very fast with untied shoes, creating a trip hazard.", "HOW_IT_COULD_BE_WORSE" : "The associate could've tripped and been injured.", "IMMEDIATE_ACTION" : "Stopped the associate with a stern voice and alerted them of their untied shoe."},
{"DESCRIPTION_OF_HAZARDOUS_SITUATION" : "Tripping hazard: electrical cord was strewn across walkway.", "HOW_IT_COULD_BE_WORSE" : "Someone could've tripped over it and been injured.", "IMMEDIATE_ACTION" : "I saw the temporary appliance that the cord was going to, unplugged the cord, and routed it in such a way so as to power it while keeping the cord off of the main path."},
{"DESCRIPTION_OF_HAZARDOUS_SITUATION" : "Label tape laying on the stairs to the SLAM lines posed a slipping hazard.", "HOW_IT_COULD_BE_WORSE" : "If an associate had stepped on this unknowingly, they could've slipped on the stairs and been seriously injured.", "IMMEDIATE_ACTION" : "I picked up the label tape and observed the area for any other debris."},
{"DESCRIPTION_OF_HAZARDOUS_SITUATION" : "Tech only partially taped off area around control panel before working on it.", "HOW_IT_COULD_BE_WORSE" : "Another associate could've unknowingly gotten past the red tape and been in the restricted area, putting themselves at risk for the hazards therein.", "IMMEDIATE_ACTION" : "I alerted the tech to the situation and proceeded to tape the remaining gap in the perimeter, securing off the area."},
{"DESCRIPTION_OF_HAZARDOUS_SITUATION" : "Tech was not wearing safety gloves while using a Wave lift.", "HOW_IT_COULD_BE_WORSE" : "They could've grazed their hand during the course of their work.", "IMMEDIATE_ACTION" : "I alerted the tech of the problem and they remediated the situation by taking their gloves out of their pocket and putting them on."},
{"DESCRIPTION_OF_HAZARDOUS_SITUATION" : "Tech was walking off of the green mile without their glasses.", "HOW_IT_COULD_BE_WORSE" : "They had put themselves at risk of flying debris from the overhead conveyor belts.", "IMMEDIATE_ACTION" : "Told the tech to put their glasses on and they did."},
{"DESCRIPTION_OF_HAZARDOUS_SITUATION" : "Associate was applying anti-adhesive to the SLAM line rollers without wearing latex gloves.", "HOW_IT_COULD_BE_WORSE" : "If their hands had open wounds, the chemicals in the wipes would've burned their hands.", "IMMEDIATE_ACTION" : "I showed the associate where the latex gloves were and had them wash hands and put the gloves on before returning to work."},
{"DESCRIPTION_OF_HAZARDOUS_SITUATION" : "Associate was staging wood pallets without wearing gloves.", "HOW_IT_COULD_BE_WORSE" : "They could've got splinters in their hands.", "IMMEDIATE_ACTION" : "I warned the associate and they put on their gloves."},
{"DESCRIPTION_OF_HAZARDOUS_SITUATION" : "Car in the parking lot almost backed into a person walking who was looking at their phone.", "HOW_IT_COULD_BE_WORSE" : "They could've been seriously injured if the driver was going faster and paying less attention.", "IMMEDIATE_ACTION" : "I stopped both groups and had a talk with them about parking lot safety."},
{"DESCRIPTION_OF_HAZARDOUS_SITUATION" : "Slipped on a piece of wood from a pallet.", "HOW_IT_COULD_BE_WORSE" : "Myself or someone else could have fallen and been seriously injured.", "IMMEDIATE_ACTION" : "I picked up the piece of wood and properly disposed of it."},
{"DESCRIPTION_OF_HAZARDOUS_SITUATION" : "Tripped going up the stairs to mezzanine because I was distracted.", "HOW_IT_COULD_BE_WORSE" : "I could have fallen down the stairs and seriously injured myself.", "IMMEDIATE_ACTION" : "I focused on where I was going to avoid tripping again."},
{"DESCRIPTION_OF_HAZARDOUS_SITUATION" : "I found a roller on an elevated conveyor that was at risk of falling.", "HOW_IT_COULD_BE_WORSE" : "It could have fallen on someone, causing serious injury.", "IMMEDIATE_ACTION" : "I immediately put up danger tape around the affected area and replaced the roller as soon as I was able to."},
{"DESCRIPTION_OF_HAZARDOUS_SITUATION" : "Found a stack of folded boxes that had fallen across the green mile.", "HOW_IT_COULD_BE_WORSE" : "Someone could have tripped and gotten hurt.", "IMMEDIATE_ACTION" : "I picked up the boxes and stacked them out of the way."},
{"DESCRIPTION_OF_HAZARDOUS_SITUATION" : "Stopped an unauthorized associate who was about to reach onto the AR floor to pick up some amnesty.", "HOW_IT_COULD_BE_WORSE" : "They could have been terminated for breaking amazon's safety rules, or worse, they could have been injured.", "IMMEDIATE_ACTION" : "Spoke to the associate about why they shouldn't reach onto the AR floor, and I also brought the issue to the associate's manager."},
{"DESCRIPTION_OF_HAZARDOUS_SITUATION" : "Found an unburied pallet jack unattended on the green mile.", "HOW_IT_COULD_BE_WORSE" : "Someone could have tripped on it and been injured.", "IMMEDIATE_ACTION" : "I took the pallet jack and properly buried it in a pallet"},
{"DESCRIPTION_OF_HAZARDOUS_SITUATION" : "Found a bag of popcorn kernels that had broken open on a walkway.", "HOW_IT_COULD_BE_WORSE" : "Someone could have slipped and fallen.", "IMMEDIATE_ACTION" : "Used a broom and dustpan to sweep up the kernels."},
{"DESCRIPTION_OF_HAZARDOUS_SITUATION" : "There was an empty cardboard roll laying on the floor.", "HOW_IT_COULD_BE_WORSE" : "Somebody could have stepped on it and fallen.", "IMMEDIATE_ACTION" : "Picked it up off of the floor and threw it away."},
{"DESCRIPTION_OF_HAZARDOUS_SITUATION" : "Found a pod on the AR floor that was missing hardware causing it to tip dangerously.", "HOW_IT_COULD_BE_WORSE" : "It could have tipped over onto someone.", "IMMEDIATE_ACTION" : "Removed the items from the pod and carefully removed it from the floor."},
{"DESCRIPTION_OF_HAZARDOUS_SITUATION" : "Found a section of netting on an elevated conveyor that was badly torn.", "HOW_IT_COULD_BE_WORSE" : "An item could have fallen through the torn section and hit someone.", "IMMEDIATE_ACTION" : "I used zip ties to repair the damaged section."}]


#Pick from random list
random_near_miss = random.choice(Near_miss)

#Updates chromedriver as needed
chromedriver_autoinstaller.install()

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
DESCRIPTION_OF_HAZARDOUS_SITUATION = driver.find_element(By.XPATH,'//*[@id="textarea_DESCRIPTION OF HAZARDOUS SITUATION"]').send_keys(random_near_miss["DESCRIPTION_OF_HAZARDOUS_SITUATION"])


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
HOW_IT_COULD_BE_WORSE = driver.find_element(By.XPATH,'//*[@id="textarea_HOW IT COULD BE WORSE"]').send_keys(random_near_miss["HOW_IT_COULD_BE_WORSE"])


#IMMEDIATE ACTION RESULT
IMMEDIATE_ACTION_RESULT = driver.find_element(By.XPATH,'//*[@id="WAJn6wQ"]/div[2]/div/div[1]').click()
keyboard.press_and_release("down")
keyboard.press_and_release("enter")


#IMMEDIATE ACTION
IMMEDIATE_ACTION = driver.find_element(By.XPATH,'//*[@id="textarea_IMMEDIATE ACTION"]').send_keys(random_near_miss["IMMEDIATE_ACTION"])


#Summit 
Summit = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/section[2]/div/div/form/div[27]/button/span').click()