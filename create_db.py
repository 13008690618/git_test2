#create some table in database
from PostgreSQL import PgSql
import numpy as np
import time

if __name__ == "__main__":
	pgsql = PgSql()
	table_name_list = np.load('dbnews_china_table_name.npy')
	for table_name in table_name_list:
		try:
			structure = [
									'num serial primary key not null',
									'title text not null',
									'text text not null',
									'source character(128) not null',
									'type data_type not null',
									'date timestamp not null',
									]
			pgsql.create_db(db_name='dbnews_china',table_name=table_name,structure=structure)
			time.sleep(0.5)
		except:
			print(table_name+'create error!!')