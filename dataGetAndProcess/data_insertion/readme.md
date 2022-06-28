## data_insertion
用于将所需要数据插入到数据库中，使用pymysql连接数据库进行插值，对于数据字段予以操作：适配数据库的字段类型，处理非法字符
#### animeIns.py
根据生成的anime数据的json文件插入其中数据到数据库中
#### animeInsTest.py 
根据生成的anime数据的json文件插入其中数据的单元测试
#### comicIns.py
根据生成的comic数据的json文件插入其中数据到数据库中
#### connectTest.py
连接数据库测试，本地（服务器）
#### cosplayIns.py
根据生成的cosplay数据的json文件插入其中数据到数据库中
#### novelInsert.py
根据生成的novel数据的json文件插入其中数据到数据库中
#### reTest.py
正则化处理的测试，插入数据过程中，部分非法字符需要剔除
#### userHistoryInsert.py
生成用户记录数据同时插入数据库中
#### userIns.py
生成用户账户数据并将数据插入数据库中
#### userJsonInsertDB.py
根据生成的存储用户记录数据的json文件将其中数据插入数据库中
#### wrongNovelInsert.py
小说数据中对于部分简介字段中包含emoji表情的特殊数据的处理