from selenium import webdriver
from bs4 import BeautifulSoup
import requests

# 发送HTTP请求，获取网页内容
url = "https://www.ssme.sh.gov.cn/public/news!loadNewsDetail.do?id=2c9e88328f5c8bff018f715101bc0171"
driver = webdriver.Chrome()
driver.get(url)
html_content = driver.page_source

# 使用BeautifulSoup解析网页内容，并提取目标文本和附件链接
soup = BeautifulSoup(html_content, "html.parser")
text_div_element = soup.find("div", class_="n_page_con")
accessory_anchor = soup.select_one("div.acessory a.dl")

if text_div_element:
    text_content = text_div_element.get_text()
    print(text_content)
else:
    print("未找到指定的文本内容")

if accessory_anchor:
    onclick_js = accessory_anchor["onclick"]
    attachment_name = accessory_anchor.get_text().strip()

    # 记录当前窗口句柄
    original_window_handle = driver.current_window_handle

    # 执行JavaScript函数获取实际附件链接
    driver.execute_script(onclick_js)

    # 切换窗口至下载页面
    for handle in driver.window_handles:
        if handle != original_window_handle:
            driver.switch_to.window(handle)
            break

    # 下载附件并保存
    attachment_link = driver.current_url
    response = requests.get(attachment_link)

    import docx
    docx_cotent = docx.Document()
    docx_cotent.add_paragraph(response.content.decode('utf-8'))
    docx_cotent.save(f"{attachment_name}")
    # with open(attachment_name, "rb") as f:
    #     f.write(response.content)
    print(f"附件已保存为：{attachment_name}")

    # 关闭下载页面
    driver.quit()
else:
    print("未找到附件")


