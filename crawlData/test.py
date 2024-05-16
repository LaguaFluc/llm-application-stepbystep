from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 初始化WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 打开目标网页
driver.get("https://shpolicy.ssme.sh.gov.cn/knowledge/#/home")

# 等待页面加载，这里设置了最长等待时间为30秒
time.sleep(10)
timeout = 10
try:
    # 找到包含特定信息的列表项
    # 这里我们使用CSS选择器来定位列表项
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".ant-list-item-meta-title > a > span"))
    )
    list_items = driver.find_elements(By.CSS_SELECTOR, ".ant-list-item")
    
    for item in list_items:
        # 在每个列表项中查找标题
        # title = item.find_element(By.CSS_SELECTOR, ".ant-list-item-meta-title > a > span")
        # print(title.text)
        # 使用find_elements定位所有的span元素
        # 注意：find_elements返回的是一个元素列表，因此我们需要遍历这个列表
        span_elements = list_items.find_elements(By.CSS_SELECTOR, "span")
        
        # 初始化一个空字符串用于存储所有span元素的文本
        full_text = ""
        
        # 遍历所有找到的span元素，并将它们的文本拼接起来
        for span in span_elements:
            full_text += span.text + " "  # 每个span文本后加一个空格分隔
        
        # 打印结果
        print(full_text.strip())  # 使用strip()移除字符串两端的空白字符
    
        # # 检查标题是否包含我们感兴趣的信息
        # if "2024年全国节能宣传周工业和信息化领域活动一览（5月14日）" in title.text:
        #     # 获取标题和描述信息
        #     title_text = title.text
        #     description = item.find_element(By.CSS_SELECTOR, ".ant-list-item-meta-description").text
            
        #     # 打印获取的信息
        #     print(f"Title: {title_text}")
        #     print(f"Description: {description}")
        #     print("-" * 50)
    
finally:
    # 关闭浏览器
    driver.quit()

