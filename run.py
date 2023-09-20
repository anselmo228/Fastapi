import requests
from fastapi import FastAPI

app = FastAPI()

# 파일 업로드 크기 제한 해제
app.config = {"max_request_body_size": None}

url = "http://13.125.245.102/upload/"

files = {
    "file": ("/Users/jungheechan/AWS_Flask/output3_5.wav", open("/Users/jungheechan/AWS_Flask/output3_5.wav", "rb")),
    "access_key": (None, "ec2_test"),
}

response = requests.post(url, files=files)

print(response.text)

