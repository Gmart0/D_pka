from unittest import TestCase
import Calculator


class TestCalculator(TestCase):

    def setUp(self):
        self.calculator = Calculator.Calculator()


class InputFileTest(TestCalculator):

    def test_read_file(self):
        with open("input.txt", "r") as file:
            program_input = file.read()

        self.calculator.read_file(program_input)
        self.assertEqual(self.calculator.newline, "5 7 - 1")
