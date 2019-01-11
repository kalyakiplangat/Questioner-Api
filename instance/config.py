import os 


class BaseConfig(object):
    """base configurations"""
    DEBUG = False

class Testing(BaseConfig):
    DEBUG = True

class Development(BaseConfig):
    DEBUG = True

class Production(BaseConfig):
    DEBUG = False

app_config = {
    "development": Development,
    "testing": Testing,
    "production": Production
}