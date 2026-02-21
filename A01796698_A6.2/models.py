import json
import os

def load_data(file_name):
    """Helper to load JSON data from a file."""
    if not os.path.exists(file_name):
        return []
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError) as error:
        print(f"Error loading {file_name}: {error}")
        return []

def save_data(file_name, data):
    """Helper to save JSON data to a file."""
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
    except IOError as error:
        print(f"Error saving to {file_name}: {error}")


class Hotel:
    """Class representing a Hotel."""
    FILE = "hotels.json"

    def __init__(self, hotel_id, name, location, rooms):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms = rooms

    @staticmethod
    def create_hotel(hotel_id, name, location, rooms):
        hotels = load_data(Hotel.FILE)
        hotels.append({
            "hotel_id": hotel_id,
            "name": name,
            "location": location,
            "rooms": rooms
        })
        save_data(Hotel.FILE, hotels)

    @staticmethod
    def delete_hotel(hotel_id):
        hotels = [h for h in load_data(Hotel.FILE)
                  if h['hotel_id'] != hotel_id]
        save_data(Hotel.FILE, hotels)

    @staticmethod
    def display_hotel(hotel_id):
        hotels = load_data(Hotel.FILE)
        hotel = next((h for h in hotels if h['hotel_id'] == hotel_id), None)
        if hotel:
            print(f"Hotel: {hotel['name']} | Location: {hotel['location']}")
        return hotel

    @staticmethod
    def modify_hotel(hotel_id, **kwargs):
        hotels = load_data(Hotel.FILE)
        for hotel in hotels:
            if hotel['hotel_id'] == hotel_id:
                hotel.update(kwargs)
        save_data(Hotel.FILE, hotels)


class Customer:
    """Class representing a Customer."""
    FILE = "customers.json"

    @staticmethod
    def create_customer(customer_id, name, email):
        customers = load_data(Customer.FILE)
        customers.append({
            "customer_id": customer_id,
            "name": name,
            "email": email
        })
        save_data(Customer.FILE, customers)

    @staticmethod
    def delete_customer(customer_id):
        customers = [c for c in load_data(Customer.FILE)
                     if c['customer_id'] != customer_id]
        save_data(Customer.FILE, customers)

    @staticmethod
    def display_customer(customer_id):
        customers = load_data(Customer.FILE)
        cust = next((c for c in customers if c['customer_id'] == customer_id),
                    None)
        if cust:
            print(f"Customer: {cust['name']} | Email: {cust['email']}")
        return cust


class Reservation:
    """Class representing a Reservation."""
    FILE = "reservations.json"

    @staticmethod
    def create_reservation(res_id, customer_id, hotel_id):
        reservations = load_data(Reservation.FILE)
        reservations.append({
            "res_id": res_id,
            "customer_id": customer_id,
            "hotel_id": hotel_id
        })
        save_data(Reservation.FILE, reservations)

    @staticmethod
    def cancel_reservation(res_id):
        reservations = [r for r in load_data(Reservation.FILE)
                        if r['res_id'] != res_id]
        save_data(Reservation.FILE, reservations)