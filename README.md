# git_test2
学习git使用。
1.建立数据库,我是win
	创建类型：
	create type data_type as enum ('news','transcript');
	创建数据库表：
	'num serial primary key not null',
	'title text not null',
	'text text not null',
	'source character(128) not null',
	'type data_type not null',
	'date timestamp not null',
	注意：postgresql没有自增设置：其中serial(序号类型)搭配not null就是自增

2.解析news数据
	我是win
	我是win
