"""
学习来源：https://www.cnblogs.com/ryanzheng/p/9693511.html
总结：正删改查区别大多在sql_sentence
注意：批量插入和查寻方式
"""
import psycopg2

class Psql:
    def __init__(self,user,password,host,port,db):
        """
        初始化参数
        :param user: 用户名【数据库的】
        :param password:密码【数据库的】
        :param host:IP
        :param port:端口
        :param db:数据库
        """
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.db = db
        self.conn = None     #连接状态


    def connection(self):
        """
        :连接
        :return: 连接成功的conn对象
        """
        self.conn = psycopg2.connect(database=self.db, user=self.user, password=self.password, host=self.host,port=self.port)
        print('connection is successful!')

        return self.conn

#实验
conn = Psql(user='postgres',password='postgres',host='127.0.0.1',port='5432',db='test').connection()    #连接数据库
cur = conn.cursor()  #游标

"""
#操作****
psql = Psql(user='postgres',password='postgres',host='127.0.0.1',port='5432',db='test')
conn = psql.connection()    #连接数据库
cur = conn.cursor()  #游标
sql_sentence = '''xxxxx'''  #sql语句
cur.execute(sql_sentence)
conn.commit()   #执行
conn.close()    #关闭
"""

#创建表
"""sql_sentence =  '''
                create table table1(
                id    int    primary key not null,
                name  text,
                age   int
                );
                '''
 
cur.execute(sql_sentence)   #编译sql语句
conn.commit()   #执行
conn.close()    #关闭"""

#插入数据【实验插入100条数据】
""" 
import numpy as np
for i in range(100):
    sql = '''insert into table1(id, name, age) values ({},'{}',{})'''.format(i, '张'+str(np.random.randint(100)), np.random.randint(100))
    cur.execute(sql)
conn.commit()  # 执行
conn.close()  # 关闭"""

#删除数据
""" 
sql = '''DELETE from table1 where id>2;'''
cur.execute(sql)
conn.commit()   #执行
conn.close()    #关闭"""

"""#查看数据
cur.execute("select * from table1;")
rows = cur.fetchall()
print(rows)




conn.close()    #关闭"""
