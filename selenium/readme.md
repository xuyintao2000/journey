Python爬虫：使用Selenium

# 安装
1. 安装firefox [2018-03-27 / 版本号：59.0.2]

2. 安装python版本的Selenium [2018-03-27 / 版本号：3.11.0]

<code>pip install selenium</code>
<p>或者</p>
<code>python -m pip install selenium</code> 

3. 下载Selenium driver [2018-03-27 / 版本号：v0.20.0]

Firefox:	https://github.com/mozilla/geckodriver/releases
Chrome:	https://sites.google.com/a/chromium.org/chromedriver/downloads
Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/

* 下载地址被墙，你需要翻墙。
[firefox、Selenium driver]
[链接]https://pan.baidu.com/s/1uKgg_nuKWx7rnQ0yKugFPg 
[密码]6v66

[Selenium Python参考文档] http://selenium-python.readthedocs.io/


#代码
<code>
from selenium import webdriver
from bs4 import BeautifulSoup

\# 指定驱动所在位置
driver = webdriver.Firefox(executable_path='C:\geckodriver\geckodriver')
\# firefox 36 mac/win  (先安装一个新版本的firefox，用来调试分析网页，然后再安装firefox36，供程序调用操作)
driver.get(
    'https://account.xiaomi.com/pass/serviceLogin?callback=http%3A%2F%2Fbbs.xiaomi.cn%2Flogin%2Fcallback%3Ffollowup%3Dhttp%253A%252F%252Fbbs.xiaomi.cn%252F%26sign%3DM2E4MTg3MzE3MGJmZGFiMTc0MTE5NmNjZTAyYWNmMDZhNTEwOTU2NQ%2C%2C&sid=new_bbs_xiaomi_cn&_locale=zh_CN')

driver.find_element_by_xpath(".//*[@id='username']").clear()
driver.find_element_by_xpath(".//*[@id='username']").send_keys("1078457227")

driver.find_element_by_xpath(".//*[@id='pwd']").clear()
driver.find_element_by_xpath(".//*[@id='pwd']").send_keys("dadeng123")

driver.find_element_by_xpath(".//*[@id='login-button']").click()

basr_url = 'http://bbs.xiaomi.cn/d-{page}'
for i in range(1, 2):
    url = basr_url.format(page=i)
    driver.get(url)
    bsObj = BeautifulSoup(driver.page_source, 'html.parser')
    Titles = bsObj.find_all('div', {'class': 'title'})
    for title in Titles:
        title_content = title.get_text().strip('\n')
        print(title_content)
</code>