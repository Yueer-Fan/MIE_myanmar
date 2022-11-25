import sys
sys.path.append('../../..')

import unittest

from app.views.controllers import generate_data_for_tiles, generate_description_for_top_item,generate_data_for_unique_items,generate_percentageof_all_infection_treatments,generate_antibiotics_barchart_data


class DatabaseTests(unittest.TestCase):
    """Class for testing views functionality and connection."""
    def test_generate_data_for_tiles(self):
        self.assertEquals(generate_data_for_tiles(), [8218165, 76.22])

    def test_generate_description_for_top_item(self):
        self.assertEquals(generate_description_for_top_item(), ["Methadone HCl_Oral Soln 1mg/1ml S/F"])

    def test_generate_data_for_unique_items(self):
        self.assertEquals(generate_data_for_unique_items(), [13935])

    # def test_generate_percentageof_all_infection_treatments(self):
    #     self.assertEquals(generate_percentageof_all_infection_treatments(), [82.25, 5.22, 2.68, 9.62, 0.23])

    def test_generate_antibiotics_barchart_data(self):
        self.assertListEqual(generate_antibiotics_barchart_data("RXA"),[[408, 30], ['Y00327', 'Y04109']])


if __name__ == "__main__":
    unittest.main()
