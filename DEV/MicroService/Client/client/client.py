from pymongo import MongoClient


class Client:
    def __init__(self):
        self._port = 27015
        self._ip = '127.0.0.1'
        self._client = MongoClient(self._ip, self._port)
        self._collection_name = 'client_collection'
        self._db = self._client[self._collection_name]

    def getClientId(self, name, last_name, country):
        posts = self._db.posts
        client_id = posts.find_one({
            "client": {
                "name": name,
                "last_name": last_name,
                "country": country
            }
        }).distinct("_id")
        return client_id

    def addClient(self, name, last_name, age, mail, country):
        posts = self._db.posts
        posts.insert_one({
            "client": {
                "name": name,
                "last_name": last_name,
                "age": age,
                "mail": mail,
                "country": country
            }
        })

    def removeClient(self, client_id):
        posts = self._db.posts
        posts.delete({"_id": client_id})
