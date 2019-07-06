import SecKillCommonTool as sec_kill_tool
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import datetime
import threading


#时钟间隔
ti=0.001
#秒杀时间
buytime="2019-03-15 00:10:59"

miAccount = 'https://account.xiaomi.com'
handUrl = 'https://item.mi.com/product/9995.html'
carUrl='https://item.mi.com/product/8881.html'

#配置账号密码
name="1299671119"
pwd="1"

try_count =3 

def star_for_mi():
    browser= webdriver.Firefox()
    login(browser)
    success = False
    count = 0
    set_hand_suit(browser)
    time.sleep(2)
    print('已选好配置，等待加入购物车')
    while True :
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') >= buytime :
            count += 1
            #超过尝试次数
            if count >= try_count :
                print(try_count, '次了')
                break 
            if sec_kill_tool.add_car(browser) == True:
                confirm_car = False
                create_order = False
                while True:
                    if sec_kill_tool.pay(browser) == True :
                        print('确认购物车')
                        confirm_car = True
                    if confirm_car == True & sec_kill_tool.pay_in_car(browser) == True:
                        print('结算购物车')
                        create_order = True
                    if create_order == True & sec_kill_tool.check_order(browser) == True:
                        success = True
                        break
            else :
                try:
                    login_btn =browser.find_element_by_xpath("//ul[@id='J_buyBtnBox']/li[1]") 
                    login_btn.click()
                    print('出现登录按钮', count)
                except Exception as e:
                    print('没有购物车和登录按钮', count)
        if success == True :
            print('购买成功')
            break
        time.sleep(ti)

"""
选择米9配置
"""
def set_hand_suit(browser):
    browser.get(handUrl)


def login(browser):
    browser.get(miAccount)#登录网址    
    print('正在打开登录网址')
    time.sleep(2)
    browser.find_element_by_id("username").send_keys(name) #利用账号标签的ID，确定位置并send信息
    browser.find_element_by_id("pwd").send_keys(pwd) #利用密码标签的ID，确定位置并send信息
    browser.find_element_by_id("login-button").click()#利用登录按钮的ID，确定位置并点击
    print('点击登录')

#使用线程
if __name__ == '__main__':
    for i in range(1):
       t1=threading.Thread(target=star_for_mi)
       t1.start()
