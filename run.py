import requests
from fastapi import FastAPI

app = FastAPI()

# 파일 업로드 크기 제한 해제
app.config = {"max_request_body_size": None}

url = "http://13.125.245.102/upload/"

### 1. main.py Upload 실행 ###
files = {
    "file": ("/Users/jungheechan/AWS_Flask/output3_5.wav", open("/Users/jungheechan/AWS_Flask/output3_5.wav", "rb")),
    "access_key": (None, "ec2_test"),
}
response = requests.post(url, files=files)
print(response.text)
# response text = File uploaded successfully" 이면 성공
# else 실패: upload fail or S3 접근 실패

### 2. Spleeter.py : MR과 AR 분리 후 Upload 실행 ###
### 3. Train.py: RVC 모델에서 학습시키기 실행 ###
