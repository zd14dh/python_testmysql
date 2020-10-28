import pymysql

class Mysql():
    #传参数
    def __init__(self,host,user,passwd,database,scursorclass=None):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
        self.scursorclass=scursorclass
        if scursorclass:
            self.scursorclass= scursorclass

        else:
            self.scursorclass= None

    #连接数据库

    def connect(self):
        #连接数据库对象
        self.db=pymysql.connect(self.host,self.user,self.passwd,self.database)
        #建立游标对象
        self.curosr=self.db.cursor()

    #执行查询一条数据
    def get_one(self,sql):
        result=0
        try:
            #调用connect连接方法
            self.connect()
            self.curosr.execute(sql)
            result=self.curosr.fetchone()
            self.close()
        except Exception as E:
            print('查询失败：',E)
        return result

    #执行查询全部数据
    def get_all(self,sql):
        result= 0
        try:
            self.connect()
            self.curosr.execute(sql)
            result=self.curosr.fetchall()
            self.close()

        except Exception as E:
            print('select error:',E)

        return result
    #关闭数据库连接
    def close(self):
        self.curosr.close()
        self.db.close()
