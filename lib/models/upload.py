"""
Model for uploading files to S3.
"""

import datetime
from enum import Enum
from typing import Any, Dict

from lib.data_types import UserID

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
            date_uploaded: datetime.datetime,
    ) -> None:
        """
        Initialize the Upload model.
        :param uploader: UserID - The user who is uploading the file.
        :param file_name: str - The name of the file.
        :param file_path: str - The path of the file.
        :param file_type: FileType - The type of the file.
        :param date_uploaded: datetime.datetime - The date and time the file was uploaded.
        """
        self.uploader = uploader
        self.file_name = file_name
        self.file_path = file_path
        self.file_type = file_type
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