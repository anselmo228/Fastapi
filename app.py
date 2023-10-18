from Train import train1key
from fastapi.responses import JSONResponse
from fastapi import FastAPI, File, Form, UploadFile

from config import Config
import numpy as np
import boto3
from i18n import I18nAuto
from main import s3_connection, s3_put_object

app = FastAPI()
# 파일 업로드 크기 제한 해제
app.config = {"max_request_body_size": None}

# 파일 업로드 엔드포인트
@app.post("/upload/")
async def upload_file(file: UploadFile, access_key: str = Form(...)):
    s3 = s3_connection()
    bucket = 'graduation-projectgc'
    if s3_put_object(s3, bucket, file, access_key):
        return {"message": "File uploaded successfully"}
    else:
        return {"message": "File upload failed"}
    


config = Config()
i18n = I18nAuto()

# -- Process data
trainset_dir4 = "/Users/jungheechan/Desktop/raw" ## api에서 get으로 입력받고 zip 아님 
exp_dir1 = "rvc_exp2" ## api에서 post로 S3 Bucket에 전송해줘야할듯
sr2 = "48k"
np7 = int(np.ceil(config.n_cpu / 1.5))

# -- Feature Extraction
gpus6 = '0'
f0method8 = 'harvest'
if_f0_3 = True
version19 = 'v2'
gpus_rmvpe = '0-0'

# -- One-click training
spk_id5 = 0
save_epoch10 = 20
total_epoch11 = 1
batch_size12 = 4
if_save_latest13 = i18n("否")
pretrained_G14 = 'pretrained_v2/f0G48k.pth'
pretrained_D15 = 'pretrained_v2/f0D48k.pth'
gpus16 = '0'
if_cache_gpu17 = i18n("否")
if_save_every_weights18 = i18n("否")




@app.post("/train/")
async def train(
    exp_dir1: str = Form(...),  #s3 Bucket
    trainset_dir4: str = Form(...),  # 사용자 입력값
):
    sr2
    np7
    gpus6
    f0method8
    if_f0_3
    version19
    gpus_rmvpe
    spk_id5
    save_epoch10
    total_epoch11
    batch_size12
    if_save_latest13
    pretrained_G14
    pretrained_D15
    gpus16
    if_cache_gpu17 
    if_save_every_weights18

    train1key(
    exp_dir1, sr2, if_f0_3, trainset_dir4, spk_id5, np7, f0method8, save_epoch10,
    total_epoch11, batch_size12, if_save_latest13, pretrained_G14, pretrained_D15, gpus16, if_cache_gpu17,
    if_save_every_weights18, version19
    )

    return JSONResponse(content={"message": "API 호출이 성공했습니다."})