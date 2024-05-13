import requests
import os

import configparser
from pathlib import Path

cur_dir = Path(os.path.dirname(__file__))
print(os.path.dirname(__file__))  # 当前文件所在的目录)#获得当前工作目录) #获得当前工作目录


config_path = cur_dir / 'config.ini'  # 确保这是正确的文件路径
if not os.path.exists(config_path):
    print(f"配置文件{config_path}不存在")
else:
    config = configparser.ConfigParser()
    try:
        config.read(config_path, encoding='utf-8')  # 指定编码，可根据实际情况调整
        # print("Sections:", config.sections())
    except Exception as e:
        print(f"读取配置文件时发生错误: {e}")

def get_api_key():
    config = configparser.ConfigParser()
    config.read(config_path)
    
    # 检查section和key是否存在，避免KeyError
    if 'LLM' in config and 'api_key' in config['LLM']:
        return config['LLM']['api_key']
    else:
        raise ValueError("API Key not found in the configuration file.")

# 使用函数获取API Key
api_key = get_api_key()
# print(f"Your API Key is: {api_key}")

# 然后你可以使用这个api_key进行后续操作，比如设置环境变量或直接用于API调用
os.environ['API_KEY'] = api_key

url = 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation'
headers = {'Content-Type': 'application/json',
           'Authorization':f'Bearer {api_key}'}
body = {
    'model': 'qwen-turbo',
    "input": {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "介绍一下你自己"
            }
        ]
    },
    "parameters": {
        "result_format": "message"
    }
}

response = requests.post(url, headers=headers, json=body)
print(response.json()["output"]["choices"][0]["message"]["content"])
# print(response.message)