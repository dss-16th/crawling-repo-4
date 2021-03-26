import pymongo

client = pymongo.MongoClient("mongodb://private_key:port_number")
collection = client.covid19_total.total
