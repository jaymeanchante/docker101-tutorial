# core
import json
from uuid import uuid4
# external
from flask import request
from flask_restful import Resource
# custom
from model.aws import Aws

class UploadFile(Resource):
    def __init__(self):
        self.aws = Aws()
        pass

    def post(self, researcher):
        data = request.get_json()
        response = self.aws.dump_json(researcher+"/"+str(uuid4())+".json", data)
        return response