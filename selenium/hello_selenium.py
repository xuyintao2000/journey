from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Firefox(executable_path='C:\geckodriver\geckodriver')
# firefox 36 mac/win  (先安装一个新版本的firefox，用来调试分析网页，然后再安装firefox36，供程序调用操作)
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
