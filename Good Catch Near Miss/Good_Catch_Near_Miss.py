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



#Good Catch near miss options
Near_miss = [
(" Slipped on stairway.", "Could have fallen and broke ankle", "Continued to watch my steps and have 3 points of contact"), 
("Found some straps on the floor","Could have tripped over straps", "Picked up straps"),
("Cardboard fallen off decant line", "Could have tripped over fallen clutter", "Put box back on line"),
(" Pallet not in 5s area", "Could have tripped over pallet", "Got a associate to move it correctly"),
("Water was dripping from the ceiling, creating a slip hazard." , "Someone could have walked through it without noticing and slipped." , "Put a bucket in place to catch the water and notified Safety Dept."),
("Associate was walking very fast with untied shoes, creating a trip hazard." , "The associate could've tripped and been injured." , "Stopped the associate with a stern voice and alerted them of their untied shoe."), 
("Tripping hazard: electrical cord was strewn across walkway." , "Someone could've tripped over it and been injured." , "I saw the temporary appliance that the cord was going to, unplugged the cord, and routed it in such a way so as to power it while keeping the cord off of the main path."),
("Label tape laying on the stairs to the SLAM lines posed a slipping hazard." , "If an associate had stepped on this unknowingly, they could've slipped on the stairs and been seriously injured." , "I picked up the label tape and observed the area for any other debris."),
("Tech only partially taped off area around control panel before working on it." , "Another associate could've unknowingly gotten past the red tape and been in the restricted area, putting themselves at risk for the hazards therein." , "I alerted the tech to the situation and proceeded to tape the remaining gap in the perimeter, securing off the area."),
("Tech was not wearing safety gloves while using a Wave lift." , "They could've grazed their hand during the course of their work." , "I alerted the tech of the problem and they remediated the situation by taking their gloves out of their pocket and putting them on."),
("Tech was walking off of the green mile without their glasses." , "They had put themselves at risk of flying debris from the overhead conveyor belts." , "Told the tech to put their glasses on and they did."),
("Associate was applying anti-adhesive to the SLAM line rollers without wearing latex gloves. , If their hands had open wounds, the chemicals in the wipes would've burned their hands." , "I showed the associate where the latex gloves were and had them wash hands and put the gloves on before returning to work."), 
("Associate was staging wood pallets without wearing gloves." , "They could've got splinters in their hands." , "I warned the associate and they put on their gloves."),
("Car in the parking lot almost backed into a person walking who was looking at their phone." , "They could've been seriously injured if the driver was going faster and paying less attention." , "I stopped both groups and had a talk with them about parking lot safety."),
("Slipped on a piece of wood from a pallet."), ("Myself or someone else could have fallen and been seriously injured."), ("I picked up the piece of wood and properly disposed of it."),
("Tripped going up the stairs to mezzanine because I was distracted."), ("I could have fallen down the stairs and seriously injured myself."), ("I focused on where I was going to avoid tripping again."),
("I found a roller on an elevated conveyor that was at risk of falling."), ("It could have fallen on someone, causing serious injury."), ("I immediately put up danger tape around the affected area and replaced the roller as soon as I was able to."),
("Found a stack of folded boxes that had fallen across the green mile."), ("Someone could have tripped and gotten hurt."), ("I picked up the boxes and stacked them out of the way."),
("Stopped an unauthorized associate who was about to reach onto the AR floor to pick up some amnesty."), ("They could have been terminated for breaking amazon's safety rules, or worse, they could have been injured."), ("Spoke to the associate about why they shouldn't reach onto the AR floor, and I also brought the issue to the associate's manager."),
("Found an unburied pallet jack unattended on the green mile."), ("Someone could have tripped on it and been injured."), ("I took the pallet jack and properly buried it in a pallet"),
("Found a bag of popcorn kernels that had broken open on a walkway."), ("Someone could have slipped and fallen."), ("Used a broom and dustpan to sweep up the kernels."),
("There was an empty cardboard roll laying on the floor."), ("Somebody could have stepped on it and fallen."), ("Picked it up off of the floor and threw it away."),
("Found a pod on the AR floor that was missing hardware causing it to tip dangerously."), ("It could have tipped over onto someone."), ("Removed the items from the pod and carefully removed it from the floor."),
("Found a section of netting on an elevated conveyor that was badly torn."), ("An item could have fallen through the torn section and hit someone."), ("I used zip ties to repair the damaged section."),]

#Pick from random list
random_near_miss = random.choice(Near_miss)

#Updates chromedriver as needed
chromedriver_autoinstaller.install()

#Is showing webdriver where chrome and chromedriver is located
options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_driver_binary = r"C:\Users\bryaburg\Desktop\Python_Projects\Python_Projects\Good Catch Near Miss\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

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