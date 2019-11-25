
import time

from seleniumtest import webdriver

driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("http://132.232.44.158:9999/shopxo/admin.php?s=/admin/logininfo.html ")

e = driver.find_element_by_name("username")
e.send_keys("admin")
r = driver.find_element_by_name("login_pwd")
r.send_keys("shopxo")

anniu = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/form/div/div[3]/button")
anniu.click()

time.sleep(3)                         # 登录等待3秒

s = driver.find_element_by_xpath('//*[@id="admin-offcanvas"]/div/ul/li[5]/a')   # 点击用户管理
s.click()

q = driver.find_element_by_xpath('//*[@id="power-menu-126"]/li/a')            # 点击用户列表
q.click()

g = driver.find_element_by_xpath('//*[@id="ifcontent"]')                     #  切换到用户列表窗口
driver.switch_to_frame(g)

h = driver.find_element_by_xpath("/html/body/div[1]/div/div/a[1]")            #  点击新增
h.click()

time.sleep(3)

j = driver.find_element_by_name("username")    # 输入用户名
j.send_keys("sz223")

k = driver.find_element_by_name("pwd")        # 输入密码
k.send_keys("123456")

l = driver.find_element_by_xpath("/html/body/div[1]/div/form/div[14]/button")
l.click()


time.sleep(5)
mz = "sz223"
o = driver.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[1]/td[2]/ul/li[1]')

if mz in o.text:
    print("测试通过")
else:
    print("shibai")    