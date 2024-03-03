## 安裝 pymongo
## python -m install pymongo # shell or bash
import pymongo 
# 連線DB
host = "mongodb://localhost:27017/"
myclient = pymongo.MongoClient(host)
db_str = "testMongoDB"
mydb = myclient[db_str]
dblst = myclient.list_database_names()

if db_str in dblst:
    print(db_str + "已存在!")
col_str = "testMongoCol"
mycol = mydb[col_str]
collst = mydb.list_database_names()
if col_str in collst: # test MongoCol 集合是否存在
 print(col_str + "已存在")
 mytestData = {"name": "Andy", "gender": "male", "adderss": "台北"}
 x = mycol.insert_one(mytestData)
 x = mycol.find_one()
print("Result:", x)
