"""
NAME:          test_database.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          24/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Suite of tests for testing the dashboards database
               functionality.
"""
import sys
sys.path.append('../../..')

import unittest

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
        self.assertEquals(self.db_mod.get_max_quantity(), 869879,
                          'Test the quantity of items with max quantity returns correct value')

    def test_get_total_quantity(self):
        """Test that the sum of quantity for total items returns the correct value."""
        self.assertEquals(self.db_mod.get_total_quantity(), int(617395554.56),
                          'Test the sum of quantity for total items returns correct value')
        
    def test_get_numberof_unique_item(self):
        """Test that number of unique items returns the correct value."""
        self.assertEquals(self.db_mod.get_numberof_unique_items(), 13935,
                          'Test number of unique items returns correct value')

    def test_get_max_quantity_item_name(self):
        self.assertEquals(self.db_mod.get_max_quantity_item_name(), "Methadone HCl_Oral Soln 1mg/1ml S/F",
                          'Test name of the item with max quantity')

    def test_percentageof_all_infection_treatments(self):
        """Test that Infection treatment drug % of all infection treatments returns the correct value."""
        self.assertListEqual(self.db_mod.get_percentageof_all_infection_treatments(), [82.25, 5.22, 2.68, 9.62, 0.23], 'Test the Infection treatment drug % of all infection treatments returns the correct value')

    def test_get_number_of_prescribed_antibiotics_in_RTV(self):
        """Test the number of prescribed antibiotics per practice in RTV"""
        self.assertListEqual(self.db_mod.get_n_antibiotics_per_practice_for_pct("RTV"), [(9,)], 'Test number of antibiotics per practice in RTV returns correct value')
    
    def test_get_n_data_for_drug(self):
        """Test the data in drug information of pct"""
        # assertIn(a, b)
        pct_list = ['12F','01G','01D','02E','00T','01R','00M','00D','01W','01C','00Y','00K','02F','00J']
        self.assertIn(self.db_mod.get_n_data_for_drug("Mucogel_Susp 195mg/220mg/5ml S/F")[0][0],pct_list,'Test the data in drug information of pct')
        
    def test_get_n_data_for_drug_count(self):
        """Test the unexsiting data in drug information of pct"""
        self.assertEquals(self.db_mod.get_n_data_for_drug_count("Mucogel_Susp 195mg/220mg/5ml S/FF"), 0, 'Test the unexsiting data in drug information of pct')
    
    def test_get_practice_drug(self):
        """Test the practice-drug data"""
        practice_list = ['N85016','N85001','N85014','N85016','N85024','N85029','N85023','N85001']
        self.assertIn(self.db_mod.get_practice_drug("12F", "Mucogel_Susp 195mg/220mg/5ml S/F")[0][0],practice_list,'Test the practice-drug data')
    
    def test_get_distinct_drugname(self):
        """Test the distinct drug name data"""
        self.assertEquals(len(self.db_mod.get_distinct_drugname()),13922,'Test the distinct drug name data')
    
    def test_get_distinct_drugcpde(self):
        """Test the distinct drug code data"""
        self.assertEquals(len(self.db_mod.get_distinct_drugcode()),13922,'Test the distinct drug code data')
    
    def test_get_bnf_code(self):
        """Test whether the bnf name can be matched to the correct bnf code"""
        self.assertEquals(self.db_mod.get_bnf_code("Mucogel_Susp 195mg/220mg/5ml S/F"),"0101010G0BCABAB",'Test whether the bnf name can be matched to the correct bnf code')



if __name__ == "__main__":
    unittest.main()
