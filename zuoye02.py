from selenium import webdriver
from dome0202 import find_element

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://132.232.44.158:9999/shopxo/admin.php?s=/admin/logininfo.html")
driver.maximize_window()

a = ("name","username")
b = ("name","login_pwd")
c = ("xpath","/html/body/div[1]/div/div[2]/div/form/div/div[3]/button")
d = ("xpath",'//*[@id="admin-offcanvas"]/div/ul/li[5]/a')
e = ("xpath",'//*[@id="power-menu-126"]/li/a')
f = ("xpath","/html/body/div[1]/div/div/a[1]")
g = ("xpath","/html/body/div[1]/div/form/div[1]/input")
h = ("name","pwd")
j = ("xpath","/html/body/div[1]/div/form/div[14]/button")
k = ("xpath","/html/body/div[1]/div/table/tbody/tr[1]/td[2]/ul/li[1]")

a1 = find_element(driver,a)         #  账号
b1 = find_element(driver,b)         #  密码              
c1 = find_element(driver,c)         #  登录
a1.send_keys("admin")
b1.send_keys("shopxo")
c1.click()

d1 = find_element(driver,d)
d1.click()

e1 = find_element(driver,e)
e1.click()

aa = driver.find_element_by_xpath('//*[@id="ifcontent"]')
driver.switch_to_frame(aa)

f1 = find_element(driver,f)
f1.click()

g1 = find_element(driver,g)
h1 = find_element(driver,h)
j1 = find_element(driver,j)
g1.send_keys("sz332")
h1.send_keys("123456")
j1.click()

l = "sz332"
k1 = driver.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr/td[2]/ul/li[1]')
print(k1.text)


if l in k1.texe:
    print("测试通过")
else:
    print("测试失败")