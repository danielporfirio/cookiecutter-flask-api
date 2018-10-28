from flask import jsonify
from {{cookiecutter.package_name}}.exceptions import ValidationError
from . import api


@api.app_errorhandler(404)
def not_found(e):
    return jsonify({'error': 'not found'}), 404


@api.app_errorhandler(500)
def internal_server_error(e):
    return jsonify({'error': 'internal server error'}), 500  # pragma: no cover


@api.errorhandler(ValidationError)
def validation_error(e):
    return jsonify({'error': 'bad request', 'message': e.message}), 400
