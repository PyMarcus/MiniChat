import configparser


class ReadIniFile:
    file = "serv_info.ini"

    @classmethod
    def read(cls):
        """Read de ini file for set serv"""
        ini = configparser.RawConfigParser()
        ini.read(cls.file)
        info: dict = {}
        for key, value in ini['serv'].items():
            info[key] = value
        return info
