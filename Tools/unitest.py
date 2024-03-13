import unittest

def is_true_parameter(parameter):
    return parameter == 50 or (parameter >= 2000 and (parameter - 2000) % 2000 == 0) or (parameter >= 32050 and (parameter - 32050) % 2000 == 0)

class TestParameter(unittest.TestCase):

    def test_true_values(self):
        true_values = [50, 2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000, 18000, 20000, 22000, 24000, 26000, 28000, 30000, 32000, 32050, 34000, 36000, 38000, 40000, 42000, 44000, 46000, 48000, 50000, 52000, 54000, 56000, 58000, 60000, 62000, 64000]
        for value in true_values:
            with self.subTest(value=value):
                self.assertTrue(is_true_parameter(value))

    def test_false_values(self):
        false_values = [0, 100, 1999, 3000, 3500, 6001, 32001, 33000, 31999]
        for value in false_values:
            with self.subTest(value=value):
                self.assertFalse(is_true_parameter(value))

if __name__ == '__main__':
    unittest.main()
