import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from lxml import etree,html
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ReadFile:
    def __init__(self):
        pass
    def read_note(self, week):
        with open(f'./notes/{week}.txt','r',encoding='utf-8') as f:
            note = f.read()
        return note
    def read_exp(self, week):
        with open(f'./Experience/{week}.txt','r',encoding='utf-8') as f:
            exp = f.read()
        return exp

class CommitNote:
    def __init__(self):
        self.etree = etree
        self.html = html
        self.login = 'https://ehall.jsei.edu.cn/new/index.html'
        edge_opts = Options()
        # edge_opts.add_argument('--headless')
        # edge_opts.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(service=Service('./chromedriver-win64/chromedriver.exe'),options=edge_opts)
        self.note = ReadFile()
    def commit(self):
        self.driver.get(self.login)
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div[3]/div[1]/form/div[1]/input').send_keys('2022131826')
        time.sleep(3)
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div[3]/div[1]/form/div[2]/input[1]').send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div[3]/div[1]/form/p[2]/button').click()
        time.sleep(6)
        # self.driver.find_element(By.XPATH,'//*[@id="ampTabContentItem0"]/div[2]/pc-card-html-5046847566183801-01/amp-w-frame/div/div[2]/table/tbody/tr[1]/td[4]/a/img').click()
        self.driver.get('https://dgsx.jsei.edu.cn:81/sso/jziotlogin/dgsx')#进入实习界面
        wait = WebDriverWait(self.driver, 10)
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="mainnav-menu"]/li[5]/a').click()#边栏
        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mainnav-menu"]/li[5]/ul/li[1]/a')))
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="mainnav-menu"]/li[5]/ul/li[1]/a').click()
        time.sleep(3)
        iframe = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="iframe_tab_N4035"]')))
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(By.ID,'btn_zj').click()#增加
        time.sleep(5)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="zc_zj_chosen"]/a/span')))
        week = self.html.fromstring(self.driver.page_source).xpath('//*[@id="zc_zj_chosen"]/a/span')
        week = week[0].text#获取第几周，字符串
        note = self.note.read_note(week)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="zrznr"]')))
        self.driver.find_element(By.XPATH,'//*[@id="zrznr"]').send_keys(note)
        time.sleep(3)
        exp = self.note.read_exp(week)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ewzrznr"]')))
        self.driver.find_element(By.XPATH,'//*[@id="ewzrznr"]').send_keys(exp)
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btn_success"]')))
        self.driver.find_element(By.XPATH,'//*[@id="btn_success"]').click()#提交
        self.driver.find_element(By.XPATH,'//*[@id="btn_success"]').click()#提交
        self.driver.quit()

if __name__ == '__main__':
    password = open('./notes/password.txt','r').read()
    CommitNote().commit()