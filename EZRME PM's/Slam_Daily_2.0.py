from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
import time

#Ask for ICW Number 
WO_Number= input("Enter WO Number")

#Closing Comments
Closing_Comments = ("I am very pleased to report that I have completed everything on my task list and found no issues. All systems are functioning as intended and there are no outstanding issues that need to be addressed. I will continue to monitor the systems closely and address any issues that may arise.")

#All buttons on WO
sign_in_as_amazon_employee = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-login-page").shadowRoot.querySelector("ez-login").shadowRoot.querySelector("mwc-button").shadowRoot.querySelector("button")'
sso_login = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-login-page").shadowRoot.querySelector("ez-login").shadowRoot.querySelector("ez-credential-card").querySelector("mwc-button")'
ptp_button = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-menu").shadowRoot.querySelectorAll("ez-menu-item")[1]'
new_assessment = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("mwc-button")'
Take_2 = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelector("ez-survey-options").shadowRoot.querySelectorAll("div")[3].querySelector("mwc-radio")'
Next_0 = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelectorAll("slot")[1].querySelectorAll("mwc-button")[2]'
ACK_1 = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelector("ez-survey-options").shadowRoot.querySelectorAll("div")[1].querySelector("mwc-checkbox").shadowRoot.querySelector("div").querySelector("input")'
ACK_2 = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelector("ez-survey-options").shadowRoot.querySelectorAll("div")[2].querySelector("mwc-checkbox").shadowRoot.querySelector("div").querySelector("input")'
ACK_3 = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelector("ez-survey-options").shadowRoot.querySelectorAll("div")[3].querySelector("mwc-checkbox").shadowRoot.querySelector("div").querySelector("input")'
ACK_4 = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelector("ez-survey-options").shadowRoot.querySelectorAll("div")[4].querySelector("mwc-checkbox").shadowRoot.querySelector("div").querySelector("input")'
ACK_5 = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelector("ez-survey-options").shadowRoot.querySelectorAll("div")[5].querySelector("mwc-checkbox").shadowRoot.querySelector("div").querySelector("input")'
ACK_6 = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelector("ez-survey-options").shadowRoot.querySelectorAll("div")[6].querySelector("mwc-checkbox").shadowRoot.querySelector("div").querySelector("input")'
Next_1 = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelectorAll("slot")[1].querySelectorAll("mwc-button")[2]'
Yes_1 = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelector("ez-survey-options").shadowRoot.querySelectorAll("div")[0].querySelector("mwc-radio")'
Next_2 = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-survey-builder").shadowRoot.querySelectorAll("slot")[1].querySelectorAll("mwc-button")[2]'
Summit_0 = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-card").querySelector("div").querySelectorAll("mwc-button")[1]'
Checklist = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-menu").shadowRoot.querySelectorAll("ez-menu-item")[2]'
Task_1 = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-checklist").shadowRoot.querySelector("ez-work-order-eam-checklist-grid").shadowRoot.querySelector("ez-card").querySelector("vaadin-grid").querySelectorAll("vaadin-grid-cell-content")[31].querySelector("div").querySelectorAll("mwc-formfield")[0].querySelector("mwc-radio").shadowRoot.querySelector("div").querySelector("input")'
Task_2 = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-checklist").shadowRoot.querySelector("ez-work-order-eam-checklist-grid").shadowRoot.querySelector("ez-card").querySelector("vaadin-grid").querySelectorAll("vaadin-grid-cell-content")[40].querySelector("mwc-formfield").querySelector("mwc-checkbox").shadowRoot.querySelector("div").querySelector("input")'
Labor = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-menu").shadowRoot.querySelectorAll("ez-menu-item")[4]'
Plus_Mark = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelectorAll("div")[1].querySelector("ez-work-order-book-labor-page").shadowRoot.querySelector("ez-card").querySelector("ez-card-set").shadowRoot.querySelector("div").querySelectorAll("ez-labor-card")[4].shadowRoot.querySelectorAll("slot")[1].querySelector("div").querySelector("mwc-icon")'
Hours = 'return document.querySelector("vaadin-dialog-overlay").querySelector("main").querySelector("ez-book-labor-form").shadowRoot.querySelectorAll("div")[0].querySelector("ez-number-input").shadowRoot.querySelector("label").querySelector("input")'
Summit_1 = 'return document.querySelector("vaadin-dialog-overlay").querySelector("main").querySelector("ez-book-labor-form").shadowRoot.querySelectorAll("div")[1].querySelectorAll("mwc-button")[1]'
Details = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-menu").shadowRoot.querySelectorAll("ez-menu-item")[0]'
Edit = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-details-page").shadowRoot.querySelector("ez-work-order-details").querySelectorAll("ez-details")[0].querySelector("h3").querySelectorAll("span")[1].querySelectorAll("mwc-button")[1]'
Closing = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-details-page").shadowRoot.querySelector("ez-work-order-details").querySelectorAll("ez-details")[4].querySelector("h3")'
Comment = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-details-page").shadowRoot.querySelector("ez-work-order-details").querySelectorAll("ez-details")[4].shadowRoot.querySelector("form").querySelector("ez-details-item").shadowRoot.querySelector("ez-details-comments").shadowRoot.querySelector("div").querySelector("mwc-textarea").shadowRoot.querySelector("label").querySelector("textarea")'
Submit_2 = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-details-page").shadowRoot.querySelector("ez-work-order-details").querySelectorAll("ez-details")[4].shadowRoot.querySelector("form").querySelector("ez-details-item").shadowRoot.querySelector("ez-details-comments").shadowRoot.querySelector("div").querySelector("mwc-button")'
Save = 'return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-details-page").shadowRoot.querySelector("ez-work-order-details").shadowRoot.querySelector("div").querySelectorAll("mwc-button")[1]'

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
  
def click_buttons(buttons):
    timeout = 10  # timeout in seconds

    attempts = 0
    while True:
        try:
            element = driver.execute_script(buttons)
            if element is not None:
                break
        except:
            attempts += 1
            if attempts >= 10:
                print("Timed out waiting for element to be located.")
                break
            time.sleep(0.5)

    # Click the element (if it was found)
    if element is not None:
        element.click()

click_buttons(sign_in_as_amazon_employee)

click_buttons(sso_login)

click_buttons(ptp_button)

click_buttons(new_assessment)

click_buttons(Take_2)

click_buttons(Next_0)

click_buttons(ACK_1)

click_buttons(ACK_2)

click_buttons(ACK_3)

click_buttons(ACK_4)

click_buttons(ACK_5)

click_buttons(ACK_6)

click_buttons(Next_1)

click_buttons(Yes_1)

click_buttons(Next_2)

time.sleep(1)

Summit_0 = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-work-order-page").shadowRoot.querySelector("ez-work-order-ptw-pilot").shadowRoot.querySelector("ez-work-order-ptp-page").shadowRoot.querySelector("ez-card").querySelectorAll("div")[0].querySelectorAll("mwc-button")[1].shadowRoot.querySelectorAll("span")[2]')
driver.execute_script("arguments[0].click()", Summit_0)

click_buttons(Checklist)

click_buttons(Task_1)

click_buttons(Task_2)

click_buttons(Labor)

click_buttons(Plus_Mark)

click_buttons(Hours)
Hours.send_keys(".5")

click_buttons(Summit_1)

click_buttons(details)

click_buttons(Edit)

click_buttons(Closing)

click_buttons(Comment)
Comment.send_keys(Closing_Comments)

click_buttons(Submit_2)

click_buttons(Save)

time.sleep(5)