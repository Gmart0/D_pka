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

    def test_null_input(self):
        with open("nullfile.txt", "r") as file:
            program_input = file.read()

        self.calculator.read_file(program_input)
        self.assertEqual(self.calculator.answer, "0", "Null input gives incorrect result")


class OneNumberTest(TestCalculator):

    def test_one_number_input(self):
        with open("only_one_num.txt", "r") as file:
            program_input = file.read()

        self.calculator.read_file(program_input)
        self.assertEqual(self.calculator.first_operand, "42", "incorrect result with only one number")


class CheckSecondNumberTest(TestCalculator):

    def test_check_second_num(self):
        with open("input.txt", "r") as file:
            program_input = file.read()

        self.calculator.read_file(program_input)
        self.assertEqual(self.calculator.second_operand, "1263", "second operand doesn't match if existed")

    def test_check_second_num_not_existed(self):
        with open("only_one_num.txt", "r") as file:
            program_input = file.read()

        self.calculator.read_file(program_input)
        self.assertEqual(self.calculator.second_operand, "", "second operand has displayed as existed when it can't")


class SubtractionTest(TestCalculator):

    def test_subtraction(self):
        with open("input_subtraction.txt", "r") as file:
            program_input = file.read()

        self.calculator.read_file(program_input)
        self.calculator.math_operations()
        self.assertEqual(self.calculator.answer, 3394, "subtraction isn't correct")

