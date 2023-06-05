from app import create_app
from config import app_active, app_config


config = app_config[app_active]
config.APP = create_app

app = lambda _ = "_": config.APP()

if __name__ == "__main__":
    app().run(debug=config.DEBUG, host=config.IP_HOST, port=config.PORT_HOST)