#postgresql数据库API开发
import psycopg2
from functools import reduce

class PgSql:
    '''init'''
    def __init__(self, host='127.0.0.1', port='5432', user='postgres', password='Li123456'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.conn = None

    '''connectin to database'''
    def connection(self,db_name):
        self.conn = psycopg2.connect(database=db_name, user=self.user, password=self.password, host=self.host,port=self.port)

    '''Checks whether the database is connected
        the function will return true if connected db;
        otherwith return flase  
    '''
    def detection(self):
        return self.conn != None

    '''
    to execute sql
    '''
    def execute_sql(self,sql):
        cur = self.conn.cursor()  #Init cursor
        if not self.detection:
            print('Database not connected！')
        else:
            cur.execute(sql)    #execute
            self.conn.commit()  #commit
            self.conn.close()   #colse

    '''create a table on database
        Amg:
            db_name : The database in
            table_name: 
            structure: the table structure like structure = ['id int prmary key auto_increment', 'name varchar(10)', ...]
        Result:
    '''
    def create_db(self,db_name,table_name, structure):
        self.connection(db_name)
        sql = '''create table "%s"(%s);''' % (table_name, reduce(lambda x,y:x+(','+y), structure))
        self.execute_sql(sql)
        print('create {} successful!'.format(table_name))
            

    '''Get table name from databases
    Amg:
        db_name:set a database
    return:
        Retuen table_name list from db
    '''
    def get_tablename(self,db_name):
        self.connection(db_name)    #To connected database
        cur = self.conn.cursor()    #Set a cursor
        cur.execute("select * from pg_tables where schemaname='public';")
        table_name_list = list(map(lambda x:x[1], cur.fetchall()))
        self.conn.close()
        self.conn = None
        return table_name_list