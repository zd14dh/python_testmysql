from pyhive import hive

class Hive_test():

    def __init__(self,host, port, username, database):
        self.host=host
        self.port=port
        self.username=username
        self.database=database


    def count(self):
        self.conn=hive.connect(self.host,self.port,self.username,self.database)
        self.cursor=self.conn.cursor()


    def get_fetone(self,hive):
        result=0
        try:
            self.count()
            self.cursor.execute(hive)
            result=self.cursor.fetchone()
            self.close()
        except Exception as e:
            print('查询失败：',e)
        return result

    def close(self):
        self.count().close()


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


