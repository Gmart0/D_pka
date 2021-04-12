class Calculator:

    def __init__(self):
        self.first_operand = ""
        self.second_operand = ""
        self.operator = ""
        self.newline = ""
        self.answer = ""

    def read_file(self, program_input):
        self.parse(program_input)

    def remove_spaces(self, program_input):
        return program_input.replace(" ", "")

    def parse(self, program_input):
        self.newline = self.remove_spaces(program_input)
        temp_line_1 = ""
        temp_line_2 = ""
        temp_operator = ""
        temp_operator2 = ""
        counter_splitter = 0
        if len(self.newline) != 0:
            for char in range(len(self.newline)):
                temp_line_1 += self.newline[char]
                counter_splitter += 1
                if not self.newline[char].isnumeric():
                    temp_operator += self.newline[char]
                    break
            if len(temp_operator) != 0:
                self.first_operand = temp_line_1[:-1]
            else:
                self.first_operand = temp_line_1
            # print("1 op =", self.first_operand)
            if len(self.newline) - counter_splitter != 0:
                for char in range(counter_splitter, len(self.newline)):
                    temp_line_2 += self.newline[char]
                    if not self.newline[char].isnumeric():
                        temp_operator2 += self.newline[char]
                        break
                if len(temp_operator2) != 0:
                    self.second_operand = temp_line_2[:-1]
                else:
                    self.second_operand = temp_line_2
                # print("2 op =", self.second_operand)
        else:
            self.answer = "0"

