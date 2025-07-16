from celery_worker import celery_app
from lib.models.upload import Upload, UploadStatus, update_upload_status
from lib.services.ocr import OCRService
from settings import logger


@celery_app.task(bind=True)
def process_upload_task(self, upload_id: str, file_type: str, s3_key: str):
    """
    Celery task to process an uploaded file (OCR or transcription).
    Updates the Upload status in the database.
    """
    logger.info(f"[Celery] Processing upload {upload_id} (type={file_type}, s3_key={s3_key})")
    try:
        result = update_upload_status(upload_id, UploadStatus.PROCESSING)
        logger.debug(f"[Celery] Update upload status result: {result}")
        result_text = ""
        if file_type in ("pdf", "image"):
            ocr_service = OCRService()
            # Use S3-based OCR for scalability
            if file_type == "pdf":
                result_text = ocr_service.get_text_from_pdf_s3(s3_key)
            else:
                result_text = ocr_service.get_text_from_image_s3(s3_key)
        elif file_type == "audio":
            # Placeholder for audio transcription
            result_text = "[Transcription not implemented yet]"
        else:
            # No processing for text/unknown
            result_text = ""
        result = update_upload_status(upload_id, UploadStatus.COMPLETED, processed_text=result_text)
        logger.warning(f"[Celery] Update upload status result: {result}")
        logger.warning(f"[Celery] Upload {upload_id} processed successfully.")
    except Exception as e:
        logger.error(f"[Celery] Failed to process upload {upload_id}: {e}")
        update_upload_status(upload_id, UploadStatus.FAILED, processed_text=str(e))
