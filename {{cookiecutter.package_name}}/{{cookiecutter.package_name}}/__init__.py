import os
from flask import Flask
from healthcheck import HealthCheck

from config import config as cfg

_VERSION = '/v1'


def create_app(config_name=None):

    config_name = config_name or os.getenv('FLASK_CONFIG') or 'default'

    app = Flask(__name__)
    app.url_map.strict_slashes = False

    app.config.from_object(cfg[config_name])

    health = HealthCheck(app, _VERSION+'/healthcheck')

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix=_VERSION)

    return app
