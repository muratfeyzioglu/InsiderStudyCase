import configparser

class ReadConfig:

    @staticmethod
    def getBaseUrl():
        config = configparser.RawConfigParser()
        config.read(".\\Configurations\\config.ini")
        url = config.get("site info", "baseURL")
        return url

    @staticmethod
    def getQaUrl():
        config = configparser.RawConfigParser()
        config.read(".\\Configurations\\config.ini")
        url = config.get("site info", "QaUrl")
        return url

    @staticmethod
    def getLeverUrl():
        config = configparser.RawConfigParser()
        config.read(".\\Configurations\\config.ini")
        url = config.get("site info", "leverUrl")
        return url

    @staticmethod
    def getLocation():
        config = configparser.RawConfigParser()
        config.read(".\\Configurations\\config.ini")
        url = config.get("page info", "Location")
        return url

    @staticmethod
    def getDepartment():
        config = configparser.RawConfigParser()
        config.read(".\\Configurations\\config.ini")
        url = config.get("page info", "Department")
        return url

    @staticmethod
    def getPositions():
        config = configparser.RawConfigParser()
        config.read(".\\Configurations\\config.ini")
        url = config.get("page info", "Position")
        return url