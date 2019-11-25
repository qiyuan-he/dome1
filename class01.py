# 类


#普通变量


a = [1,2,3]
b = 1
c = True


#普通方法
def ccc():
    print("12312312")



# 类包含属性(特征)和方法（方法，能干啥）
# 类名字大写
class Person():
    
    # 成员变量 ，无论什么地方都可以用
    mz = "张三"
    nl = 18
    sg = 175
    xb = "男"

    # 成员方法：以self参数开头的方法
    def chang(self):                                                           
        print("大家好，我是联系2年半的实习生，我会唱")
        print("还会跳")
        print("总之啥都会")
        def zzz():
            print(1)       #成员方法里面只能引用普通方法
        zzz()


    def tiao(self,wd):      # wd = "广场舞"
        print("我会跳{}".format(wd))


    # self用法
    # self和实例化对象一样，self在类里面,实例化对象在类的外面
    def rap(self):
        b = self.nl
        print(b)
        self.chang()


#实例化类：d是Person实例化对象
#引用类，不要放到类里面
d = Person()    #赋值语句


# print(d.mz)      #引用成员变量
# d.chang()        #引用成员
# d.tiao("广场舞")  #成员方法的传参


# self在类里面引用方法和变量
# d.rap()




#类的构造

# class Person():
#     name = "战三"
#     age = 18
    
#     def __init__(self,mz,xb):     # 构造一个成员变量
#         self.name = mz
#         self.age = xb             # 用新构造的变量去覆盖之前变量的值
#         self.my()                 # 引用成员方法
    
#     def my(self):
#         print("你好")

# v = Person("李四",22)             #赋值新的值
# print(v.name)
# print(v.age)





#类的继承

class Daxie():
    zm = 26

    def xx(self):
        print("大写字母一共26个")

class Xiaoxie(Daxie):
    zm = 5

    def xx(self):
        print("小写字母也是26个")
    
k = Xiaoxie()      #实例化
print(k.zm)        #子类继承父类的属性
k.xx()             #子类继承父类的方法