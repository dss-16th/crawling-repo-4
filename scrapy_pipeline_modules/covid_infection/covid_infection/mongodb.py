import pymongo

client = pymongo.MongoClient("mongodb://public_ip:port_num")
db = client.keyword
collection = db.kword_infection
