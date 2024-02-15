from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class CareersPageModel:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    careers_page_xpath = "/html/body"
    careers_location_id = "career-our-location"
    careers_teams_id = "career-find-our-calling"
    carrers_lifeatinsider_xpath = "/html/body/div[1]/section[4]"

    def careersPageIsDisplayed(self):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.careers_page_xpath)))
        status = element.is_displayed()
        return status

    def careersLocationIsDisplayed(self):
        element = self.wait.until(EC.visibility_of_element_located((By.ID, self.careers_location_id)))
        status = element.is_displayed()
        return status

    def careersTeamsIsDisplayed(self):
        element = self.wait.until(EC.visibility_of_element_located((By.ID, self.careers_teams_id)))
        status = element.is_displayed()
        return status

    def careersLifeAtInsiderIsDisplayed(self):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.carrers_lifeatinsider_xpath)))
        status = element.is_displayed()
        return status
