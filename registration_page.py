from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

# THIS FILE IS BASICALLY USED FOR LOCATORS AND THEIR ACTIONS


'''*locators
enter_name = //input[@name='name'])[1]
enter_emai = //input[@name='email']
enter_password = //input[@type='password']
select_gender =  exampleFormControlSelect1
employment_status = //input[@value='option2'] 
//input[@value='option1']
submit_form = //input[@type='submit']
get_success_message =  //div[@class='alert alert-success alert-dismissible']
'''


class RegistrationPage:
    def __init__(self, driver):  #  Fixed constructor
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_name(self, name):
        name_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@name='name'])[1]")))
        name_input.clear()
        name_input.send_keys(name)

    def enter_email(self, email):
        email_input = self.driver.find_element(By.XPATH, "//input[@name='email']")
        email_input.clear()
        email_input.send_keys(email)

    def enter_password(self, password):
        password_input = self.driver.find_element(By.XPATH, "//input[@type='password']")
        password_input.clear()
        password_input.send_keys(password)

    def select_gender(self, gender):
        gender_dropdown = self.driver.find_element(By.ID, "exampleFormControlSelect1")
        Select(gender_dropdown).select_by_visible_text(gender)

    def select_employment_status(self, employment_status):
        if employment_status == "Employed":
            self.driver.find_element(By.XPATH, "//input[@value='option2']").click()
        elif employment_status == "Student":
            self.driver.find_element(By.XPATH, "//input[@value='option1']").click()

    def submit_form(self):
        submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
        submit_button.click()

    def get_success_message(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-success alert-dismissible']"))).text
