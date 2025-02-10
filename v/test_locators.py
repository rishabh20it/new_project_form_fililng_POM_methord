import time
import pandas as pd
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

# **Reading Data from CSV File**
file_path = "test_pom_data.csv"
df = pd.read_csv(file_path)

# **Check if Data is Loaded**
test_data = []
for row in df.itertuples(index=False, name=None):
    test_data.append(tuple(row))    #This does the same thing—iterating over
    # df.itertuples() and appending each row (converted to a tuple) to the test_data list.

print("Loaded Test Data:", test_data)  # Debugging Step

@pytest.fixture(scope="function")
def browser_setup():
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    time.sleep(2)  # Small delay
    yield driver
    driver.quit()  #  Close browser after test execution

# **Validation Functions**
def validate_name(name):
    assert name.replace(" ", "").isalpha(), f"Invalid name: {name}. It should only contain letters and spaces."

def validate_email(email):
    assert "@" in email and email.endswith(".com"), f"Invalid email: {email}. Email must contain '@' and end with '.com'."

def validate_password(password):
    special_characters = "!@#$%^&*()_+-=:;.,/?\\|"
    assert any(c.isupper() for c in password) and any(c in special_characters for c in password), \
        f"Invalid password: {password}. Password must contain at least one uppercase letter and one special character."

def validate_gender(gender):
    assert gender in ["Male", "Female"], f"Invalid gender: {gender}. Allowed values: ['Male', 'Female']"

def validate_employment_status(employment_status):
    assert employment_status in ["Student", "Employed"], f"Invalid employment status: {employment_status}. Allowed values: ['Student', 'Employed']"

# **Parameterized Test Case**
@pytest.mark.parametrize("name, email, password, gender, employment_status", test_data)  # ✅ Fixed parameter formatting
def test_details(browser_setup, name, email, password, gender, employment_status):
    """Fills the form using Selenium and performs assertions before inputting values."""
    driver = browser_setup  # ✅ Use the fixture driver
    wait = WebDriverWait(driver, 10)

    # **Validations before form submission**
    validate_name(name)
    validate_email(email)
    validate_password(password)
    validate_gender(gender)
    validate_employment_status(employment_status)

    # **Filling Form**
    name_input = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@name='name'])[1]")))
    name_input.clear()
    name_input.send_keys(name)

    email_input = driver.find_element(By.XPATH, "//input[@name='email']")
    email_input.clear()
    email_input.send_keys(email)

    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    password_input.clear()
    password_input.send_keys(password)

    gender_dropdown = driver.find_element(By.ID, "exampleFormControlSelect1")
    Select(gender_dropdown).select_by_visible_text(gender)

    if employment_status == "Employed":
        driver.find_element(By.XPATH, "//input[@value='option2']").click()
    elif employment_status == "Student":
        driver.find_element(By.XPATH, "//input[@value='option1']").click()

    # Submit Form
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()

    # ✅ Wait for Confirmation Message Instead of Sleep
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-success")))
