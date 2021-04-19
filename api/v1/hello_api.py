from flask import jsonify
from api import api, sample_service
import socket

@api.route('/v1/hello', methods=['GET'])
def hello_world():
    return jsonify(sample_service.hello_world())