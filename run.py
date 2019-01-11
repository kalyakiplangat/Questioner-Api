import os
from flask import Flask
from app import create_app

configur = os.getenv('APP_SETTINGS')
if configur:
    app = create_app(configur)
else:
    config_ = os.getenv('FLASK_ENV')
    app = create_app(config_)


if __name__ == '__main__':
    app.run(debug=True)