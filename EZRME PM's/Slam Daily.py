from selenium import webdriver
import chromedriver_autoinstaller
from selenium.common.exceptions import NoSuchElementException
import time
import keyboard

#Ask for ICW Number 
WO_Number= input("Enter WO Number")

#Closing Comments
Closing_Comments = ("I am very pleased to report that I have completed everything on my task list and found no issues. All systems are functioning as intended and there are no outstanding issues that need to be addressed. I will continue to monitor the systems closely and address any issues that may arise.")


# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

#Updates chromedriver as needed
chromedriver_autoinstaller.install()

#Is showing webdriver where chrome and chromedriver is located
options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_driver_binary = r"C:\Users\bryaburg\Desktop\Python_Projects\Python_Projects\EZRME PM's\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

#make Webpage 
details = (f"https://portal.ez.na.rme.logistics.a2z.com/work-orders/{WO_Number}/details")

#Get Webpage and launches it.
driver.get(details)
driver.maximize_window()

# Signing into EZRME 
while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        sign_in_as_amazon_employee = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-login-page").shadowRoot.querySelector("ez-login").shadowRoot.querySelector("mwc-button").shadowRoot.querySelector("button")')


        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1
sign_in_as_amazon_employee.click()

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        sso_login = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-login-page").shadowRoot.querySelector("ez-login").shadowRoot.querySelector("ez-credential-card").querySelector("mwc-button")')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1
sso_login.click()
'''
#Click PTP Button
ptp_button = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-menu").shadowRoot.querySelectorAll("ez-menu-item")[1]')
ptp_button.click()

time.sleep(3)


#Fill out PTP with no hazards
new_assessment = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("mwc-button")')
new_assessment.click()

time.sleep(3)

Take_2 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelector("ez-survey-options").shadowRoot.querySelectorAll("div")[3].querySelector("mwc-radio")')
Take_2.click()

time.sleep(3)

Next_0 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelectorAll("slot")[1].querySelectorAll("mwc-button")[2]')
Next_0.click()

time.sleep(3)

ACK_1 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelector("ez-survey-options").shadowRoot.querySelectorAll("div")[1].querySelector("mwc-checkbox")')
ACK_1.click()

ACK_2 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelector("ez-survey-options").shadowRoot.querySelectorAll("div")[2].querySelector("mwc-checkbox").shadowRoot.querySelector("div")')
ACK_2.click()

ACK_3 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelector("ez-survey-options").shadowRoot.querySelectorAll("div")[3].querySelector("mwc-checkbox")')
ACK_3.click()

ACK_4 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelector("ez-survey-options").shadowRoot.querySelectorAll("div")[4].querySelector("mwc-checkbox")')
ACK_4.click()

ACK_5 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelector("ez-survey-options").shadowRoot.querySelectorAll("div")[5].querySelector("mwc-checkbox")')
ACK_5.click()

ACK_6 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelector("ez-survey-options").shadowRoot.querySelectorAll("div")[6].querySelector("mwc-checkbox").shadowRoot.querySelector("div")')
ACK_6.click()

time.sleep(3)

Next_1 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelectorAll("slot")[1].querySelectorAll("mwc-button")[2]')
Next_1.click()

time.sleep(3)

Yes_1 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelector("ez-survey-options").shadowRoot.querySelectorAll("div")[0].querySelector("mwc-radio")')
Yes_1.click()

time.sleep(3)

Next_2 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelectorAll("slot")[1].querySelectorAll("mwc-button")[2]')
Next_2.click()

time.sleep(3)

Summit_0 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-card").querySelectorAll("div")[0].querySelectorAll("mwc-button")[1].shadowRoot.querySelectorAll("span")[2]')
driver.execute_script("arguments[0].click()", Summit_0)

time.sleep(5)


#Go to checklist and fill out

Checklist = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-menu").shadowRoot.querySelectorAll("ez-menu-item")[2]')
Checklist.click()

time.sleep(5)

Task_1 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-checklist").shadowRoot.querySelector("ez-work-order-eam-checklist-grid").shadowRoot.querySelector("ez-card").querySelector("vaadin-grid").querySelectorAll("vaadin-grid-cell-content")[31].querySelector("div").querySelectorAll("mwc-formfield")[0].querySelector("mwc-radio").shadowRoot.querySelector("div").querySelector("input")')
Task_1.click()

time.sleep(3)

Task_2 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-checklist").shadowRoot.querySelector("ez-work-order-eam-checklist-grid").shadowRoot.querySelector("ez-card").querySelector("vaadin-grid").querySelectorAll("vaadin-grid-cell-content")[40].querySelector("mwc-formfield").querySelector("mwc-checkbox").shadowRoot.querySelector("div").querySelector("input")')
Task_2.click()

time.sleep(5)

#Book Labor

Labor = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-menu").shadowRoot.querySelectorAll("ez-menu-item")[4]')
Labor.click()

time.sleep(5)

Plus_Mark = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelectorAll("div")[1].querySelector("ez-work-order-book-labor-page").shadowRoot.querySelector("ez-card").querySelector("ez-card-set").shadowRoot.querySelector("div").querySelectorAll("ez-labor-card")[4].shadowRoot.querySelectorAll("slot")[1].querySelector("div").querySelector("mwc-icon")')
Plus_Mark.click()

time.sleep(3)

Hours = driver.execute_script('return document.querySelector("vaadin-dialog-overlay").querySelector("main").querySelector("ez-book-labor-form").shadowRoot.querySelectorAll("div")[0].querySelector("ez-number-input").shadowRoot.querySelector("label").querySelector("input")')
Hours.click()
keyboard.press_and_release(".")
keyboard.press_and_release("5")

time.sleep(3)

Summit = driver.execute_script('return document.querySelector("vaadin-dialog-overlay").querySelector("main").querySelector("ez-book-labor-form").shadowRoot.querySelectorAll("div")[1].querySelectorAll("mwc-button")[1]')
Summit.click()

time.sleep(5)

#Details and complete WO

Details = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-menu").shadowRoot.querySelectorAll("ez-menu-item")[0]')
Details.click()

time.sleep(5)

Edit = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-details-page").shadowRoot.querySelector("ez-work-order-details").querySelectorAll("ez-details")[0].querySelector("h3").querySelectorAll("span")[1].querySelectorAll("mwc-button")[1]')
Edit.click()

time.sleep(5)

Closing = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-details-page").shadowRoot.querySelector("ez-work-order-details").querySelectorAll("ez-details")[4].querySelector("h3")')
Closing.click()

time.sleep(5)

Comment = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-details-page").shadowRoot.querySelector("ez-work-order-details").querySelectorAll("ez-details")[4].shadowRoot.querySelector("form").querySelector("ez-details-item").shadowRoot.querySelector("ez-details-comments").shadowRoot.querySelector("div").querySelector("mwc-textarea").shadowRoot.querySelector("label").querySelector("textarea")')
Comment.click()
Comment.send_keys(Closing_Comments)

time.sleep(3)

Submit = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-details-page").shadowRoot.querySelector("ez-work-order-details").querySelectorAll("ez-details")[4].shadowRoot.querySelector("form").querySelector("ez-details-item").shadowRoot.querySelector("ez-details-comments").shadowRoot.querySelector("div").querySelector("mwc-button")')
Submit.click()

time.sleep(3)

Save = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-details-page").shadowRoot.querySelector("ez-work-order-details").shadowRoot.querySelector("div").querySelectorAll("mwc-button")[1]')
Save.click

time.sleep(5)
'''