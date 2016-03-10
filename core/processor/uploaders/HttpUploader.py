import requests

from core.processor.processor import Processor


class HttpUploader(Processor):
    def __init__(self, file, location, credentials):
        self.credentials = credentials
        self.location = location
        self.file = file

    def run(self):
        response = requests.post(
                self.location,
                auth=(self.credentials.username, self.credentials.password),
                files={'file': open(self.file, 'rb')}
        )

        response.raise_for_status()

