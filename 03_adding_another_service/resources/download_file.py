# external
from flask import jsonify
from flask_restful import Resource
# custom
from model.aws import Aws

class DownloadFile(Resource):
    def __init__(self):
        self.aws = Aws()
        pass

    def get(self, researcher, file_id):
        response = self.aws.load_json(researcher+"/"+file_id+".json")
        return jsonify(response)