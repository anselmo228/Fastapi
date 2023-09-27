from fastapi import FastAPI, File, Form, UploadFile

import boto3

app = FastAPI()
# 파일 업로드 크기 제한 해제
app.config = {"max_request_body_size": None}

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

# S3에 파일 업로드 함수
def s3_put_object(s3, bucket, file, access_key):
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

# 파일 업로드 엔드포인트
@app.post("/upload/")
async def upload_file(file: UploadFile, access_key: str = Form(...)):
    s3 = s3_connection()
    bucket = 'graduation-projectgc'
    if s3_put_object(s3, bucket, file, access_key):
        return {"message": "File uploaded successfully"}
    else:
        return {"message": "File upload failed"}


# curl -X POST -F "file=@/Users/jungheechan/AWS_Flask/output3_5.wav" -F "access_key= api_test" http://0.0.0.0:8001/upload/
# uvicorn main:app --host 0.0.0.0 --port 8001 --reload
# curl -X POST -F "file=@/Users/jungheechan/AWS_Flask/output3_5.wav" -F "access_key=ec2_test3" http://13.125.73.24:8001/upload/


