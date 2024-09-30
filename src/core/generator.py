import os
from dataclasses import dataclass

import boto3
import crcmod
import dotenv
import qrcode

from src.core.dto.generate_pix import ResponseGeneratePix

dotenv.load_dotenv()

@dataclass
class GenerateQRCode():
    key: str
    value: str
    image_url: str = ""
    name_receiver: str = "N"
    city_receiver: str = "C"

    def calcular_crc16(self, payload: str) -> str:
        crc16_func = crcmod.mkCrcFun(0x11021, initCrc=0xFFFF, rev=False, xorOut=0x0000)
        crc = hex(crc16_func(payload.encode('utf-8'))).upper()[2:]
        return crc.zfill(4)

    def gerar_payload_pix(self):
        payload_format_indicator = "000201"
        point_of_initiation_method = "010212" 
        merchant_account_information = f"0014BR.GOV.BCB.PIX01{len(self.key):02d}{self.key}"
        merchant_account_information_length = f"26{len(merchant_account_information):02d}"
        merchant_category_code = "52040000"  
        transaction_currency = "5303986" 
        transaction_amount = f"54{len(self.value):02d}{self.value}"  
        country_code = "5802BR"
        merchant_name = f"59{len(self.name_receiver):02d}{self.name_receiver}"
        merchant_city = f"60{len(self.city_receiver):02d}{self.city_receiver}"
        additional_data_field_template = "62070503***"
        crc_placeholder = "6304"

        br_code = (
            payload_format_indicator +
            point_of_initiation_method +
            merchant_account_information_length +
            merchant_account_information +
            merchant_category_code +
            transaction_currency +
            transaction_amount +
            country_code +
            merchant_name +
            merchant_city +
            additional_data_field_template +
            crc_placeholder
        )

        crc_value = self.calcular_crc16(br_code)
        return br_code + crc_value
    
    async def gerar_qrcode_pix(self)->ResponseGeneratePix:
        payload = self.gerar_payload_pix()
        nome_arquivo = f"{self.key+self.value}.png"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(payload)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img.save(nome_arquivo)
        
        try:
            file_url = self.upload_to_s3(nome_arquivo)
            self.clean_dir_files(nome_arquivo)
            return ResponseGeneratePix(url=file_url, payload=payload)
        except Exception as e:
            raise e

    def upload_to_s3(self, nome_arquivo: str) -> str:
        s3 = boto3.resource(
            service_name='s3',
            aws_access_key_id=os.getenv("S3_KEY"),
            aws_secret_access_key=os.getenv("S3_KEY_SECRET"),
            endpoint_url='https://s3.tebi.io'
        )
        data = open(nome_arquivo, 'rb')
        s3.Bucket(os.getenv("S3_NAME")).put_object(
            Key=nome_arquivo, 
            Body=data,
            ACL='public-read'
        )
        return f"https://{os.getenv('S3_NAME')}.s3.tebi.io/{nome_arquivo}"

    def clean_dir_files(self, name_file: str):
        os.remove(name_file)
        return True