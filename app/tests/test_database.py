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
from selenium import webdriver

class DatabaseTests(unittest.TestCase):
    """Class for testing database functionality and connection."""
    def setUp(self):
        """Run prior to each test."""
        self.db_mod = Database()
        self.driver = webdriver.Safari()

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

    def test_input_form(self):
        driver = self.driver
        driver.get("file:///Users/reese/miskeleton/MIE_myanmar/app/tests/index_test.html")

        driver.find_element_by_id("total-items").send_keys("8218165")
        driver.find_element_by_id("act-cost").send_keys("76.22")
        driver.find_element_by_id("top-prescribed-item").send_keys("0.14")
        driver.find_element_by_id("unique-item").send_keys("13935")
        driver.find_element_by_id("per-infect-treat").send_keys(
            "82.25,5.22,2.68,9.62,2.3")
        driver.find_element_by_id("ok-button").click()

if __name__ == "__main__":
    unittest.main()
