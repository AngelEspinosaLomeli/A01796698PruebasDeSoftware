import unittest
import os
from models import Hotel, Customer, Reservation

class TestHotelManagement(unittest.TestCase):
    """Unit tests for Hotel, Customer, and Reservation classes."""

    def setUp(self):
        """Clean up files before each test."""
        for f in ["hotels.json", "customers.json", "reservations.json"]:
            if os.path.exists(f):
                os.remove(f)

    def test_hotel_crud(self):
        Hotel.create_hotel(1, "Grand Plaza", "NYC", 50)
        hotel = Hotel.display_hotel(1)
        self.assertEqual(hotel['name'], "Grand Plaza")
        
        Hotel.modify_hotel(1, name="Updated Plaza")
        hotel = Hotel.display_hotel(1)
        self.assertEqual(hotel['name'], "Updated Plaza")
        
        Hotel.delete_hotel(1)
        self.assertIsNone(Hotel.display_hotel(1))

    def test_customer_crud(self):
        Customer.create_customer(101, "John Doe", "john@example.com")
        cust = Customer.display_customer(101)
        self.assertEqual(cust['name'], "John Doe")
        
        Customer.delete_customer(101)
        self.assertIsNone(Customer.display_customer(101))

    def test_reservation_flow(self):
        Hotel.create_hotel(1, "Motel 6", "LA", 10)
        Customer.create_customer(101, "Jane Doe", "jane@example.com")
        Reservation.create_reservation(500, 101, 1)
        
        res_list = Reservation.load_data(Reservation.FILE) # If helper was public
        self.assertTrue(len(res_list) > 0)
        
        Reservation.cancel_reservation(500)
        # Verify empty...

    def tearDown(self):
        """Clean up files after tests."""
        self.setUp()

if __name__ == '__main__':
    unittest.main()