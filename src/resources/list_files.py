# external
from flask import jsonify
from flask_restful import Resource
# custom
from model.aws import Aws

class ListFiles(Resource):
    def __init__(self):
        self.aws = Aws()
        pass

    def get(self, researcher):
        response = self.aws.list_files(researcher)
        return jsonify(response)