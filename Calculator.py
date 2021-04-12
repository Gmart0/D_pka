class Calculator:

    def __init__(self):
        self.first_operand = 0
        self.second_operand = 0
        self.operator = ""
        self.newline = ""

    def read_file(self, program_input):
        self.parse(program_input)

    def parse(self, program_input):
        self.newline = program_input
        # return newline


