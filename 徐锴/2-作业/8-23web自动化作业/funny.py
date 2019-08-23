# -*- coding: UTF-8 -*-
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from collections import OrderedDict
import requests
import sys
import io


def loginin():
    global driver
    driverfile_path = r'D:\Users\Administrator\AppData\Local\Programs\Python\chrome\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driverfile_path)
    driver.implicitly_wait(10)
    driver.get(r'http://119.3.163.10/forum.php')
    driver.find_element_by_id('ls_username').send_keys('zy06637')
    driver.find_element_by_id('ls_password').send_keys('123456')
    driver.find_element_by_xpath('//*[@id="lsform"]/div/div/table/tbody/tr[2]/td[3]/button').click()
    sleep(5)
    driver.refresh()


def search(content):
    driver.find_element_by_id('scbar_txt').send_keys(content)
    driver.find_element_by_id('scbar_btn').click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    assert "对不起，没有找到匹配结果" not in driver.page_source


def personal():
    driver.find_element_by_xpath("//*[@id='um']/p[1]/strong/a").click()
    sleep(5)




def image():
    driver.find_element_by_xpath("//*[@id='um']/p[1]/a[2]").click()
    sleep(5)
    driver.find_element_by_xpath("//*[@id='ct']/div[2]/div/ul/li[1]/a").click()
    sleep(5)


'''
def modify(name, emotion = '情感状态等待交配', target = '交友目的需要繁殖'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
    username = {'fastloginfield':'username',
            'username':'zy06637',
            'password':'123456',
            'quickforward':'yes',
            'handlekey':'ls'}

    cookie_str = r'dTno_2132_sid=I52xez; dTno_2132_saltkey=I6A7F2jj; dTno_2132_lastvisit=1566548983; dTno_2132_ulastactivity=7e0cCPzfLhW7B7OFairaXGkHv2tNXvB6oH1Qf%2BYEZvMrgATg3qbl; dTno_2132_auth=f1004NCOKZpmmdTN%2F8umMutPbkmuZPZy3iIMnKUCIU6iaozR96kDzafcAjWnHbR6%2BKyxakIY93VGZznDtyH6xQ; dTno_2132_lastcheckfeed=13%7C1566552893; dTno_2132_lip=113.110.201.37%2C1566552869; dTno_2132_sendmail=1; dTno_2132_lastact=1566552893%09misc.php%09patch'
    cookies = {}
    for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    resp = requests.get(r'http://119.3.163.10/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1', headers = headers, cookies = cookies)
    print(resp.content.decode('utf-8'))


    params = {"formhash": (None,'abbb35ab'),
              "realname": (None, name),
              "privacy[realname]": (None, '0'),
              "gender": (None, '1'),
              "privacy[gender]": (None, '0'),
              "birthyear": (None, '2000'),
              "birthmonth": (None, '5'),
              "birthday": (None, '5'),
              "privacy[birthday]": (None, '0'),
              "birthprovince": (None, '北京市'),
              "birthcity": (None, '延庆县'),
              "birthdist": (None, '香营乡'),
              "privacy[birthcity]": (None, '0'),
              "resideprovince": (None, '北京市'),
              "residecity": (None, '延庆县'),
              "residedist": (None, '香营乡'),
              "privacy[residecity]": (None, '0'),
              "affectivestatus": (None, emotion),
              "privacy[affectivestatus]": (None, '0'),
              "lookingfor": (None, target),
              "privacy[lookingfor]": (None, '0'),
              "bloodtype": (None, 'A'),
              "privacy[bloodtype]": (None, '0'),
              "profilesubmit": (None, 'true'),
              "profilesubmitbtn": (None, 'true')}

    res = requests.post(r'http://119.3.163.10/home.php?mod=spacecp&ac=profile&op=base', headers = headers, cookies = cookies, data=params)

    print(res.content.decode('utf-8'))

    print(params)
'''



def modify(name='辣鸡', gender='保密', year='1992', month='01', day='17', emotion='需要港湾', target='繁衍下一代', blood='其它'):
    driver.find_element_by_xpath("//*[@id='um']/p[1]/a[2]").click()
    sleep(5)
    driver.find_element_by_id('realname').send_keys(Keys.CONTROL, 'a')
    driver.find_element_by_id('realname').send_keys(name)
    if gender == '男':
        driver.find_element_by_xpath("//*[@id='gender']/option[2]").click()
    elif gender == '女':
        driver.find_element_by_xpath("//*[@id='gender']/option[3]").click()
    else:
        driver.find_element_by_xpath("//*[@id='gender']/option[1]").click()
    year = int(year)
    y = 2019-year+2
    driver.find_element_by_xpath("//*[@id='birthyear']/option[%d]"%(y)).click()
    month = int(month)
    m = month+1
    driver.find_element_by_xpath("//*[@id='birthmonth']/option[%d]"%(m)).click()
    day = int(day)
    d = day+1
    driver.find_element_by_xpath("//*[@id='birthday']/option[%d]" % (d)).click()
    driver.find_element_by_id('affectivestatus').send_keys(Keys.CONTROL, 'a')
    driver.find_element_by_id('affectivestatus').send_keys(emotion)
    driver.find_element_by_id('lookingfor').send_keys(Keys.CONTROL, 'a')
    driver.find_element_by_id('lookingfor').send_keys(target)
    if blood == 'A':
        driver.find_element_by_xpath("//*[@id='bloodtype']/option[1]").click()
    elif blood == 'B':
        driver.find_element_by_xpath("//*[@id='bloodtype']/option[2]").click()
    elif blood == 'AB':
        driver.find_element_by_xpath("//*[@id='bloodtype']/option[3]").click()
    elif blood == 'O':
        driver.find_element_by_xpath("//*[@id='bloodtype']/option[4]").click()
    else:
        driver.find_element_by_xpath("//*[@id='bloodtype']/option[5]").click()

    driver.find_element_by_xpath("//*[@id='profilesubmitbtn']/strong").click()



def postamessage():
    driver.find_element_by_xpath("//*[@id='category_1']/table/tbody/tr[1]/td[2]/h2/a").click()
    driver.find_element_by_xpath("//*[@id='newspecial']/img").click()
    tn = time.localtime()
    timer = str(time.asctime(tn))
    driver.find_element_by_id('subject').send_keys(timer)
    tnn = str(time.time())
    driver.switch_to.frame("e_iframe")
    driver.find_element_by_xpath("/html/body").send_keys(timer+tnn)
    driver.switch_to.default_content()
    driver.find_element_by_xpath("//*[@id='postsubmit']/span").click()

def logoutout():
    driver.find_element_by_xpath("//*[@id='um']/p[1]/a[5]").click()
    sleep(5)
    driver.quit()












if __name__ == '__main__':
    loginin()

