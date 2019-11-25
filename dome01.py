#  #python常用命定


# #  print()      print表示打印输出

# print("hello, world")   

# # input()         input输入,input输入的都是字符串

# input("请输入：")  

# #  len()   统计字符串、元组、数组和字典个数



  

# #   python数据格式



# #  字符串（str）
# print("你好")             # "你好"就是数据格式，只要加了引号都是字符串

# #   整数（int）           
# print(3)                   #  3就是整数，整数就是数字类型的

# #   小数（float）
# print(19.99)               #  19.99j就是小数

# #   布尔值 (bool)           #  用于判断和循环中，只有True和False
# print(True)
# print(False)

# #空值
# None

# #   变量  赋值

# a = 3   #  等号左边赋值给等号右边
# print(a)

# yy = input("请输入：")
# print("这是我赋值的内容：",yy)

# #  数据转换

# aa = input("请输入第一个数:")
# bb = input("请输入第二个数:")
# cc = aa + bb
# print("aa+bb的和为：",cc)                   #字符串加字符串和为拼接

# aa = int(input("请输入第一个数:"))          #字符串转为数字，前提是必须的长得像数字，否则不能转换
# bb = float(input("请输入第二个数:"))
# cc = aa + bb
# print("aa+bb的和为：",cc)                   

# #  type（）获取数据类型
# sss = ("111")
# print(type(sss))

# #布尔值的产生

# a = 10
# b = 6
# print(a > b)

# # len()的使用
# p = len("qsqsdsjdhsjbsscsbjssdbjdbsjdbhbwdgwqubdshd")
# print(p)

# gg = len(input("请输入您要计算的字符串:"))
# print("您输入字符的个数为:",gg,"个")



# # 元组(tuple)  用（）定义，元组里面可以放多个值  元组里面的值一旦确定，不能更改


# zz = (1,"苏喂苏喂","222",88,45.33,88,88,88,88)
# print(zz[3])         #  元组下标是默认从0开始的，要去出元组中的值在“[]”填写对应的下标就可以取出

# # count  统计元组中某个值的个数  
# print("元组中统计结果为：",zz.count(88),"个")

# # index  数出具体某个值的下标
# print("下标为:",zz.index(88))       # 若元组中有多个相同的值，index数出下标为第一个下标


#  数组/列表 （list） 用[]定义， 元组里面可以放多个值  数组里面的值可以更改

# vv = ["哈哈","嘿嘿",1,88,33,33,26.22,(23,56)]
# # a = vv.index(33)
# # print(a)
# # print(vv.count(33))
# # print(vv[2])

# # #  appdend  在数组最后插入一个值
# # vv.append("这是新插入的值")
# # print(vv)

# # #  insert 选择位置插入 insert(下标位置,需要插入的值) 
# # vv.insert(2,"insert插入的值")
# # print(vv)

# # # clear  清除数组的值
# # vv.clear()
# # print(vv)

# # # copy  拷贝数组
# # vv.copy()                      # 也可以 yy = vv ,然后在print（yy） 
# # print(vv)

# #  extend 合并数组
# # vv.extend((1,23))
# # print(vv)

# # vv.extend("想想吓唬吓唬")         # 将字符串拆开合并到数组中     字符串具有和数组一样的属性
# # print(vv)

# # yy = "HSDVSJKHBCASDJHASDJCH"      #  字符串具有和数组一样的属性
# # print(list(yy))


# # pop    将数组里面的某一个值拿出来，用下标方式

# # vv.pop(0)                           #  拿出了当前列表中下标为0的数，即拿出了“哈哈”
# # print(vv.pop(0))                    #  拿出之后的数组为"[嘿嘿",1,88,33,33.55,(1,5,"嘻嘻"),33],所以第一个值为“嘿嘿”

# # sort 按照从小到大排序，数组中只能有整数
# # vv.sort()
# # print(vv)

# # # reverse  颠倒
# # vv.reverse()
# # print(vv)

# # #  remove 删除列表中的值
# # vv.remove(88)                 # 如果有多个相同的值，只会删除第一个
# # print(vv)

# # #  del    删除
# del vv[0]
# print(vv)

'''

# 字典（dict）  用{}来定义，通过键值对来控制的     cc = {key:value}

mm = {"name":"张三","age":18,"hobby":"打球"}
print(mm["name"])
print(mm["age"])             # 通过键来打印输出值

# #  clear 清除字典中所有的内容
# mm.clear()                   
# print(mm)

# copy   拷贝字典

mm.copy()
print(mm)

# get 模糊取值    

a = mm.get("hobby")
print(a)

#  字典中新增值
mm["爱好"] = "打球"
print(mm)

mm["age"] = 22      #  如果加入字典中有的key值，就是修改
print(mm)

mm["籍贯"] = "湖南"  #  如果加入字典中没有的key值，就是新增
print(mm)    

#  删除
del mm["hobby"]     
print(mm)

'''

'''
# 二元数据类型
xx = [1,2,22,2,(1,6)]
v=xx[4]            #    取出列表中下标为4的值
print(v)

print(xx[4][1])     #   获取列表中元组的某个值

print(xx[0:4])      #   批量取值，必须是连续的，取值区间左闭右开

print(xx[-1])       #   取出最后一个值

print(xx[-3:-1])      #   取值区间必须从小到大

print(xx[-2:])        #    从-2开始一直结尾

print(xx[:3])         #    从默认开始一直到3结尾，都是不包括3


print(len(xx))


#  字符串转为列表

u = "njsdcsacn;saklnvsadnvlskdnv"
q = list(u)
print(q)

'''

# # 字符串初始化

# name = input("请输入你的名字：")
# age =  input("请输入你的年龄：")
# hobby = input("请输入你的爱好：")

# print("大家好，我叫{a},我今年{b}岁了，我的爱好是{c},{c}真得很有趣".format(a=name,b=age,c=hobby))



# 判断    == 等于  < 大于   >  小于   is 是不是   not is   不是   in  在不在   not in  不在


#  if 循环
'''
  if 条件:
    print()
  else:
    print()
'''

# shouru = int(input("请输入你的月收入："))

# if shouru >= 10000:
#     print("月收入{}元，你可以买房子了".format(shouru))
# elif shouru > 8000:                                        # elif 多条件判断
#     print("月收入{},努努力，房子离你不远了".format(shouru))
# elif shouru > 5000:
#     print("月收入才{},还想买房".format(shouru))        
# else:    
#     print("月收入才{}元，赶紧攒钱吧".format(shouru))

'''

i = input("请输入：")

if type(i) is int:                       #  is一般用于判断数据类型
    print("i的类型为int")
elif type(i) is str:
    print("i的类型为str")
else:
    print("其他")

'''

# a = input("请输入：")
# b = ["1",2,2.3,True]

# if a in b:
#     print("a在b中")
# else:
#     print("a不在b中")


#   for 循环

m = input("请输入：")
d = [1,"1"]
for i in d:

  if m in d:
    print("m在d中")
    
  else:
    print("m不在d中")













