from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

# Test data
URL = "https://qprime-qa.myqone.com/"

# Locators
User_Name_Field = "//input[@name='username']"
Password_Field = "//input[@name='password']"
Login_Button = "//ion-button[contains(.,'Login')]"
Dashboard_Tab = "//ion-label[contains(.,'Home')]"

# List of test credentials
test_credentials = [
    ("john.doe123@example.com", "Passw0rd!2024"),
    ("jane.smith456@exa", "S3cureP@ssw0rd"),
    ("johnson789@example.net", "MyP@ssw0rd123"),
    ("emily.brown321@example.edu", "Str0ngP@ssword!"),
    ("michael.jones654@example.co", "   "),
    ("somraj.navale@triarqhealth.com", "P@ssword1"),
    ("robert.white432@example.tv", "@@@@@@@"),
    ("mary.green567@example.us", "Myp@ssw0rd2024"),
    ("david.miller890@example.info", "P@ssw0rd1234!"),
    ("susan.clark123@example.name", "SecreT!2024P@ss")
]


@pytest.fixture
def setup():
    driver = webdriver.Chrome()  # Make sure chromedriver is in your PATH or specify its location
    driver.maximize_window()
    driver.get(URL)
    yield driver
    driver.quit()


@pytest.mark.parametrize("username, password", test_credentials)
def test_Login(setup, username, password):
    driver = setup

    # Perform login
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, User_Name_Field))).send_keys(username)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Password_Field))).send_keys(password)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, Login_Button))).click()

    # Wait for the dashboard to be visible
    dashboard_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Dashboard_Tab)))
    assert dashboard_tab.is_displayed(), "Login failed. Dashboard tab not displayed."
    driver.quit()