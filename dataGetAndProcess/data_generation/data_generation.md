## data_generation
存放用户记录数据生成的算法、代码及所生成的用户记录数据

#### getUniqueIdList.py

获取独占某一用户画像的作品id列表

#### getUserImgIdList.py

获取某种用户画像对应的tag，再根据tag获取符合对应画像的作品id列表

#### historyGenerationDemo.py

尝试生成用户记录的demo文件

#### imgBasedHistoryGeneration.py

根据用户画像生成用户记录数据（初始数据与每日阅览数据）

#### userImgDescription.md

用户画像描述

#### data_generation.md

本文档

### selectList

存放符合各个用户画像对应tag的作品id列表
#### zhongerSelectList.json
存放符合中二画像对应tag的作品id列表
#### xianchongSelectList.json
存放符合现充画像对应tag的作品id列表
#### feizhaiSelectList.json
存放符合肥宅画像对应tag的作品id列表
#### zhiguaiSelectList.json
存放符合志怪画像对应tag的作品id列表
#### qingchunSelectList.json
存放符合青春画像对应tag的作品id列表

### sysData
存放系统用户记录数据的json文件
#### sysData.json
新生成数据默认存放位置
#### sysDataV1.json
不考虑独占一特定画像作品情况下的记录生成文件（次新数据）
#### sysDataV2.json
考虑独占一特定画像作品情况下的记录生成文件（最新数据）

### uniqueList
存放独占某一特定画像作品的id列表
#### zhongerUniqueIdList.json
存放仅独占中二画像的作品id列表
#### xianchongUniqueIdList.json
存放仅独占现充画像的作品id列表
#### feizhaiUniqueIdList.json
存放仅独占肥宅画像的作品id列表
#### zhiguaiUniqueIdList.json
存放仅独占志怪画像的作品id列表
#### qingchunUniqueIdList.json
存放仅独占青春画像的作品id列表

