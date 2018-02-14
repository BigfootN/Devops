from pymongo import MongoClient


class Price:
    def __init__(self):
        self._port = 27017
        self._ip = '127.0.0.1'
        self._client = MongoClient(self._ip, self._port)
        self._collection_name = 'price_collection'
        self._db = self._client[self._collection_name]

    def getPrice(self, room_type_id):
        posts = self._db.posts
        price = posts.find({"rtype_id": room_type_id}).distinct("price")
        return price

    def addPrice(self, room_type_id, price):
        posts = self._db.posts
        posts.insert_one({"rtype_id": room_type_id, "price": price})

    def removePrice(self, room_type_id, price):
        posts = self._db.posts
        posts.delete({"rtype_id": room_type_id, "price": price})
