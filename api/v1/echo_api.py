from flask import request, jsonify
from api import api, sample_service

@api.route('/v1/echo', methods=['POST'])
def echo():
    echo_request_body = request.json
    print(echo_request_body)
    response = sample_service.echo(echo_request_body)
    return jsonify(response)