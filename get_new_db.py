# -*- coding: UTF-8 -*- 
import re
import os
import gzip
from PostgreSQL import *
from xml.etree import ElementTree as ET

pgsql = PgSql() #Init the databases


#***************************************解析****************************************
def US_HK_Wind(windcodes):
    """
    :param x: windcodes标签内值如：1691.HK:JS环球生活|ON0201:A股|ON0204:港股|ON0205:美股|0005.HK:汇丰控股|0014.HK:希慎兴业|0334.HK:华显光电|0347.HK:鞍钢股份|000898.SZ:鞍钢股份|0488.HK:丽新发展|0656.HK:复星国际|
    :return: 含有US或者HK的港股编号或者每股英文名，如：'hshkms', 'hshks', '1772', '1071',
    """
    res = []
    for win in windcodes.split('|'):
        a = win.split(':')[0].split('.')[0].lower()
        try:
            res.append(str(int(a)))
        except:
            res.append(a)
    return res

def GetAttContent(product):
    title = product.findall('title')[0].text
    text = product.findall('content')[0].text
    source = product.findall('source')[0].text
    type_ = 'news'
    date = product.findall('opdate')[0].text
    windcodes = product.findall('windcodes')[0].text    #返回股票种类
    #只返回含有US/HK的windcodes
    if (('HK' in windcodes)|('US' in windcodes)):
        return title, re.sub(r' ',"",re.sub(r'<.*?>',"",text)), source, type_, date, US_HK_Wind(windcodes)


#根据本地文件路径阅读文件
def read_data(path):
    #per = ET.parse(gzip(path))    # 打开xml文档
    per = ET.parse(gzip.open(path, 'r'))     ## 打开xml.gz文档
    all_Product = per.findall('./Product')  #所有的Product
    #对每个Product标签内容进行处理
    for product in all_Product:
        try:
            title, text, source, type_, date_, USorHK_list= GetAttContent(product)
            #插入数据库（不一定要做匹配，try就行）
            for table_name in USorHK_list:
                try:
                    pgsql.insert_into_db('dbnews_china', table_name.lower(), field_list=['title','text','source','type','date'], value_list=[title, text, source, 'news', date_])
                except:
                    pass
        except:
            pass

        


#返回文件夹下所有文件的文件名
def FileList(dir_path='data'):
    return os.listdir(dir_path)


if __name__ == "__main__":
    #dir_path = '/home/ubuntu/wind/__DATA__/FinancialNews'  #第一批
    dir_path = '/home/DATA/FinancialNews'  #第二批

    file_list = FileList(dir_path)

    i, count = 0, len(file_list)    #设置进度标识
    for path in  file_list:
        try:
            read_data(dir_path+'/'+path)
        except:
            pass
        print("\r当前进度：{:.2f}%".format(i*100/count), end="")
        i += 1