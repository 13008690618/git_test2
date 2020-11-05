#postgresql数据库API开发
import psycopg2
import nump
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
        self.conn = psycopg2.connect(database=db_name, user=self.user, password=self.password, host=self.host, port=self.port)


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

    '''Insert data to databases(dbnews_china or db_english)
    Args:
        db_name:The database of accepts
        table_name: the data insert in to
        field_list: eg：['title', 'text', 'source', 'type', 'date']
        value_list:
    '''
    def insert_into_db(self，db_name, table_name, field_list, value_list):
        #self.connection(db_name)    #connected to dataabse
        #
        if len(field_list) != len(value_list):
            print('The quantities of Field and Value are not equal！')
            return

        sql_ = reduce(lambda x,y:x+(','+y), field_list)
        print(sql_)
        #sql = '''insert into "%s" (title, text, source, type, date) values ('%s', '%s', '%s', '%s', '%s');''' % (table, title, text, source, type, date)
        #self.execute_sql(sql)
        pass