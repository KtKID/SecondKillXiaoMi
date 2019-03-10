from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
import time
import datetime
import threading

#时钟间隔
ti=0.001
#秒杀时间
buytime="2018-09-05 23:59:00"

miAccount = 'https://account.xiaomi.com'
mi9Url = 'https://item.mi.com/product/10000134.html'
carUrl='https://item.mi.com/product/7832.html'

#配置账号密码
name="1299671119"
pwd="xgt8230280"

#创建8个浏览器
browser= webdriver.Firefox()
#browser2= webdriver.firefox()
#browser3= webdriver.firefox()
#browser4= webdriver.firefox()
#browser5= webdriver.firefox()
#browser6= webdriver.firefox()
#browser7= webdriver.Firefox()
#browser8= webdriver.Firefox()

def star_for_mi9():
    #set_suit()
    add_car()

"""
选择米9配置
"""
def set_suit():
    browser.get(mi9Url) 
    memory = browser.find_element_by_xpath("//li[@data-name='8GB+128GB']")
    memory.click()
    color = browser.find_element_by_xpath("//li[@data-value='全息幻彩蓝']")
    color.click()
    suit = browser.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[2]/div[2]/div[7]/div[3]/ul/li[1]") 
    suit.click()
    print(suit)

def add_car():
    browser.get(carUrl)
    car = browser.find_element_by_xpath("//ul[@id='J_buyBtnBox']/li/a[@data-name='加入购物车']")
    car.click()
    print(car) 

#创建8个方法
def bro1():

    browser.get(miAccount)#登录网址    
    time.sleep(2)
    browser.find_element_by_id("username").send_keys(name) #利用账号标签的ID，确定位置并send信息
    browser.find_element_by_id("pwd").send_keys(pwd) #利用密码标签的ID，确定位置并send信息
    #browser.find_element_by_id("login-button").click()#利用登录按钮的ID，确定位置并点击
    #如果找不到标签ID，可以使用其他方法来确定元素位置
    time.sleep(3)
    if browser.find_element_by_id("login-button"):
        browser.find_element_by_id("login-button").click()
        go_mi9()
    return
    while True: #不断刷新时钟
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') >= buytime:
            while True:
                if browser.find_element_by_xpath('').click():
                # browser.find_element_by_xpath('/html/body').click() #取消提醒
                #except NoSuchElementException:
                #    print("元素异常")
                    print('下单成功，请抓紧付款！1')

        time.sleep(ti)#注意刷新间隔时间要尽量短
def bro2():

    browser2.get( 'https://account.xiaomi.com')#登录网址    
    time.sleep(2)
    browser2.find_element_by_id("username").send_keys(name) #利用账号标签的ID，确定位置并send信息
    browser2.find_element_by_id("pwd").send_keys(pwd) #利用密码标签的ID，确定位置并send信息
    browser2.find_element_by_id("login-button").click()#利用登录按钮的ID，确定位置并点击
    #如果找不到标签ID，可以使用其他方法来确定元素位置
    time.sleep(3)

    browser2.get("https://www.mi.com/seckill/")

    while True: #不断刷新时钟
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') >= buytime:
            while True:
                try :
                    browser2.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/ul[1]/li[1]/div[2]/a[2]').click() #购买按钮的Xpath
                # browser.find_element_by_xpath('/html/body').click() #取消提醒
                except NoSuchElementException:
                    print("元素异常")
                print('下单成功，请抓紧付款！2')

        time.sleep(ti)#注意刷新间隔时间要尽量短

def go_mi9():
    browser.get(mi9Url)
    if browser.find_element_by_class_name("name"):
        print('8GB')

#使用线程
t1=threading.Thread(target=star_for_mi9)
t2=threading.Thread(target=bro2)

t1.start()
#t2.start()
#t3.start()
#t4.start()
#t5.start()
#t6.start()
#t7.start()
#t8.start()
