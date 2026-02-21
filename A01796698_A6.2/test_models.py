def test_negative_hotel_not_found(self):
        """Prueba buscar un hotel que no existe."""
        result = Hotel.display_hotel(999)
        self.assertIsNone(result)

    def test_negative_corrupt_json(self):
        """Prueba el manejo de un archivo JSON corrupto."""
        with open("hotels.json", "w", encoding='utf-8') as f:
            f.write("{ este no es un json válido }")
        # El programa debe manejar el error y retornar una lista vacía
        result = Hotel.display_hotel(1)
        self.assertIsNone(result)

    def test_negative_invalid_customer_id(self):
        """Prueba eliminar un cliente con un ID inexistente."""
        Customer.create_customer(1, "Test", "test@test.com")
        # No debe lanzar excepción aunque el ID sea distinto
        Customer.delete_customer(999)
        cust = Customer.display_customer(1)
        self.assertIsNotNone(cust)

    def test_negative_cancel_non_existent_reservation(self):
        """Prueba cancelar una reservación que no existe."""
        # No debe fallar ni detener la ejecución
        Reservation.cancel_reservation(888)
        
    def test_negative_modify_non_existent_hotel(self):
        """Prueba modificar un hotel que no existe."""
        # No debe lanzar error de ejecución
        Hotel.modify_hotel(777, name="Fake Hotel")
        self.assertIsNone(Hotel.display_hotel(777))
