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

    def test_get_top_prescribed_item(self):
        """Test that the percentage of top prescribed item returns the correct value."""
        self.assertEquals(self.db_mod.get_top_prescribed_item(), 0.14, 'Test average act cost returns correct value')

    def test_get_numberof_unique_item(self):
        """Test that number of unique items returns the correct value."""
        self.assertEquals(self.db_mod.get_numberof_unique_items(), 298682, 'Test number of unique items returns correct value')

if __name__ == "__main__":
    unittest.main()
