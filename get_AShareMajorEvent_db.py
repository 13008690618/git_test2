#make AShareMajorEvent to database
import re
import os
import gzip
from PostgreSQL import *
from xml.etree import ElementTree as ET

pgsql = PgSql()	#Init the databases



'''parsing Product Element'''
def parse_product(product):
  #table = product.findall('')[0].text
  title = product.findall('OBJECT_ID')[0].text
  text = product.findall('S_EVENT_CONTENT')[0].text
  source = 'AShareMajorEvent'
  date = product.findall('OPDATE')[0].text

  return [title, text, source, 'news', date]


'''parsing xml'''
def parse_xml(xml_file):
  per = ET.parse(gzip.open(xml_file, 'r'))     #open the xml.gz
  all_product = per.findall('./Product')  #because of there are many label in the Product ,so it return some Element 'Product'
  #Parse each Product_Element through a loop
  for product in all_product:
    try:
      x = parse_product(product)
      #make data to database
      pgsql.insert_into_db('dbnews_china', '27', field_list=['title','text','source','type','date'], value_list=x)
    except:
      pass
    

'''Get the file name under the folder'''
def FileList(dir_path):

  return os.listdir(dir_path)


if __name__ == '__main__':
  dir_path = "/home/DATA/AShareMajorEvent/"
  for file in FileList(dir_path):
    parse_xml(dir_path+file)
    