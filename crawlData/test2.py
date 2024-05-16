from selenium import webdriver
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

# 等待页面加载或执行必要的操作来确保元素已经加载到DOM中
timeout = 10
try:
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".ant-list-item-meta-title > a > span"))
    )
    # 定位到包含所有li元素的ul
    ul_element = driver.find_element(By.CSS_SELECTOR, ".ant-list-items")

    # 定位到所有的li元素
    li_elements = ul_element.find_elements(By.CSS_SELECTOR, ".ant-list-item")

    # 遍历每个li元素
    for li in li_elements:
        # 提取<h4 class="ant-list-item-meta-title">中的span内容
        h4_element = li.find_element(By.CSS_SELECTOR, ".ant-list-item-meta-title > a")
        span_elements = h4_element.find_elements(By.CSS_SELECTOR, "span")
        if len(span_elements) >= 2:
            title_span_text = span_elements[0].text + span_elements[1].text
            print(f"Title span text: {title_span_text}")
        else:
            print("The h4 element does not contain the expected two span elements.")
        
        # 提取<div class="ant-list-item-meta-description">中的span内容
        description_element = li.find_element(By.CSS_SELECTOR, ".ant-list-item-meta-description")
        # 假设描述信息中的每个span元素都包裹在ant-col类的一个div中
        ant_col_elements = description_element.find_elements(By.CSS_SELECTOR, ".ant-col")
        
        for col in ant_col_elements:
            # 定位到每个ant-col中的所有span元素
            col_span_elements = col.find_elements(By.TAG_NAME, "span")
            col_span_texts = [span.text for span in col_span_elements]
            # 打印每个ant-col中的span元素文本
            print(f"Description span texts in col: {' '.join(col_span_texts)}")
    
    # 定位到h4标题中的a标签
    li_element = driver.find_element(By.CSS_SELECTOR, ".ant-list-item")
    a_element = li_element.find_element(By.CSS_SELECTOR, ".ant-list-item-meta-title > a")
        
    li_element.click()
    # 等待一段时间，让JavaScript处理点击事件
    driver.implicitly_wait(5)  # 根据需要调整等待时间
    # 获取并打印当前的window.location
    current_url = driver.execute_script("return window.location.href;")
    print(f"The current URL after the click is: {current_url}")
    # # 模拟点击事件
    # a_element.click() 
    # # 等待页面跳转
    # driver.implicitly_wait(10)  # 根据需要调整等待时间
    # # 获取并打印跳转后的URL
    # current_url = driver.current_url
    # print(f"The current URL after the click is: {current_url}")


finally:
    # 如果需要的话，关闭浏览器
    # driver.quit()
    pass