from pymongo import MongoClient

def init_db():
    client = MongoClient('mongodb://localhost:27017/flight_status')
    db = client['flightStatusDB']
    db.create_collection('flights', capped=False)
    db.create_collection('notifications', capped=False)
