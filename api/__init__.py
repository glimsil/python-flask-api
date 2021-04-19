from flask import Blueprint
from service.sample_service import SampleService
api = Blueprint('api', __name__)
sample_service = SampleService()

from api.v1.echo_api import *
from api.v1.hello_api import *