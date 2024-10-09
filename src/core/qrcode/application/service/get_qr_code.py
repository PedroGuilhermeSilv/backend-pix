import os
from dataclasses import dataclass

import boto3
import dotenv

dotenv.load_dotenv()

@dataclass
class GetQrCode:
    file_name: str

    def download_from_s3(self, url: str) -> str:
        s3 = boto3.client(
            service_name='s3',
            aws_access_key_id=os.getenv("S3_KEY"),
            aws_secret_access_key=os.getenv("S3_KEY_SECRET"),
            endpoint_url='https://s3.tebi.io'
        )
        nome_arquivo = f"{self.file_name}.png"
        s3.download_file(os.getenv("S3_NAME"), url, nome_arquivo)
        return nome_arquivo


