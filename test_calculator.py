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
        with open("null_file.txt", "r") as file:
            program_input = file.read()

        self.calculator.read_file(program_input)
        self.calculator.math_operations()
        self.assertEqual(self.calculator.answer, "0", "Null input gives incorrect result")


class OneNumberTest(TestCalculator):

    def test_one_number_input(self):
        with open("only_one_num.txt", "r") as file:
            program_input = file.read()

        self.calculator.read_file(program_input)
        self.calculator.math_operations()
        self.assertEqual(self.calculator.first_operand, "42", "incorrect result with only one number")


class CheckSecondNumberTest(TestCalculator):

    def test_check_second_num(self):
        with open("input.txt", "r") as file:
            program_input = file.read()

        self.calculator.read_file(program_input)
        self.calculator.math_operations()
        self.assertEqual(self.calculator.second_operand, "1263", "second operand doesn't match if existed")

    def test_check_second_num_not_existed(self):
        with open("only_one_num.txt", "r") as file:
            program_input = file.read()

        self.calculator.read_file(program_input)
        self.calculator.math_operations()
        self.assertEqual(self.calculator.second_operand, "", "second operand has displayed as existed when it can't")


class SubtractionTest(TestCalculator):

    def test_subtraction(self):
        with open("input_subtraction.txt", "r") as file:
            program_input = file.read()

        self.calculator.read_file(program_input)
        self.calculator.math_operations()
        self.assertEqual(self.calculator.answer, -3394, "subtraction isn't correct")


class SumTest(TestCalculator):

    def test_sum(self):
        with open("input_sum.txt", "r") as file:
            program_input = file.read()

        self.calculator.read_file(program_input)
        self.calculator.math_operations()
        self.assertEqual(self.calculator.answer, 70, "sum isn't correct")


class MultiplicationTest(TestCalculator):

    def test_multiplication(self):
        with open("input_multiplication.txt", "r") as file:
            program_input = file.read()

        self.calculator.read_file(program_input)
        self.calculator.math_operations()
        self.assertEqual(self.calculator.answer, 45, "multiplication isn't correct")


class DivisionTest(TestCalculator):

    def test_division(self):
        with open("input_division.txt", "r") as file:
            program_input = file.read()

        self.calculator.read_file(program_input)
        self.calculator.math_operations()
        self.assertEqual(self.calculator.answer, 33, "division isn't correct")

    def test_zero_division(self):
        with open("input_zero_division.txt", "r") as file:
            program_input = file.read()

        self.calculator.read_file(program_input)
        self.calculator.math_operations()
        self.assertEqual(self.calculator.answer, ZeroDivisionError, "division isn't correct")


class LastInputTest(TestCalculator):

    def test_last_input(self):
        with open("input_sum_without_equal.txt", "r") as file:
            program_input = file.read()

        self.calculator.read_file(program_input)
        self.calculator.math_operations()
        self.assertEqual(self.calculator.answer, "13", "second operator should be displayed")

    def test_first_symbol_and_equal(self):
        with open("one_num_and_operator.txt", "r") as file:
            program_input = file.read()

        self.calculator.read_file(program_input)
        self.calculator.math_operations()
        self.assertEqual(self.calculator.answer, "42", "first operator should be displayed")


class WriteFileTest(TestCalculator):
    def test_write_file(self):
        with open("input_division.txt", "r") as file:
            program_input = file.read()

        self.calculator.read_file(program_input)
        self.calculator.math_operations()
        self.calculator.print_to_file()
        with open("output.txt") as file:
            content = file.read()

        self.assertEqual(content, "33", "file output does not match")
