"""
OCR service for calling AWS Textract.
"""
from typing import List, Dict, Any

import boto3
from werkzeug.datastructures import FileStorage

from settings import BUCKET_NAME


class OCRService:
    """
    A service for performing OCR using AWS Textract.
    """
    def __init__(self, bucket_name: str = BUCKET_NAME) -> None:
        """
        Initializes the OCRService with a Textract client.
        """
        self.client = boto3.client('textract')
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
        return self.get_text_from_pdf(pdf_file.filename)

    def get_text_from_pdf_s3(self, pdf_key: str) -> str:
        """
        Get text from a PDF file stored in S3.
        :param bucket_name: str - Name of the S3 bucket.
        :param pdf_key: str - Key of the PDF file in S3.
        :return: str - Extracted text from the PDF.
        """
        response = self.client.get_document_text_detection(
            Document={'S3Object': {'Bucket': self.bucket_name, 'Name': pdf_key}})

        blocks = response['Blocks']
        return self.get_text(blocks)

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

    def upload_file_to_s3(self, file: FileStorage, s3_key: str) -> None:
        """
        Upload a file to S3.
        :param file: FileStorage - The file to upload.
        :param s3_key: str - The key under which to store the file in S3.
        """
        s3 = boto3.client('s3')
        s3.upload_fileobj(file, self.bucket_name, s3_key)
        print(f"File uploaded to {self.bucket_name}/{s3_key}")


if __name__ == '__main__':
    ocr_service = OCRService()
    print(ocr_service.get_text_from_image('test.png'))
