# external
from flask import Flask
from flask_restful import Api
# custom
from resources.create_bucket import CreateBucket
from resources.upload_file import UploadFile
from resources.list_files import ListFiles
from resources.download_file import DownloadFile


app = Flask(__name__)
api = Api(app)
api.add_resource(CreateBucket, "/create_bucket/<string:bucket>")
api.add_resource(UploadFile, "/upload_file/<string:researcher>")
api.add_resource(ListFiles, "/list_files/<string:researcher>")
api.add_resource(DownloadFile, "/download_file/<string:researcher>/<string:file_id>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)