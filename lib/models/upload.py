"""
Model for uploading files to S3.
"""

import datetime
import os
import uuid
from enum import Enum
from typing import Any, Dict, List, Optional

import boto3 # type: ignore
from werkzeug.datastructures import FileStorage

from lib.data_types import UserID
from lib.db.surreal import DbController
from settings import BUCKET_NAME, logger


class FileType(Enum):
    """
    Enum for file types.
    """
    PDF = "pdf"
    IMAGE = "image"
    TEXT = "text"
    VIDEO = "video"
    AUDIO = "audio"
    UNKNOWN = "unknown"

class UploadStatus(Enum):
    """
    Enum for upload statuses.
    """
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

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
            date_uploaded: Optional[datetime.datetime] = None,
            status: UploadStatus = UploadStatus.PENDING,
            file_size: int = 0,
            s3_key: str = "",
            processed_text: str = "",
            task_id: str = "",
    ) -> None:
        """
        Initialize the Upload model.
        :param uploader: UserID - The user who is uploading the file.
        :param file_name: str - The name of the file.
        :param file_path: str - The path of the file.
        :param file_type: FileType - The type of the file.
        :param bucket_name: str - The name of the S3 bucket.
        :param date_uploaded: datetime.datetime - The date and time the file was uploaded.
        :param status: UploadStatus - The status of the upload.
        :param file_size: int - The size of the file in bytes.
        :param s3_key: str - The S3 key for the uploaded file.
        :param processed_text: str - The extracted text from the file.
        :param task_id: str - The Celery task ID for processing.
        """
        self.uploader = uploader
        self.file_name = file_name
        self.file_path = file_path
        self.file_type = file_type
        self.bucket_name = bucket_name
        self.date_uploaded = date_uploaded or datetime.datetime.now()
        self.status = status
        self.file_size = file_size
        self.s3_key = s3_key
        self.processed_text = processed_text
        self.task_id = task_id

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the model to a dictionary.
        """
        return {
            "uploader": str(self.uploader),
            "file_name": self.file_name,
            "file_path": self.file_path,
            "file_type": self.file_type.value,
            "bucket_name": self.bucket_name,
            "date_uploaded": self.date_uploaded.isoformat(),
            "status": self.status.value,
            "file_size": self.file_size,
            "s3_key": self.s3_key,
            "processed_text": self.processed_text,
            "task_id": self.task_id,
        }

    def upload_file_to_s3(self, file: FileStorage, s3_key: str) -> None:
        """
        Upload a file to S3.
        :param file: FileStorage - The file to upload.
        :param s3_key: str - The key under which to store the file in S3.
        """
        try:
            s3 = boto3.client('s3')
            s3.upload_fileobj(file, self.bucket_name, s3_key)
            self.s3_key = s3_key
            logger.info(f"File uploaded to {self.bucket_name}/{s3_key}")
        except Exception as e:
            logger.error(f"Failed to upload file to S3: {e}")
            raise

    @staticmethod
    def get_file_type_from_extension(filename: str) -> FileType:
        """
        Determine file type from file extension.
        :param filename: str - The filename to analyze.
        :return: FileType - The determined file type.
        """
        if not filename:
            return FileType.UNKNOWN
            
        extension = os.path.splitext(filename)[1].lower()
        
        image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
        pdf_extensions = {'.pdf'}
        text_extensions = {'.txt', '.md', '.csv', '.json', '.xml', '.html', '.htm'}
        video_extensions = {'.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mkv'}
        audio_extensions = {'.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'}
        
        if extension in image_extensions:
            return FileType.IMAGE
        elif extension in pdf_extensions:
            return FileType.PDF
        elif extension in text_extensions:
            return FileType.TEXT
        elif extension in video_extensions:
            return FileType.VIDEO
        elif extension in audio_extensions:
            return FileType.AUDIO
        else:
            return FileType.UNKNOWN

    @staticmethod
    def generate_s3_key(uploader: UserID, filename: str) -> str:
        """
        Generate a unique S3 key for the file.
        :param uploader: UserID - The user uploading the file.
        :param filename: str - The original filename.
        :return: str - The generated S3 key.
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_id = str(uuid.uuid4())[:8]
        extension = os.path.splitext(filename)[1]
        return f"uploads/{uploader}/{timestamp}_{unique_id}{extension}"

def create_upload(upload: Upload) -> Optional[str]:
    """
    Create an upload record in the database.
    :param upload: Upload - The upload object to create.
    :return: Optional[str] - The ID of the created upload record.
    """
    db = DbController()
    try:
        db.connect()
        result = db.create("upload", upload.to_dict())
        logger.debug(f"Upload create result: {result}")
        
        if result and 'id' in result:
            return str(result['id'])
        return None
    except Exception as e:
        logger.error(f"Error creating upload: {e}")
        return None
    finally:
        db.close()

def get_uploads_by_user(user_id: UserID) -> List[Dict[str, Any]]:
    """
    Get all uploads for a specific user.
    :param user_id: UserID - The user ID to get uploads for.
    :return: List[Dict[str, Any]] - List of upload records.
    """
    db = DbController()
    try:
        db.connect()
        result = db.query("SELECT * FROM upload WHERE uploader = $user_id ORDER BY date_uploaded DESC", 
                         {"user_id": str(user_id)})
        
        if result and len(result) > 0:
            # Extract the result array from the first item
            uploads = result[0].get('result', []) if isinstance(result[0], dict) else result
            return uploads if isinstance(uploads, list) else []
        return []
    except Exception as e:
        logger.error(f"Error getting uploads for user {user_id}: {e}")
        return []
    finally:
        db.close()

def update_upload_status(upload_id: str, status: UploadStatus, processed_text: str = "", task_id: str = "") -> bool:
    """
    Update the status of an upload.
    :param upload_id: str - The ID of the upload to update.
    :param status: UploadStatus - The new status.
    :param processed_text: str - The processed text (optional).
    :param task_id: str - The task ID (optional).
    :return: bool - True if successful, False otherwise.
    """
    db = DbController()
    try:
        db.connect()
        update_data = {"status": status.value}
        if processed_text:
            update_data["processed_text"] = processed_text
        if task_id:
            update_data["task_id"] = task_id
            
        result = db.update(f"upload:{upload_id}", update_data)
        logger.debug(f"Upload status update result: {result}")
        return bool(result)
    except Exception as e:
        logger.error(f"Error updating upload status: {e}")
        return False
    finally:
        db.close()

def get_upload_by_id(upload_id: str) -> Optional[Dict[str, Any]]:
    """
    Get an upload by its ID.
    :param upload_id: str - The ID of the upload.
    :return: Optional[Dict[str, Any]] - The upload record or None.
    """
    db = DbController()
    try:
        db.connect()
        result = db.select(f"upload:{upload_id}")
        return result if result else None
    except Exception as e:
        logger.error(f"Error getting upload {upload_id}: {e}")
        return None
    finally:
        db.close()
