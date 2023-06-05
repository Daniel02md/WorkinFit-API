import os

class __Config(object):
    SECRET = "047a5134f25021504881d296ead9d6c99293431eae656eb6b2e250de1d303c32"
    APP = None


class Development(__Config):
    TESTING = False
    DEBUG = True
    IP_HOST = "localhost"
    PORT_HOST = "5000"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:020205md@localhost:3306/development"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Testing(__Config):
    pass

class Production(__Config):
    pass

app_config = {
    "development": Development(),
    "testing": Testing(),
    "production": Production()
}


app_active = os.getenv("FLASK_ENV")

if not app_active: 
    app_active = "development"