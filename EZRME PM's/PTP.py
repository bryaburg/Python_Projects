from selenium import webdriver
import chromedriver_autoinstaller
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

time.sleep(3)

# Signing into EZRME 
sign_in_as_amazon_employee = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-login-page").shadowRoot.querySelector("ez-login").shadowRoot.querySelector("mwc-button").shadowRoot.querySelector("button")')
sign_in_as_amazon_employee.click()

sso_login = driver.execute_script('return document.querySelector("ez-rme-app").shadowRoot.querySelector("ez-login-page").shadowRoot.querySelector("ez-login").shadowRoot.querySelector("ez-credential-card").querySelector("mwc-button")')
sso_login.click()

time.sleep(5)

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