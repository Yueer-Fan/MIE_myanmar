import unittest
from selenium import webdriver

class TestWebForm(unittest.TestCase):
    """Class for test basic functionality of a web-based input form."""
    def setUp(self):
        """Set up function to set the web driver Safari."""
        self.driver = webdriver.Safari()

    def test_input_form(self):
        driver = self.driver
        driver.get("file:///Users/reese/miskeleton/MIE_myanmar/app/tests/index_test.html")

        driver.find_element_by_id("total-items").send_keys("8218165")
        driver.find_element_by_id("act-cost").send_keys("76.22")
        driver.find_element_by_id("top-prescribed-item").send_keys("0.14")
        driver.find_element_by_id("unique-item").send_keys("13935")
        driver.find_element_by_id("per-infect-treat").send_keys("82.25,5.22,2.68,9.62,0.23")
        driver.find_element_by_id("ok-button").click()

if __name__ == "__main__":
    unittest.main()

