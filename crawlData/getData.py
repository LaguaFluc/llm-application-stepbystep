# 导入所需库
import requests
from bs4 import BeautifulSoup

def fetch_website_title(url):
    '''
    抓取指定URL网页的标题。
    
    参数:
    url (str): 需要爬取的网页地址。
    
    返回:
    str: 网页的标题，如果发生错误则返回None。
    '''
    try:
        # 发送GET请求
        response = requests.get(url)
        
        # 检查请求是否成功（状态码为200表示成功）
        if response.status_code == 200:
            # 使用BeautifulSoup解析HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 提取<title>标签中的内容，即网页标题
            title = soup.find('title').text
            
            return title
        else:
            print(f'请求失败，状态码：{response.status_code}')
            return None
    except Exception as e:
        print(f'发生错误：{e}')
        return None

# 示例用法
url = 'https://www.example.com'
print(fetch_website_title(url))


<div class="n_page_con">
					
					<div class="ueditor_font" id="new_content">
						<p style="text-align: justify; text-indent: 2em;"><span style="font-size: 16px;">为帮助上海“专精特新”企业、独角兽企业、老字号企业、品牌企业等提升品牌、拓展市场，遴选企业的精品、新品、名品，为工会会员提供优质的产品、放心的服务，以高质量发展助推高品质生活，上海市中小企业发展服务中心于2024年3月开展2024年“共享计划”供应商遴选工作。</span></p><p style="text-align: justify; text-indent: 2em;"><span style="font-size: 16px;"><br></span></p><p style="text-align: justify; text-indent: 2em;"><span style="font-size: 16px;">通过公开报名、初审及供应商评审会议，确定2024年“共享计划”供应商遴选入围名单，现予以公示。公示期为2024年5月13日至5月17日（5个工作日），详细名单见附件。</span></p><p style="text-align: justify; text-indent: 2em;"><span style="font-size: 16px;"><br></span></p><p style="text-align: justify; text-indent: 2em;"><span style="font-size: 16px;">公示期间，如对入围供应商有异议，请将有关意见发至邮箱420989757@qq.com。反映情况的材料要客观真实，须署实名并提供联系方式。</span></p><p style="text-align: justify; text-indent: 2em;"><span style="font-size: 16px;"><br></span></p><p style="text-align: justify; text-indent: 2em;"><span style="font-size: 16px;">联系人：张桃君&nbsp;&nbsp;19121752136</span></p><p style="text-align: justify; text-indent: 2em;"><span style="font-size: 16px;">&nbsp;</span></p><p style="text-align: justify; text-indent: 2em;"><span style="font-size: 16px;">特别提示：基于供应商提供材料审核遴选形成该入围名单。公示通过后将形成入选名单，并在“上海市企业服务云”网站公布。</span></p><p style="text-align: justify; text-indent: 2em;"><span style="font-size: 16px;">&nbsp;</span></p><p style="text-align: justify; text-indent: 2em;"><span style="font-size: 16px;">附件：2024年“共享计划”供应商遴选入围名单</span></p><p style="text-align: justify;"><span style="font-size: 16px;">&nbsp;</span></p><p style="text-align: right;"><span style="font-size: 16px;">上海市中小企业发展服务中心</span></p><p style="text-align: right;"><span style="font-size: 16px;">2024年5月13日</span></p>
					</div>
					</div>