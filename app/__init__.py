from flask import Flask

"""local imports"""

from instance.config import app_config
from app.api.v1.views.meetup_view import meetupre
#from app.api.v1.views.user_view import userview
#from app.api.v1.views.question_view import questionreq

def create_app(Config):
    """Create all configs"""
    app = Flask(__name__, instance_relative_config=True)
    app.config['JSON_SORT_KEYS'] = False
    #app.config.from_object(app_config[config])
    app.config.from_pyfile('config.py', silent=True)

    app.register_blueprint(meetupre)
    #app.register_blueprint(userview)
    #app.register_blueprint(questionreq)
    return app