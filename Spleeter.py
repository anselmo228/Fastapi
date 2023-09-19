from fastapi import FastAPI, File, Form, UploadFile
import boto3
from spleeter.separator import Separator
import multiprocessing

app = FastAPI()

# AWS S3 연결 함수
def s3_connection():
    try:
        s3 = boto3.client(
            service_name="s3",
            region_name="ap-northeast-2",  # 자신의 S3 버킷의 리전을 지정
            aws_access_key_id='AKIA2R3FKW6ILEFUHTXP',
            aws_secret_access_key='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',
        )
    except Exception as e:
        print(e)
    else:
        print("S3 bucket connected!")
        return s3
    
def separate_audio(input_audio_file):
    separator = Separator('spleeter:2stems')  # 2stems 모델은 보컬과 MR을 분리해준다
    ### 보컬과 MR을 분리 되는 곳###
    separator.separate_to_file(input_audio_file, 'output')

# MR과 AR 분리 및 S3에 파일 업로드 함수
def s3_put_object(input_audio_file, s3, bucket, file, access_key):
    separator = Separator('spleeter:2stems')  # 2stems 모델은 보컬과 MR을 분리해준다
    ### 보컬과 MR을 분리 되는 곳###
    separator.separate_to_file(input_audio_file, 'output')
    
    try:
        s3.upload_fileobj(
            file.file,  # 업로드할 파일
            Bucket=bucket,
            Key=access_key,  # S3에 저장될 파일 이름
            ExtraArgs={"ContentType": "sound/wav", "ACL": "public-read"},
        )
    except Exception as e:
        print(e)
        return False
    print('success')
    return True


if __name__ == '__main__':
    input_audio_file = 'Song/Dynamite.wav'

    # multiprocessing을 사용하여 분리 작업을 실행
    multiprocessing.freeze_support()
    separate_audio(input_audio_file)