# external
from flask_restful import Resource
# customer
from model.aws import Aws

class CreateBucket(Resource):
    def __init__(self):
        self.aws = Aws()
        
    def post(self, bucket):
        response = self.aws.create_bucket(bucket)
        return response