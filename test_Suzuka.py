import unittest
from unittest.mock import patch
from Suzuka import Menu

class MenuTestCase(unittest.TestCase):
    def setUp(self):
        self.menu = Menu()

    def test_product_menu_add(self):
        with patch('builtins.input', side_effect=['1', '1', 'Test Product', '10.99', '6']):
            self.menu.menu()
            products = self.menu.productController.list()
            self.assertEqual(len(products), 1)
            self.assertEqual(products[0].name, 'Test Product')
            self.assertEqual(products[0].price, '10.99')

    def test_product_menu_list(self):
        with patch('builtins.input', side_effect=['1', '1', 'Test Product', '10.99', '2', '6']):
            self.menu.menu()
            with patch('builtins.print') as mock_print:
                self.menu.menu()
                mock_print.assert_called_with('1 - Test Product - 10.99')

    def test_product_menu_search(self):
        with patch('builtins.input', side_effect=['1', '1', 'Test Product', '10.99', '3', '1', '6']):
            self.menu.menu()
            with patch('builtins.print') as mock_print:
                self.menu.menu()
                mock_print.assert_called_with('1 - Test Product - 10.99')

    def test_product_menu_delete(self):
        with patch('builtins.input', side_effect=['1', '1', 'Test Product', '10.99', '4', '1', '6']):
            self.menu.menu()
            self.assertEqual(len(self.menu.productController.list()), 0)

    def test_product_menu_update(self):
        with patch('builtins.input', side_effect=['1', '1', 'Test Product', '10.99', '5', '1', 'Updated Product', '19.99', '6']):
            self.menu.menu()
            products = self.menu.productController.list()
            self.assertEqual(len(products), 1)
            self.assertEqual(products[0].name, 'Updated Product')
            self.assertEqual(products[0].price, '19.99')

    def test_customer_menu_add(self):
        with patch('builtins.input', side_effect=['2', '1', '1', 'Test Customer', 'test@example.com', '6']):
            self.menu.menu()
            customers = self.menu.customerController.list()
            self.assertEqual(len(customers), 1)
            self.assertEqual(customers[0].name, 'Test Customer')
            self.assertEqual(customers[0].email, 'test@example.com')

    def test_customer_menu_list(self):
        with patch('builtins.input', side_effect=['2', '1', '1', 'Test Customer', 'test@example.com', '2', '6']):
            self.menu.menu()
            with patch('builtins.print') as mock_print:
                self.menu.menu()
                mock_print.assert_called_with('1 - Test Customer - test@example.com')

    def test_customer_menu_search(self):
        with patch('builtins.input', side_effect=['2', '1', '1', 'Test Customer', 'test@example.com', '3', '1', '6']):
            self.menu.menu()
            with patch('builtins.print') as mock_print:
                self.menu.menu()
                mock_print.assert_called_with('1 - Test Customer - test@example.com')

    def test_customer_menu_delete(self):
        with patch('builtins.input', side_effect=['2', '1', '1', 'Test Customer', 'test@example.com', '4', '1', '6']):
            self.menu.menu()
            self.assertEqual(len(self.menu.customerController.list()), 0)

    def test_customer_menu_update(self):
        with patch('builtins.input', side_effect=['2', '1', '1', 'Test Customer', 'test@example.com', '5', '1', 'Updated Customer', 'new@example.com', '6']):
            self.menu.menu()
            customers = self.menu.customerController.list()
            self.assertEqual(len(customers), 1)
            self.assertEqual(customers[0].name, 'Updated Customer')
            self.assertEqual(customers[0].email, 'new@example.com')

if __name__ == '__main__':
    unittest.main()
