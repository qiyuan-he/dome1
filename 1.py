'''
print("你好")
a=float(input("情输入第一个数："))
b=int(input("请输入第二个数:"))
c=a+b
print("a+b的和为",c)
print(type(a))
print(a>b)


zz = ("你好",1,"22","33","4562")
print(len(zz))

zz = ("你好",1,"22","33","4562")
print(len(zz))


z=(78,"45",32)
a=z.append(2)
print(a)

u = (78,"QQ","微信",1,78,89.33)
#  print(u.count(78))     #统计元组中78的个数
#  print(u.index("QQ"))   #找出元组中""QQ"的下标 xx = u.count(78)
x = u.count(78)
print(x)
y = u.index(1)
print(y)


d = [1,"124",1,44,78.35]
h = (1,2.3)

y = d.count(1)
print(y)
d.insert(0,33)    #指定位置插入，0表示下标，33表示要插入的值
print(d)
d.append(88)      #在数值最后添加数值
print(d)

c = d.copy()      #复制数组
print(c)

d.extend(h)       #合并数组
print(d)

d.pop(1)          #取出数组中的值，1表示下标
print(d)

d.reverse()       #颠倒顺序
print(d)


# d.remove("124")
print(d.remove("124"))

# d.pop(2)
# print(d.pop(2))



u = {"name":"李四"，"age":18,"hobby":"打球")
u("name")=1
print(u)

w = input("请输入：")
zz =("要是能重来，我要做{a},{a}".format(a=w))
print(zz)

ck = int(input("请输入你的存款金额:，万"))

if ck > 100:
    print("买宝马")
elif ck > 20:
    print("买本田")
else:
    print("买玩具车把")         


x = input("请输入年份：")
y = input("请输入月份：")
z = input("请输入日期：")
print("今天是{a}年{b}月{c}日。".format(a=x,b=y,c=z))


xx = {"name":"1","age":18,"hobby":"2"}
xx ["name"]="张三"
print(xx)
xx ["hobby"]="打球"
print(xx)
xx["职业"]="学生"
print(xx)
del xx["age"]
print(xx)

'''

   
ss = {"1":"is",
    2:13.33,
    "键":[1,13.33,
    "22","wangwu"]
    }
tt = ss["键"][1]
print(tt)


