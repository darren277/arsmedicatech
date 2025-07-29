"""
OCR service for calling AWS Textract.
"""
from typing import List, Dict, Any, Tuple

import boto3 # type: ignore
from werkzeug.datastructures import FileStorage

from settings import BUCKET_NAME, TEXTRACT_AWS_ACCESS_KEY_ID, TEXTRACT_AWS_SECRET_ACCESS_KEY
from settings import logger


import json

def extract_text_from_blocks(blocks: List[Dict[str, Any]]) -> str:
    """
    Extract and return plain text from Textract-style OCR output.
    Only extracts LINE-level text in reading order.
    """
    # Filter only blocks of type 'LINE'
    line_blocks: List[Dict[str, Any]] = [b for b in blocks if b.get("BlockType") == "LINE" and "Text" in b]

    # Sort by top position, then by left to approximate reading order
    def sort_key(block: Dict[str, Any]) -> Tuple[float, float]:
        """
        Sort key for blocks.
        :param block: Dict[str, Any] - The block to sort.
        :return: Tuple[float, float] - The sort key.
        """
        top: float = block["Geometry"]["BoundingBox"]["Top"]
        left: float = block["Geometry"]["BoundingBox"]["Left"]
        return (round(top, 3), left)

    line_blocks.sort(key=sort_key)

    lines: List[str] = [b["Text"] for b in line_blocks]
    return "\n".join(lines)



class OCRService:
    """
    A service for performing OCR using AWS Textract.
    """
    def __init__(self, bucket_name: str = BUCKET_NAME) -> None:
        """
        Initializes the OCRService with a Textract client.
        """
        self.client = boto3.client(
            'textract',
            aws_access_key_id=TEXTRACT_AWS_ACCESS_KEY_ID,
            aws_secret_access_key=TEXTRACT_AWS_SECRET_ACCESS_KEY,
        )
        self.bucket_name = bucket_name

    def ocr(self, image_path: str) -> List[Dict[str, Any]]:
        """
        Perform OCR on an image file using AWS Textract.
        :param image_path: str - Path to the image file.
        :return: list - List of detected text blocks.
        """
        with open(image_path, 'rb') as image:
            response = self.client.detect_document_text(Document={'Bytes': image.read()})
            return response['Blocks']

    def get_text(self, blocks: List[Dict[str, Any]]) -> str:
        """
        Extract text from the blocks returned by Textract.
        :param blocks: List[Dict[str, Any]] - List of blocks containing text.
        :return: str - Concatenated text from all LINE blocks.
        """
        return '\n'.join([block['Text'] for block in blocks if block['BlockType'] == 'LINE'])

    def get_text_from_image(self, image_path: str) -> str:
        """
        Get text from an image file.
        :param image_path: str - Path to the image file.
        :return: str - Extracted text from the image.
        """
        blocks = self.ocr(image_path)
        return self.get_text(blocks)
    
    def get_text_from_pdf(self, pdf_path: str) -> str:
        """
        Get text from a PDF file using AWS Textract.
        :param pdf_path: str - Path to the PDF file.
        :return: str - Extracted text from the PDF.
        """
        with open(pdf_path, 'rb') as pdf:
            response = self.client.detect_document_text(Document={'Bytes': pdf.read()})
            return response['Blocks']

    def get_text_from_pdf_file(self, pdf_file: FileStorage) -> str:
        """
        Get text from a PDF file uploaded as a FileStorage object.
        :param pdf_file: FileStorage - The PDF file to process.
        :return: str - Extracted text from the PDF.
        """
        if pdf_file.filename is None:
            raise ValueError("PDF file must have a filename.")
        return self.get_text_from_pdf(pdf_file.filename)

    def get_text_from_pdf_s3(self, pdf_key: str) -> str:
        """
        Get text from a PDF file stored in S3.
        :param bucket_name: str - Name of the S3 bucket.
        :param pdf_key: str - Key of the PDF file in S3.
        :return: str - Extracted text from the PDF.
        """
        # Start async job
        response: Dict[str, Any] = self.client.start_document_text_detection(
            DocumentLocation={'S3Object': {'Bucket': self.bucket_name, 'Name': pdf_key}}
        )
        job_id: str = response['JobId']

        # Poll for job completion
        import time
        while True:
            result: Dict[str, Any] = self.client.get_document_text_detection(JobId=job_id)
            status: str = result['JobStatus']
            logger.warning(f"Textract job status: {status}")
            if status in ['SUCCEEDED', 'FAILED']:
                break
            time.sleep(2)

        if status == 'SUCCEEDED':
            blocks: List[Dict[str, Any]] = result['Blocks']
            logger.warning(f"Textract job completed: {len(blocks)} blocks")
            return extract_text_from_blocks(blocks)
        else:
            logger.error(f"Textract job failed: {result}")
            raise Exception(f"Textract job failed: {result}")

    def get_text_from_image_s3(self, image_key: str) -> str:
        """
        Get text from an image file stored in S3.
        :param bucket_name: str - Name of the S3 bucket.
        :param image_key: str - Key of the image file in S3.
        :return: str - Extracted text from the image.
        """
        response = self.client.detect_document_text(
            Document={'S3Object': {'Bucket': self.bucket_name, 'Name': image_key}})

        blocks = response['Blocks']
        return self.get_text(blocks)


if __name__ == '__main__':
    ocr_service = OCRService()
    print(ocr_service.get_text_from_image('test.png'))
