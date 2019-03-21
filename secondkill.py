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
mi9Url = 'https://item.mi.com/product/10000134.html'
miNote7Url = 'https://item.mi.com/product/10000131.html'
carUrl='https://item.mi.com/product/8881.html'

#配置账号密码
name="1299671119"
pwd="1"

try_count = 100

def star_for_mi9():
    browser= webdriver.Firefox()
    login(browser)
    success = False
    count = 0
    #set_mi9_suit(browser)
    browser.get(carUrl)
    time.sleep(2)
    print('已选好mi9配置，等待加入购物车')
    while True :
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') >= buytime :
            count += 1
            #超过尝试次数
            if count >= try_count :
                print(try_count, '次了')
                break 
            if add_car(browser) == True:
                confirm_car = False
                create_order = False
                while True:
                    if pay(browser) == True :
                        print('确认购物车')
                        confirm_car = True
                    if confirm_car == True & pay_in_car(browser) == True:
                        print('结算购物车')
                        create_order = True
                    if create_order == True & check_order(browser) == True:
                        success = True
                        break
            else :
                print('没有购物车按钮', count)
        if success == True :
            print('购买成功')
            break
        time.sleep(ti)

"""
选择米9配置
"""
def set_mi9_suit(browser):
    browser.get(mi9Url) 
    memory = browser.find_element_by_xpath("//li[@data-name='6GB+128GB']")
    memory.click()
    color = browser.find_element_by_xpath("//li[@data-value='全息幻彩蓝']")
    color.click()
    suit = browser.find_element_by_xpath("//div[@id='J_list']/div[3]/ul/li[1]")
    suit.click()

def add_car(browser):
    try :
        car = browser.find_element_by_xpath("//ul[@id='J_buyBtnBox']/li/a[@data-name='加入购物车']")
        car.click()
        print('点击加入购物车')
        return True
    except NoSuchElementException :
        print('找不到购物车按钮') 
        return False

def pay(browser):
    try :
        pay_btn = browser.find_element_by_xpath("//a[contains(@href,'/cart/')]")
        #pay_btn = browser.find_element_by_link_text('去购物车结算')
        pay_btn.click()
        print('准备结算')
        return True
    except NoSuchElementException :
        #browser.back()
        print('找不到结算按钮，返回上一级页面')
        return False

def pay_in_car(browser):
    try :
        pay_btn = browser.find_element_by_id("J_goCheckout")
        pay_btn.click()
        print('在购物车结算')
        return True
    except NoSuchElementException :
        print('找不到购物车结算按钮')
        return False

def check_order(browser):
    try :
        addr_btn = browser.find_element_by_xpath("//div[@id='J_addressList']/div[1]")
        addr_btn.click()
        pay_btn = browser.find_element_by_id("J_checkoutToPay")
        pay_btn.click()
        print('订单结算')
        return True
    except NoSuchElementException :
        print('找不到订单结算按钮')
        return False

#创建8个方法
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
    #for i in range(2):
    #    t1=threading.Thread(target=star_for_mi9)
    #    t1.start()
    t1=threading.Thread(target=star_for_mi9)
    t2=threading.Thread(target=star_for_mi9)
    t1.start()
    #t2.start()

