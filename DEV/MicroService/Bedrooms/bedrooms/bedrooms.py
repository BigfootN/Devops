from pymongo import MongoClient


class Bedrooms:
    def __init__(self):
        self._port = 27017
        self._ip = '127.0.0.1'
        self._client = MongoClient(self._ip, self._port)
        self._collection_name = 'hotel_collection'
        self._db = self._client[self._collection_name]

    def get(self, room_type_id):
        posts = self._db.posts
        price = posts.find({"rtype_id": room_type_id}).distinct("price")
        return price

    def add_bedroom(self, hotel_id, room_number, room_type_id):
        posts = self._db.posts
        posts.update({{
            "hotel_id": hotel_id,
        }, {
            "$push": {
                "bedroom": {
                    "room_number": room_number,
                    "room_type_id": room_type_id
                }
            }
        }})

    def remove_bedroom(self, room_type_id, price):
        posts = self._db.posts
        posts.delete({"rtype_id": room_type_id, "price": price})
