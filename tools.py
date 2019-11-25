import pymysql    #导入包

# 连接数据库
# 选择数据库
# 获取游标
# 增删改查
def query(sql):
    '''
    查询sql方法
    '''

    db = pymysql.connect(host="localhost",user="root",password="123456",db="testdb")   #连接并选择数据库
    cursor = db.cursor()                 #获取游标
    try:
        cursor.execute(sql)                  #执行sql语句
        res = cursor.fetchall()              # 获取查询结果
        db.close()                           #  关闭数据库
        return res                           #  返回参数
    except:
        return "sql错误"
   
    

def commit(sql):
    '''
    修改sql方法
    '''

    db = pymysql.connect(host="localhost",user="root",password="123456",db="testdb")   #连接并选择数据库
    cursor = db.cursor()                 #获取游标
    try:
        cursor.execute(sql)                  #   执行sql语句
        db.commit()                          #   点击提交
        db.close()                           #  关闭数据库
        return True                          #  返回参数
    except:
        return "sql错误"
   
    
                               
   
   

