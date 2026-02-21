"""
Módulo de gestión de Hoteles, Clientes y Reservaciones.
Provee persistencia de datos mediante archivos JSON.
"""
import json
import os


def load_data(file_name):
    """Carga datos desde un archivo JSON."""
    if not os.path.exists(file_name):
        return []
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError) as error:
        print(f"Error cargando {file_name}: {error}")
        return []


def save_data(file_name, data):
    """Guarda datos en un archivo JSON."""
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
    except IOError as error:
        print(f"Error guardando en {file_name}: {error}")


class Hotel:
    """Clase que representa un Hotel."""
    FILE = "hotels.json"

    def __init__(self, hotel_id, name, location, rooms):
        """Inicializa una instancia de Hotel."""
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms = rooms

    @staticmethod
    def create_hotel(hotel_id, name, location, rooms):
        """Crea un hotel y lo guarda en el archivo."""
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
        """Elimina un hotel por su ID."""
        hotels = [h for h in load_data(Hotel.FILE)
                  if h['hotel_id'] != hotel_id]
        save_data(Hotel.FILE, hotels)

    @staticmethod
    def display_hotel(hotel_id):
        """Muestra la información de un hotel."""
        hotels = load_data(Hotel.FILE)
        hotel = next((h for h in hotels if h['hotel_id'] == hotel_id), None)
        if hotel:
            print(f"Hotel: {hotel['name']} | Ciudad: {hotel['location']}")
        return hotel

    @staticmethod
    def modify_hotel(hotel_id, **kwargs):
        """Modifica atributos de un hotel existente."""
        hotels = load_data(Hotel.FILE)
        for hotel in hotels:
            if hotel['hotel_id'] == hotel_id:
                hotel.update(kwargs)
        save_data(Hotel.FILE, hotels)


class Customer:
    """Clase que representa un Cliente."""
    FILE = "customers.json"

    @staticmethod
    def create_customer(customer_id, name, email):
        """Crea un cliente y lo guarda en el archivo."""
        customers = load_data(Customer.FILE)
        customers.append({
            "customer_id": customer_id,
            "name": name,
            "email": email
        })
        save_data(Customer.FILE, customers)

    @staticmethod
    def delete_customer(customer_id):
        """Elimina un cliente por su ID."""
        customers = [c for c in load_data(Customer.FILE)
                     if c['customer_id'] != customer_id]
        save_data(Customer.FILE, customers)

    @staticmethod
    def display_customer(customer_id):
        """Muestra la información de un cliente."""
        customers = load_data(Customer.FILE)
        cust = next((c for c in customers if c['customer_id'] == customer_id),
                    None)
        if cust:
            print(f"Cliente: {cust['name']} | Email: {cust['email']}")
        return cust

    @staticmethod
    def modify_customer(customer_id, **kwargs):
        """Modifica información de un cliente."""
        customers = load_data(Customer.FILE)
        for cust in customers:
            if cust['customer_id'] == customer_id:
                cust.update(kwargs)
        save_data(Customer.FILE, customers)


class Reservation:
    """Clase que representa una Reservación."""
    FILE = "reservations.json"

    @staticmethod
    def create_reservation(res_id, customer_id, hotel_id):
        """Crea una reservación vinculando cliente y hotel."""
        reservations = load_data(Reservation.FILE)
        reservations.append({
            "res_id": res_id,
            "customer_id": customer_id,
            "hotel_id": hotel_id
        })
        save_data(Reservation.FILE, reservations)

    @staticmethod
    def cancel_reservation(res_id):
        """Cancela una reservación por su ID."""
        reservations = [r for r in load_data(Reservation.FILE)
                        if r['res_id'] != res_id]
        save_data(Reservation.FILE, reservations)
