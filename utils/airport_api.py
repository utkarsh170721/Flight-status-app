import requests

def get_flight_data(flight_number):
    # Mock function to fetch data from an external API
    response = requests.get(f'https://api.example.com/flights/{flight_number}')
    return response.json()
