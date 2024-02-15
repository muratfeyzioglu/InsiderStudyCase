import time
from PageObjects.HomePageModel import HomePageModel
from PageObjects.CareersPageModel import CareersPageModel
from PageObjects.QAPageModel import QaPageModel
from Utilities.Helper import Helper
from Utilities.readProperties import ReadConfig

class Test_Deneme:

    def test_deneme(self, setup):

        baseURL = ReadConfig.getBaseUrl()
        qaURL = ReadConfig.getQaUrl()
        leverURL = ReadConfig.getLeverUrl()

        locationISTfromConfig = ReadConfig.getLocation()
        departmentfromConfig = ReadConfig.getDepartment()
        positionfromConfig = ReadConfig.getPositions()

        driver = setup
        driver.maximize_window()
        driver.implicitly_wait(20)

        homepage = HomePageModel(driver)
        careerspage = CareersPageModel(driver)
        qapage = QaPageModel(driver)
        helper = Helper()
        logger = Helper.loggen()

        driver.get(baseURL)
        logger.info("Starting")

        assert "#1 Leader in Individualized, Cross-Channel CX \u2014 Insider" in driver.title
        logger.info(driver.title)

        homepage.clickAcceptCookiesButton()
        logger.info("click the cookies- Accept-Cookies button")

        homepage.clickCompanyDropdownButton()
        logger.info("click the company- dropdown button")

        homepage.clickCareersButton()
        logger.info("click the careers- button")

        time.sleep(5)
        assert careerspage.careersPageIsDisplayed()
        assert careerspage.careersTeamsIsDisplayed()
        assert careerspage.careersLocationIsDisplayed()
        assert careerspage.careersLifeAtInsiderIsDisplayed()

        driver.get(qaURL)
        logger.info(f"Go to: {qaURL}")

        qapage.clickSeeAllQaJobsButton()
        logger.info("click the see-all-qa-jobs- button")

        time.sleep(2)
        qapage.clickLocationFilter()
        logger.info("click the location-filter")
        qapage.selectFilterElement(locationISTfromConfig)
        logger.info(f"select the location-filter: {locationISTfromConfig}")

        qapage.clickDepartmentFilter()
        qapage.selectFilterElement(departmentfromConfig)
        logger.info(f"select the department-filter: {departmentfromConfig}")

        time.sleep(2)

        driver.execute_script("arguments[0].scrollIntoView(true);", qapage.getJobList())
        logger.info("Scroll down")

        job_elements = qapage.getJobElements()
        logger.info("getting job elements")

        elementsize = len(job_elements)
        print(elementsize)

        position_positions = qapage.getPositionsList()
        position_department = qapage.getDepartmentsList()
        position_locations = qapage.getLocationsList()

        #search the positions, locations, and department from the job elements
        for i in range(elementsize):
            positions = position_positions[i].text
            assert positionfromConfig in positions

            department = position_department[i].text
            assert departmentfromConfig in department

            location = position_locations[i].text
            assert locationISTfromConfig in location


        qapage.clickViewRoleButton()
        helper.switchDriver(driver)

        assert leverURL in driver.current_url

        stopper = input()
# pytest -v -s Tests/test_demo.py
