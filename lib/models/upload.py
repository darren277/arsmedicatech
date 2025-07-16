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
from settings import BUCKET_NAME, logger, S3_AWS_ACCESS_KEY_ID, S3_AWS_SECRET_ACCESS_KEY


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
            s3 = boto3.client(
                's3',
                aws_access_key_id=S3_AWS_ACCESS_KEY_ID,
                aws_secret_access_key=S3_AWS_SECRET_ACCESS_KEY,
            )
            s3.upload_fileobj(
                file,
                self.bucket_name,
                s3_key,
                ExtraArgs={'ACL': 'private'}
            )
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
    :return: Optional[str] - The ID of the created upload record (just the ID, not 'table:id').
    """
    db = DbController()
    try:
        db.connect()
        # Ensure uploader is stored as a record link (user:<id>)
        uploader_id = str(upload.uploader)
        if uploader_id.startswith("user:"):
            uploader_link = uploader_id
        elif ":" in uploader_id:
            uploader_link = f"user:{uploader_id.split(':')[-1]}"
        else:
            uploader_link = f"user:{uploader_id}"
        upload_dict = upload.to_dict()
        #upload_dict["uploader"] = {"@link": uploader_link}
        upload_dict["uploader"] = uploader_link
        result = db.create("upload", upload_dict)
        #result = db.query("CREATE upload CONTENT $data", {"data": upload_dict})
        logger.warning(f"Upload create result: {result}")
        if not result:
            logger.warning("db.create returned no result! Upload may not have been saved.")
        if result and 'id' in result:
            full_id = str(result['id'])
            # Extract just the ID part after the colon if present
            if ':' in full_id:
                return full_id.split(':', 1)[1]
            return full_id
        return None
    except Exception as e:
        logger.error(f"Error creating upload: {e}")
        return None
    finally:
        db.close()

def parse_upload(upload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Parse an upload record into an Upload object.
    """
    for key, value in upload.items():
        if key == "uploader":
            upload["uploader"] = str(value)
        elif key == "id":
            upload["id"] = str(value)
    return upload

def get_uploads_by_user(user_id: UserID) -> List[Dict[str, Any]]:
    """
    Get all uploads for a specific user.
    :param user_id: UserID - The user ID to get uploads for.
    :return: List[Dict[str, Any]] - List of upload records.
    """
    db = DbController()
    try:
        db.connect()
        # Always use just the id part for the record link
        id_part = str(user_id)
        if ":" in id_part:
            id_part = id_part.split(":")[-1]
        uploader_link = f"user:{id_part}"

        logger.warning(f"UPLOADER LINK: {uploader_link}")
        
        # Query using uploader link string
        res = db.query(
            "SELECT * FROM upload WHERE uploader = $uid ORDER BY date_uploaded DESC",
            {"uid": uploader_link}
        )
        
        logger.warning(f"RAW DB RESULT: {res}")

        return [parse_upload(r) for r in res]
        
    except Exception as e:
        logger.error(f"Error getting uploads for user {user_id}: {e}")
        return []
    finally:
        db.close()

def update_upload_status(upload_id: str, status: UploadStatus, processed_text: str = "", task_id: str = "") -> bool:
    """
    Update the status of an upload, merging with existing fields to avoid overwriting other attributes.
    :param upload_id: str - The ID of the upload to update.
    :param status: UploadStatus - The new status.
    :param processed_text: str - The processed text (optional).
    :param task_id: str - The task ID (optional).
    :return: bool - True if successful, False otherwise.
    """
    # Normalize upload_id to just the ID part (strip any prefix like 'upload:')
    if ":" in upload_id:
        upload_id = upload_id.split(':')[-1]
    db = DbController()
    try:
        db.connect()
        
        # Build only the fields that can change
        patch: Dict[str, Any] = {"status": status.value}
        if processed_text:
            patch["processed_text"] = processed_text
        if task_id:
            patch["task_id"] = task_id

        # MERGE keeps everything else intact
        sql = "UPDATE type::thing('upload', $rid) MERGE $data"
        result = db.query(sql, {"rid": upload_id, "data": patch})

        logger.warning(f"Upload status update MERGE result: {result}")
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
        logger.warning(f"GET UPLOAD BY ID: {upload_id}")
        if ":" in upload_id:
            table, rid = upload_id.split(":")
        else:
            table, rid = "upload", upload_id

        result = db.query(
            "SELECT * FROM type::thing($table, $id)",
            {"table": table, "id": rid}
        )

        # db.query returns a list, so we need to get the first item
        if not result or len(result) == 0:
            return None
            
        upload_data = result[0]  # Get the first (and should be only) item
        if not upload_data:
            return None

        # Create a copy to avoid modifying the original
        upload_dict = dict(upload_data)
        
        # Remove the id field and store uploader separately
        upload_dict.pop("id", None)
        uploader = upload_dict.pop("uploader", None)

        # Add back the fields with proper formatting
        upload_dict["id"] = upload_id
        upload_dict["uploader"] = str(uploader) if uploader else ""

        logger.warning(f"GET UPLOAD BY ID RESULT: {upload_dict}")
        return upload_dict
    except Exception as e:
        logger.error(f"Error getting upload {upload_id}: {e}")
        return None
    finally:
        db.close()
