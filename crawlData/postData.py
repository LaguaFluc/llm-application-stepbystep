import requests
import json
import csv

import re
import html

def html_to_text(html_content):
    """
    将HTML内容转换为纯文本。
    :param html_content: 包含HTML标签的原始字符串。
    :return: 去除HTML标签后的纯文本字符串。
    """
    # 取消转义HTML字符
    text = html.unescape(html_content)
    
    # 使用正则表达式移除HTML标签
    clean_text = re.sub(r'<[^>]+>', '', text)
    
    return clean_text



# POST请求的URL和请求体
url = "https://shpolicy.ssme.sh.gov.cn/governmentCloudApi/chatSNet/policyDoc"
payload = {
    "pageNum": 1,
    "pageSize": 10,
    "newsCategory": "政策法规",
    "area": "上海市",
    "name": None,
    "department": None
}

# 发送POST请求
response = requests.post(url, json=payload)

# 检查请求是否成功
if response.status_code == 200:
    # 将响应内容解析为JSON
    data = response.json()
    
    # 要保存的字段列表
    fields = [
        "newsCategory", "publishTime", "content", "area", "attachments", "department", "id", "name",
        "departmentFilter", "areaFilter", "createdTime"
    ]
    
    # 打开一个新的CSV文件用于写入# 打开一个新的CSV文件用于写入
    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        
        # 写入表头
        writer.writeheader()
        
        # 遍历dataList中的每个元素
        for item in data["data"]["respData"]["dataList"]:
            # 将content字段中的HTML标签转换为纯文本
            item['content'] = html_to_text(item.get('content', ''))
            
            # 附件字段是一个列表，我们需要将其转换为字符串
            attachments = json.dumps(item.get("attachments", [])) if item.get("attachments") else ""
            
            # 收集fields中指定的字段
            row = {field: (item.get(field, "") if field != "attachments" else attachments) for field in fields}
            
            # 写入CSV文件
            writer.writerow(row)

    print("CSV文件已保存。")
else:
    print("请求失败，状态码：", response.status_code)