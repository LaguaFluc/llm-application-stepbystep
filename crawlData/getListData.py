from selenium import webdriver
from bs4 import BeautifulSoup
import csv

# 设置Chrome浏览器驱动路径
chrome_driver_path = "path_to_chromedriver"

# 设置Chrome选项
options = webdriver.ChromeOptions()
options.binary_location = "path_to_chrome_executable"  # 如果需要指定Chrome可执行文件的路径

# 创建一个Chrome浏览器实例
driver = webdriver.Chrome(options=options)

# 打开目标网页
url = "https://shpolicy.ssme.sh.gov.cn/knowledge/#/home"
driver.get(url)

# 等待一定时间，确保页面加载完成
driver.implicitly_wait(10)

# 获取页面源码
html_content = driver.page_source

# 关闭浏览器
driver.quit()

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(html_content, 'html.parser')

# 在HTML块中找到所有政府文件的链接
list_items = soup.find_all("div", class_="ant-list-item-meta-content")

# 创建一个CSV文件，并写入表头
with open('government_files.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['区域', '标题', '链接'])

    # 遍历每个政府文件块，提取所需信息并写入CSV文件
    for item in list_items:
        region = item.find('i', class_='icon ic_person').find_next_sibling('span').text
        title = item.find('h4', class_='ant-list-item-meta-title').text.strip()
        link = item.find('h4', class_='ant-list-item-meta-title').find('a')['href']

        writer.writerow([region, title, link])

print("已成功生成government_files.csv文件。")
