from selenium import webdriver
import chromedriver_autoinstaller
from selenium.common.exceptions import NoSuchElementException
import time
import keyboard

#Ask for ICW Number 
WO_Number= input("Enter WO Number")

#Closing Comments
Closing_Comments = ("I am very pleased to report that I have completed everything on my task list and found no issues. All systems are functioning as intended and there are no outstanding issues that need to be addressed. I will continue to monitor the systems closely and address any issues that may arise.")

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
# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0
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

# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

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

#Click PTP Button
# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        ptp_button = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelectorAll("div")[1].querySelector("main").querySelector("ez-work-order-page").shadowRoot.querySelectorAll("div")[0].querySelector("ez-menu").shadowRoot.querySelectorAll("ez-menu-item")[1].shadowRoot.querySelectorAll("div")[0].querySelector("span")')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1
ptp_button.click()

#Fill out PTP with no hazards
# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        new_assessment = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("mwc-button")')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1
new_assessment.click()

# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        Take_2 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelector("ez-survey-options").shadowRoot.querySelectorAll("div")[3].querySelector("mwc-radio")')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1
Take_2.click()

# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        Next_0 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelectorAll("slot")[1].querySelectorAll("mwc-button")[2]')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1
Next_0.click()

# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        ACK_1 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelector("ez-survey-options").shadowRoot.querySelectorAll("div")[1].querySelector("mwc-checkbox")')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1
ACK_1.click()

# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        ACK_2 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelector("ez-survey-options").shadowRoot.querySelectorAll("div")[2].querySelector("mwc-checkbox").shadowRoot.querySelector("div")')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1
ACK_2.click()

# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        ACK_3 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelector("ez-survey-options").shadowRoot.querySelectorAll("div")[3].querySelector("mwc-checkbox")')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1
ACK_3.click()

# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        ACK_4 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelector("ez-survey-options").shadowRoot.querySelectorAll("div")[4].querySelector("mwc-checkbox")')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1
ACK_4.click()

# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        ACK_5 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelector("ez-survey-options").shadowRoot.querySelectorAll("div")[5].querySelector("mwc-checkbox")')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1
ACK_5.click()

# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        ACK_6 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelector("ez-survey-options").shadowRoot.querySelectorAll("div")[6].querySelector("mwc-checkbox").shadowRoot.querySelector("div")')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1
ACK_6.click()

# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        Next_1 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelectorAll("slot")[1].querySelectorAll("mwc-button")[2]')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1
Next_1.click()

time.sleep(3)

# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        Yes_1 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelector("ez-survey-options").shadowRoot.querySelectorAll("div")[0].querySelector("mwc-radio")')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1
Yes_1.click()

# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        Next_2 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelectorAll("slot")[1].querySelectorAll("mwc-button")[2]')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1
Next_2.click()

# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        Summit_0 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-card").querySelectorAll("div")[0].querySelectorAll("mwc-button")[1].shadowRoot.querySelectorAll("span")[2]')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1
driver.execute_script("arguments[0].click()", Summit_0)

#Go to checklist and fill out
# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        Checklist = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-menu").shadowRoot.querySelectorAll("ez-menu-item")[2]')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1
Checklist.click()

# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        Task_1 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-checklist").shadowRoot.querySelector("ez-work-order-eam-checklist-grid").shadowRoot.querySelector("ez-card").querySelector("vaadin-grid").querySelectorAll("vaadin-grid-cell-content")[31].querySelector("div").querySelectorAll("mwc-formfield")[0].querySelector("mwc-radio").shadowRoot.querySelector("div").querySelector("input")')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1

Task_1.click()

# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        Task_2 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-checklist").shadowRoot.querySelector("ez-work-order-eam-checklist-grid").shadowRoot.querySelector("ez-card").querySelector("vaadin-grid").querySelectorAll("vaadin-grid-cell-content")[40].querySelector("mwc-formfield").querySelector("mwc-checkbox").shadowRoot.querySelector("div").querySelector("input")')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1

Task_2.click()

#Book Labor
# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        Labor = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-menu").shadowRoot.querySelectorAll("ez-menu-item")[4]')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1
Labor.click()

# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        Plus_Mark = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelectorAll("div")[1].querySelector("ez-work-order-book-labor-page").shadowRoot.querySelector("ez-card").querySelector("ez-card-set").shadowRoot.querySelector("div").querySelectorAll("ez-labor-card")[4].shadowRoot.querySelectorAll("slot")[1].querySelector("div").querySelector("mwc-icon")')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1

Plus_Mark.click()

# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        Hours = driver.execute_script('return document.querySelector("vaadin-dialog-overlay").querySelector("main").querySelector("ez-book-labor-form").shadowRoot.querySelectorAll("div")[0].querySelector("ez-number-input").shadowRoot.querySelector("label").querySelector("input")')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1
Hours.click()
keyboard.press_and_release(".")
keyboard.press_and_release("5")

# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        Summit = driver.execute_script('return document.querySelector("vaadin-dialog-overlay").querySelector("main").querySelector("ez-book-labor-form").shadowRoot.querySelectorAll("div")[1].querySelectorAll("mwc-button")[1]')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1

Summit.click()

#Details and complete WO
# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        Details = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-menu").shadowRoot.querySelectorAll("ez-menu-item")[0]')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1
Details.click()

# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        Edit = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-details-page").shadowRoot.querySelector("ez-work-order-details").querySelectorAll("ez-details")[0].querySelector("h3").querySelectorAll("span")[1].querySelectorAll("mwc-button")[1]')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1

Edit.click()

# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        Closing = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-details-page").shadowRoot.querySelector("ez-work-order-details").querySelectorAll("ez-details")[4].querySelector("h3")')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1

Closing.click()

# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        Comment = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-details-page").shadowRoot.querySelector("ez-work-order-details").querySelectorAll("ez-details")[4].shadowRoot.querySelector("form").querySelector("ez-details-item").shadowRoot.querySelector("ez-details-comments").shadowRoot.querySelector("div").querySelector("mwc-textarea").shadowRoot.querySelector("label").querySelector("textarea")')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1

Comment.click()
Comment.send_keys(Closing_Comments)

# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        Submit = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-details-page").shadowRoot.querySelector("ez-work-order-details").querySelectorAll("ez-details")[4].shadowRoot.querySelector("form").querySelector("ez-details-item").shadowRoot.querySelector("ez-details-comments").shadowRoot.querySelector("div").querySelector("mwc-button")')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1

Submit.click()

# Set a flag to indicate whether the element has been found
element_found = False

# Set a counter to keep track of the number of attempts
attempts = 0

while not element_found and attempts < 10:
    try:
        # Look for the element on the page
        Save = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-details-page").shadowRoot.querySelector("ez-work-order-details").shadowRoot.querySelector("div").querySelectorAll("mwc-button")[1]')

        # If the element is found, set the flag to True to exit the loop
        element_found = True
    except NoSuchElementException:
        # If the element is not found, wait for a second and try again
        time.sleep(1)
        attempts += 1

Save.click

time.sleep(5)
