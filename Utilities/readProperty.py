import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\Config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def getUserName():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getSFApplicationURL():
        url = config.get('common info', 'sfUrl')
        return url

    @staticmethod
    def getSFUserName():
        username = config.get('common info', 'sf_username')
        return username

    @staticmethod
    def getSFPassword():
        password = config.get('common info', 'sf_password')
        return password
