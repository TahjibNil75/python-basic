# Description: This module defines an abstract base class for a storage service and two concrete implementations: one for AWS S3 and another for local file storage.

from abc import ABC, abstractmethod

class StorageService(ABC):
    @abstractmethod
    def upload_file(self, file_path, destination):
        pass

    @abstractmethod
    def download_file(self, file_path, destination):
        pass


class S3StorageService(StorageService):
    def upload_file(self, file_path, destination):
        return f"Uploading {file_path} to S3 at {destination}."

    def download_file(self, file_path, destination):
        return f"Downloading {file_path} from S3 to {destination}."
    
class LocalStorageService(StorageService):
    def upload_file(self, file_path, destination):
        return f"Uploading {file_path} to local storage at {destination}."

    def download_file(self, file_path, destination):
        return f"Downloading {file_path} from local storage to {destination}."
    

s3 = S3StorageService()
local = LocalStorageService()

print(s3.upload_file("data.txt", "/s3/bucket/data.txt"))
print(s3.download_file("data.txt", "/local/data.txt"))

print(local.upload_file("image.png", "/local/images/image.png"))
print(local.download_file("image.png", "/local/downloads/image.png"))