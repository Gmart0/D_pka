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
        self.assertEqual(self.calculator.newline, "4657-1263", "information form input file was not read correctly")


class NullInputTest(TestCalculator):

    def test_read_file(self):
        with open("nullfile.txt", "r") as file:
            program_input = file.read()

        self.calculator.read_file(program_input)
        self.assertEqual(self.calculator.answer, "0", "Null input gives incorrect result")


class OneNumberTest(TestCalculator):

    def test_read_file(self):
        with open("only_one_num.txt", "r") as file:
            program_input = file.read()

        self.calculator.read_file(program_input)
        self.assertEqual(self.calculator.first_operand, "42", "incorrect result with only one number")

