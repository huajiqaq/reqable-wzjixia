# 王者稷下学院图片替换脚本 v0.1
# date: 2025/09/04
# author: huajiqaq
# qq group: 746855036
# github: https://github.com/huajiqaq/reqable-wzjixia
# 使用时请将脚本生效url改为 https://download.nature.qq.com/SnsShare/SocialProfile/*
# 使用请确保已经安装了python 以及 cos sdk 安装教程 https://cloud.tencent.com/document/product/436/12269
# 使用请替换 IMG_PATH 变量为你的本地图片路径

from reqable import *
from qcloud_cos import CosConfig, CosS3Client

# 配置
SECRET_ID = 'AKIDNZbQ2Sfy5D9rM073nLhstiQzMWUHyUpI'
SECRET_KEY = 'OaYL1Yu3qY3JAyd6OceRzMbcrukNcdR5'
REGION = 'ap-nanjing'
BUCKET = 'sgame-data-service-1252931805'
TARGET_DOMAIN = 'download.nature.qq.com'
IMG_PATH = r"你的本地图片路径"  # 例如：C:/your_image.jpg 或 /Users/xxx/image.png

# 注意 这里 Scheme 必须为 http 否则可能会报ssl错误
config = CosConfig(Region=REGION, SecretId=SECRET_ID, SecretKey=SECRET_KEY, Scheme='http')
client = CosS3Client(config)

def onRequest(context, request):
    url = context.url
    if request.method == 'GET' and TARGET_DOMAIN in url and 'SnsShare/SocialProfile' in url:
        try:
            key = url.split(TARGET_DOMAIN + '/', 1)[1].split('?', 1)[0]
            client.upload_file(
                Bucket=BUCKET,
                Key=key,
                LocalFilePath=IMG_PATH,
                PartSize=1024,        # 每块 1024MB 超过1024MB可能会403
                EnableMD5=False
            )
            print(f'[+] Uploaded: {key}')
        except Exception as e:
            print(f'[!] Upload failed: {e}')
    return request

def onResponse(context, response):
    return response