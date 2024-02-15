import inspect
import logging

class Helper:

    def switchDriver(self, driver):
        new_window_handle = driver.window_handles[-1]
        driver.switch_to.window(new_window_handle)

    @staticmethod
    def loggen():
        #os.remove('.\\Logs\\automation.log')
        #open('.\\Logs\\automation.log', 'a').close()
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        fhandler = logging.FileHandler('.\\Logs\\automation.log')
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.info(' denemeee')
        return logger