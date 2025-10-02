import unittest
from parameterized import parameterized
from app.main import Calculator
from app.error import InvalidInputException


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculator()

    def tearDown(self) -> None:
        ...

    def test_log(self):
        a = 8
        b = 2

        expected_result = 3
        actual_result = self.calc.log(a, b)

        self.assertEqual(actual_result, expected_result)

    @parameterized.expand([
        ('str_int', 'a', 0, TypeError),
        ('int_str', 0, 'a', TypeError),
        ('str_none', 'a', None, TypeError),
    ])
    def test_log_type(self, name, a, b, expected_result):
        with self.assertRaises(expected_result):
            self.calc.log(a, b)

    @parameterized.expand([
        (-1, 2, InvalidInputException),
        (1, 2, InvalidInputException),
    ])
    def test_log_invalid_input_exception(self, a, b, expected_result):
        with self.assertRaises(expected_result):
            self.calc.log(a, b)


if __name__ == "__main__":
    unittest.main()
