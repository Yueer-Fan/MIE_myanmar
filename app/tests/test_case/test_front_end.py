import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class TestWebForm(unittest.TestCase):
    """Class for test basic functionality of a web-based input form."""
    def setUp(self):
        """Set up function to set the web driver Safari."""
        self.driver = webdriver.Safari()

    def test_input_form(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/dashboard/home/")
        driver.maximize_window()

        """Test four data in title."""
        ti = driver.find_element_by_id("total_items").text
        self.assertEqual(ti, "8218165")
        ac = driver.find_element_by_id("avg_cost").text
        self.assertEqual(ac, "£76.22")
        tnq = driver.find_element_by_id("top_nq").text
        self.assertEqual(tnq, "Methadone HCl_Oral Soln 1mg/1ml S/F (869879)")
        td = driver.find_element_by_id("top_data").text
        self.assertEqual(td, "0.14%")
        nu = driver.find_element_by_id("num_uni").text
        self.assertEqual(nu, "13935")

        """Test five figures in infection treatment."""
        ab = driver.find_element_by_id("anti_b").text
        self.assertEqual(ab, "82.25%")
        af = driver.find_element_by_id("anti_f").text
        self.assertEqual(af, "5.22%")
        av = driver.find_element_by_id("anti_v").text
        self.assertEqual(av, "2.68%")
        ap = driver.find_element_by_id("anti_p").text
        self.assertEqual(ap, "9.62%")
        ah = driver.find_element_by_id("ant_h").text
        self.assertEqual(ah, "0.23%")
        time.sleep(2)

        """Test button of about box."""
        driver.find_element_by_id("ab-box").click()
        time.sleep(2)
        driver.find_element_by_id("close_about").click()
        time.sleep(1)

        """Test button of generate report."""
        driver.find_element_by_id("gen-re").click()
        time.sleep(1)
        driver.find_element_by_id("yes").click()
        time.sleep(1)
        driver.find_element_by_id("no").click()
        time.sleep(2)

        """Test function of creatinine calculator."""
        driver.find_element_by_id("crea-cl").click()
        time.sleep(1)
        driver.find_element_by_id("female").click()
        time.sleep(1)
        driver.find_element_by_id("Age").send_keys("65")
        time.sleep(1)
        driver.find_element_by_id("Weight").send_keys("67.2")
        time.sleep(1)
        driver.find_element_by_id("serum").send_keys("65.4")
        time.sleep(1)
        driver.find_element_by_id("calculate").click()
        time.sleep(2)
        driver.find_element_by_id("reset").click()
        time.sleep(1)
        driver.find_element_by_id("close").click()
        time.sleep(2)

        """Test data in BNF data per PCT."""
        # js = "arguments[0].scrollIntoView()"11
        # el = driver.find_element_by_id("input-group-select")
        # driver.execute_script("document.documentElement.scrollTop=10000")
        # time.sleep(2)
        # lis = driver.find_element_by_id("input-group-select")
        # ActionChains(driver).move_to_element(lis).click().perform()
        # time.sleep(3)
        # s = Select(lis)
        # # s.select_by_value("RWW")
        # s.select_by_index(8)
        # time.sleep(3)
        # driver.find_element_by_id("update").submit()
        # time.sleep(5)
        # driver.execute_script("document.documentElement.scrollTop=10000")
        # time.sleep(2)
        driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(2)
        s = driver.find_element_by_css_selector("select#input-group-select")
        s.click()
        driver.find_element_by_id("input-group-select").send_keys("RWW")
        # s.find_element_by_css_selector("option[value='RWW']").click()
        time.sleep(3)
        driver.find_element_by_id("update").submit()
        time.sleep(5)
        driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(2)
        # lis = driver.find_element_by_id("input-group-select")
        # ActionChains(self.driver).move_to_element(lis).perform()
        # driver.find_element_by_id("input-group-select").click()
        # s = Select(lis)
        # s.select_by_value("RWW")

        # for li in lis:
        #     if "RWW" in lis.text:
        #         li.click()
        #         break
        # sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

