# core
import os
import json
import datetime
from io import StringIO
# external
import boto3

class Aws:
    def __init__(self):
        self.aws_access_key = "AKIAIOSFODNN7EXAMPLE"
        self.aws_secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
        self.bucket = "iris"
        self.endpoint_url = "http://localhost:4572"
        self.client = self._get_client()
        self.error_description = "Please check your status code in https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html"
        pass
    def _get_client(self):
        """
        Create an AWS connection
        """
        client = boto3.client(
            "s3",
            aws_access_key_id=self.aws_access_key,
            aws_secret_access_key=self.aws_secret_key,
            endpoint_url=self.endpoint_url
            )
        return client
    def create_bucket(self, bucket):
        """
        Create an AWS S3 Bucket
        """
        response = self.client.create_bucket(Bucket=bucket)
        return response
    def _put_object(self, key, body):
        """
        Upload contents to a S3 Key
        """
        response = self.client.put_object(Bucket=self.bucket, Key=key, Body=body)
        return response
    def _make_response(self, response, key):
        status_code = response["ResponseMetadata"]["HTTPStatusCode"]
        unformatted_date = response["ResponseMetadata"]["HTTPHeaders"]["date"]
        date = datetime.datetime.strptime(unformatted_date, "%a, %d %b %Y %H:%M:%S %Z").strftime("%Y-%m-%d %H:%M:%S")
        response = {"status_code": status_code, "date": date}
        if response["status_code"] ==  200:
            response["description"] = "Successfully uploaded contents!"
            response["Key"] = key
        else:
            response["description"] = self.error_description
        return response
    def dump_json(self, key, json_dict, **kwargs):
        """
        Dump a list/dictionary to a S3 Key
        """
        json_buffer = StringIO()
        json.dump(json_dict, json_buffer, ensure_ascii=False, **kwargs)
        response = self._put_object(key, json_buffer.getvalue())
        response = self._make_response(response, key)
        return response
    def list_files(self, prefix=""):
        """
        List available files in S3
        """
        response = self.client.list_objects(Bucket=self.bucket, MaxKeys=1000, Prefix=prefix)
        files = []
        if "Contents" in response:
            contents = response["Contents"]
            for item in contents:
                files.append(item["Key"])
        return files
    def _get_object(self, key):
        """
        Get object
        """
        aws_object = self.client.get_object(Bucket=self.bucket, Key=key)
        return aws_object
    def load_json(self, key, **kwargs):
        """
        Load a S3 key and return a list/dictionary
        """
        try:
            json_object = self._get_object(key)
            json_dict = json.load(json_object["Body"], **kwargs)
        except:
            json_dict = {"description": "this key is not available", "Key": key}
        return json_dict