import unittest
import app
# TODO: Create a better formatted test suite
class TestUtilityMethods(unittest.TestCase):
    def test_format_fullname(self):
        self.assertEqual(app.format_fullname("pearl mcphee"), "PEARL MCPHEE")

    def test_format_zipcode(self):
        self.assertEqual(app.format_zipcode("23"), "00023")

    def test_calc_total_seconds(self):
        self.assertEqual(app.calc_total_seconds("111:23:32.123"), 401012.123)
        self.assertEqual(app.calc_total_seconds("0:23:0"), 1380.0)

    def test_format_datetime_to_ise(self):
        self.assertEqual(app.format_datetime_to_iso("4/1/11 11:00:00 AM"), "2011-04-01T11:00:00")
        self.assertEqual(app.format_datetime_to_iso("4/1/11 11:00:00 PM"), "2011-04-01T23:00:00")

if __name__ == '__main__':
    unittest.main()