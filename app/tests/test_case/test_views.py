import sys
sys.path.append('../../..')

import unittest

from app.views.controllers import generate_data_for_tiles, generate_description_for_top_item, \
    generate_data_for_unique_items, generate_antibiotics_barchart_data, \
    generate_barchart_data, home


class ViewsTests(unittest.TestCase):
    """Class for testing views functionality and connection."""
    def test_generate_data_for_tiles(self):
        self.assertEquals(generate_data_for_tiles(), [8218165, 76.22])

    def test_generate_description_for_top_item(self):
        self.assertEquals(generate_description_for_top_item(), ["Methadone HCl_Oral Soln 1mg/1ml S/F"])

    def test_generate_data_for_unique_items(self):
        self.assertEquals(generate_data_for_unique_items(), [13935])

    def test_generate_antibiotics_barchart_data(self):
        self.assertListEqual(generate_antibiotics_barchart_data("RXA"), [[408, 30], ['Y00327', 'Y04109']])

    def test_generate_barchart_data(self):
        self.assertListEqual(generate_barchart_data(), [[229169, 799112, 583776, 567062, 652972, 531254, 331009,
                                                         457151, 374641, 395672, 531267, 299724, 567186, 253161,
                                                         216994, 336864, 430706, 11, 6612, 165, 2365, 2765, 846,
                                                         636539, 976, 1269, 21, 2, 1445, 965, 2855, 2, 1083, 2524],
                                                        ['01C', '01R', '02D', '02E', '02F', '12F', '322', 'RTV', 'RWW',
                                                        'RXA', 'RY7', '00C', '00D', '00J', '00K', '00M', '111', '112',
                                                         '113', '114', '116', '117', 'AJ6', 'DAN', 'Q45', 'RTR', 'RVW',
                                                         '00T', '00V', '00Y', '01D', '01G', '01W', '01Y']
                                                        ])


if __name__ == "__main__":
    unittest.main()
