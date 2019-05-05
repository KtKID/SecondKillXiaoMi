#添加到购物车
def add_car(browser):
    try :
        car = browser.find_element_by_xpath("//ul[@id='J_buyBtnBox']/li/a[@data-name='加入购物车']")
        car.click()
        print('点击加入购物车')
        return True
    except NoSuchElementException :
        print('找不到购物车按钮') 
        return False

#成功加入购物车 跳转去购物车
def pay(browser):
    try :
        pay_btn = browser.find_element_by_xpath("//a[contains(@href,'/cart/')]")
        pay_btn.click()
        print('准备结算')
        return True
    except NoSuchElementException :
        #browser.back()
        print('找不到结算按钮，返回上一级页面')
        return False

# 在购物车结算
def pay_in_car(browser):
    try :
        pay_btn = browser.find_element_by_id("J_goCheckout")
        pay_btn.click()
        print('在购物车结算')
        return True
    except NoSuchElementException :
        print('找不到购物车结算按钮')
        return False

# 选择第一个地址并结算
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
