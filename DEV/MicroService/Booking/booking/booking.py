from pymongo import MongoClient


class Booking:
    def __init__(self):
        self._port = 27017
        self._ip = '127.0.0.1'
        self._client = MongoClient(self._ip, self._port)
        self._collection_name = 'price_collection'
        self._db = self._client[self._collection_name]

    def getBookingId(self, date, client_id):
        posts = self._db.posts
        booking_id = posts.find_one({
            "booking": {
                "client_id": client_id,
                "month": date.getDay(),
                "year": date.getYear(),
                "day": date.getDay()
            }
        }).distinct("_id")
        return booking_id

    def addBooking(self, hotel_id, date, client_id):
        posts = self._db.posts
        posts.update(
            {
                "hotel_id": hotel_id
            }, {
                "$push": {
                    "hotel": {
                        "month": date.getDay(),
                        "year": date.getYear(),
                        "day": date.getDay(),
                        "client_id": client_id
                    },
                    "hotel_id": hotel_id
                }
            },
            upsert=True)

    def removeBooking(self, booking_id):
        posts = self._db.posts
        posts.delete({"_id": booking_id})
