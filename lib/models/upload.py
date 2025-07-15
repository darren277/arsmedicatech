"""
Model for uploading files to S3.
"""

import datetime
from enum import Enum
from typing import Any, Dict

from lib.data_types import UserID

import boto3
from werkzeug.datastructures import FileStorage

from settings import BUCKET_NAME

class FileType(Enum):
    """
    Enum for file types.
    """
    PDF = "pdf"
    IMAGE = "image"
    TEXT = "text"
    VIDEO = "video"
    AUDIO = "audio"


class Upload:
    """
    Model for uploading files to S3.
    """
    def __init__(
            self,
            uploader: UserID,
            file_name: str,
            file_path: str,
            file_type: FileType,
            bucket_name: str = BUCKET_NAME,
            date_uploaded: datetime.datetime = datetime.datetime.now(),
    ) -> None:
        """
        Initialize the Upload model.
        :param uploader: UserID - The user who is uploading the file.
        :param file_name: str - The name of the file.
        :param file_path: str - The path of the file.
        :param file_type: FileType - The type of the file.
        :param bucket_name: str - The name of the S3 bucket.
        :param date_uploaded: datetime.datetime - The date and time the file was uploaded.
        """
        self.uploader = uploader
        self.file_name = file_name
        self.file_path = file_path
        self.file_type = file_type
        self.bucket_name = bucket_name
        self.date_uploaded = date_uploaded

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the model to a dictionary.
        """
        return {
            "uploader": self.uploader,
            "file_name": self.file_name,
            "file_path": self.file_path,
            "file_type": self.file_type,
            "date_uploaded": self.date_uploaded,
        }

    def upload_file_to_s3(self, file: FileStorage, s3_key: str) -> None:
        """
        Upload a file to S3.
        :param file: FileStorage - The file to upload.
        :param s3_key: str - The key under which to store the file in S3.
        """
        s3 = boto3.client('s3')
        s3.upload_fileobj(file, self.bucket_name, s3_key)
        print(f"File uploaded to {self.bucket_name}/{s3_key}")