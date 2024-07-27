from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['flightStatusDB']
flights_collection = db['flights']

def insert_flight(flight):
    return flights_collection.insert_one(flight).inserted_id

def get_flights():
    return list(flights_collection.find())
