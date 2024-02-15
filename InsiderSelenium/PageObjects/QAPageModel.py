from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class QaPageModel:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(20)
        self.wait = WebDriverWait(self.driver, 10)

    seeAllQaJobs_button_xpath = "//*[text()='See all QA jobs']"
    location_filter_dropdown_id = "select2-filter-by-location-container"
    department_filter_dropdown_id = "select2-filter-by-department-container"
    job_elements_xpath = "//div[@id='jobs-list']//div[contains(@class, 'position-list-item')]//p[contains(@class, 'position-title')]"
    job_list_id = "jobs-list"
    positions_xpath = "//div[@id='jobs-list']//div[contains(@class, 'position-list-item')]//p[contains(@class, 'position-title')]"
    departments_xpath = "//div[@id='jobs-list']//div[contains(@class, 'position-list-item')]//span[contains(@class, 'position-department')]"
    locations_xpath = "//div[@id='jobs-list']//div[contains(@class, 'position-list-item')]//div[contains(@class, 'position-location')]"
    view_role_button_xpath = "//*[text()='View Role']"

    def clickSeeAllQaJobsButton(self):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.seeAllQaJobs_button_xpath)))
        element.click()

    def clickLocationFilter(self):
        element = self.wait.until(EC.element_to_be_clickable((By.ID, self.location_filter_dropdown_id)))
        element.click()

    def clickDepartmentFilter(self):
        element = self.wait.until(EC.element_to_be_clickable((By.ID, self.department_filter_dropdown_id)))
        element.click()

    def selectFilterElement(self, key):
        xpath = "//li[contains(text(),'" + key +"')]"
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()

    def getJobElements(self):
        elements = self.driver.find_elements(By.XPATH, self.job_elements_xpath)
        return elements

    def getJobList(self):
        element = self.driver.find_element(By.ID, self.job_list_id)
        return element

    def getPositionsList(self):
        elements = self.driver.find_elements(By.XPATH, self.positions_xpath)
        return elements

    def getDepartmentsList(self):
        elements = self.driver.find_elements(By.XPATH, self.departments_xpath)
        return elements

    def getLocationsList(self):
        elements = self.driver.find_elements(By.XPATH, self.locations_xpath)
        return elements

    def clickViewRoleButton(self):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.view_role_button_xpath)))
        element.click()


