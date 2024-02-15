from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class HomePageModel:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    accept_cookies_button_id = "wt-cli-accept-all-btn"
    company_dropdown_button_xpath = "//a[contains(text(), 'Company')]"
    careers_button_xpath = "//*[text()='Careers']"

    def clickAcceptCookiesButton(self):
        element = self.wait.until(EC.element_to_be_clickable((By.ID, self.accept_cookies_button_id)))
        element.click()

    def clickCompanyDropdownButton(self):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.company_dropdown_button_xpath)))
        element.click()

    def clickCareersButton(self):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.careers_button_xpath)))
        element.click()
