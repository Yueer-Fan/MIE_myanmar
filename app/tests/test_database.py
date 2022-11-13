"""
NAME:          test_database.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          24/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Suite of tests for testing the dashboards database
               functionality.
"""

import unittest
#from app import app
from app.database.controllers import Database

class DatabaseTests(unittest.TestCase):
    """Class for testing database functionality and connection."""
    def setUp(self):
        """Run prior to each test."""
        self.db_mod = Database()

    def tearDown(self):
        """Run post each test."""
        pass

    def test_get_total_number_items(self):
        """Test that the total number of items returns the correct value."""
        self.assertEquals(self.db_mod.get_total_number_items(), 8218165, 'Test total items returns correct value')
    def test_get_average_act_cost(self):
        """Test that the average act cost of items returns the correct value."""
        self.assertEquals(self.db_mod.get_average_act_cost(), 76.22, 'Test average act cost returns correct value')
    def test_get_max_quantity(self):
        """Test that the quantity of items with max quantity returns the correct value."""
        self.assertEquals(self.db_mod.get_max_quantity(), 869879, 'Test the quantity of items with max quantity returns correct value')
    def test_get_total_quantity(self):
        """Test that the sum of quantity for total items returns the correct value."""
        self.assertEquals(self.db_mod.get_total_quantity(), int(617395554.56), 'Test the sum of quantity for total items returns correct value')
    def test_get_max_quantity_item_name(self):
        """Test that the item with max quantity returns the correct value."""
        self.assertEquals(self.db_mod.get_max_quantity_item_name(), 0.14, 'Test the item with max quantity returns correct value')
    def test_get_numberof_unique_item(self):
        """Test that number of unique items returns the correct value."""
        self.assertEquals(self.db_mod.get_numberof_unique_items(), 13935, 'Test number of unique items returns correct value')

    def test_get_average_act_cost(self):
        """Test that the average act cost of items returns the correct value."""
        self.assertEquals(self.db_mod.get_average_act_cost(), 76.22, 'Test average act cost returns correct value')

    def test_get_top_prescribed_item(self):
        """Test that the percentage of top prescribed item returns the correct value."""
        self.assertEquals(self.db_mod.get_top_prescribed_item(), 0.14, 'Test average act cost returns correct value')

    def test_get_numberof_unique_item(self):
        """Test that number of unique items returns the correct value."""
        self.assertEquals(self.db_mod.get_numberof_unique_items(), 298682, 'Test number of unique items returns correct value')

if __name__ == "__main__":
    unittest.main()
