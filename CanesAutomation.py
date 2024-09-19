from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import random
import string
import time


#Chrome Upload
driver = Driver(uc=True)
driver.get("https://raisingcanes.myguestaccount.com/en-us/guest/register")
#chrome.get("https://chatgpt.com/?oai-dm=1")
# driver.find_element(By.type, 'printedCard').send_keys("192819829182")


#Card Number/Code
val = input("What is the Card Number: ")
driver.type('#printedCard', val)
driver.click("button.registerCardnumberSubmitButton")
code = input("What is the code: ")
driver.type('#registrationCode', code)
driver.click("button.registerRegCodeSubmitButton")
dropdown = driver.find_element(By.ID, "salutation")
print(dropdown)


#First Dropdown
select_dropdown = Select(dropdown)
select_dropdown.select_by_visible_text("Mr.")


#First Name
length = 6
firstName = ''.join(random.choices(string.ascii_letters, k = length))
driver.type('#firstName', str(firstName))
lastName = ''.join(random.choices(string.ascii_letters, k = length))
driver.type('#lastName', str(lastName))


#Address
driver.type('#address1', '846 Surrey Ave.')
driver.type('#city', 'Dallas')


#Second Dropdown
x = driver.find_element(By.ID, 'stateProvince')
state = Select(x)
state.select_by_visible_text('Texas')


#Zip Code
driver.type('#postalCode', '75034')


#Phone Number
number_list = list()
for i in range(10):
    var = random.randint(0, 9)
    number_list.append(var)
strNumber = [str(i) for i in number_list]
phone_number = "".join(strNumber)
driver.type('#mobilePhone', phone_number)
print(phone_number)


#Birthmonth/birthdate
driver.type('#dateOfBirthMonth', '09')
driver.type('#dateOfBirthDay', '10')


#gmail
email = "xxxxx@gmail.com"
email_list = list(email)
random_period = random.randint(0, len(email)-1)
email_list.insert(random_period, ".")
joint_random = "".join(email_list)
driver.type('#email', joint_random)


#Third Dropdown
y = driver.find_element(By.ID, 'favoriteStoreState')
storeState = Select(y)
storeState.select_by_visible_text('TX')


#Delay
time.sleep(3)


#Fourth Dropdown
z = driver.find_element(By.ID, 'favoriteStore')
store = Select(z)
store.select_by_visible_text("Frisco - Preston Rd. (C81)")


#Username
user_name = ''.join(random.choices(string.ascii_letters, k = length))
driver.type('#username', str(user_name))


#Password
password = ''.join(random.choices(string.ascii_letters, k = length))
driver.type('#password', password)
driver.type('#confirmPassword', password)


driver.click("button.registerRegistrationFieldsSubmitButton")


time.sleep(1000)


