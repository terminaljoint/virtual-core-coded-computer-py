class VirtualComputer:
    def __init__(self):
        # 256 bytes of RAM
        self.memory = [0] * 256

        # Registers
        self.reg_A = 0
        self.reg_B = 0
        self.pc = 0

        self.running = True

    def load_program(self, instructions):
        for i, bytecode in enumerate(instructions):
            self.memory[i] = bytecode

    def step(self):
        if not self.running:
            return

        # FETCH
        instruction = self.memory[self.pc]
        self.pc += 1

        # DECODE & EXECUTE

        # LOAD_A value
        if instruction == 0x01:
            self.reg_A = self.memory[self.pc]
            self.pc += 1

        # LOAD_B value
        elif instruction == 0x02:
            self.reg_B = self.memory[self.pc]
            self.pc += 1

        # ADD
        elif instruction == 0x03:
            self.reg_A = self.reg_A + self.reg_B

        # INPUT_A
        elif instruction == 0x04:
            self.reg_A = int(input("Enter a number: "))

        # OUTPUT_A
        elif instruction == 0x05:
            print(f"Output: {self.reg_A}")

        # HALT
        elif instruction == 0x00:
            self.running = False

        else:
            print(f"Unknown instruction: {instruction}")
            self.running = False

    def run(self):
        print("=== Virtual Computer Started ===")

        while self.running:
            self.step()

        print("=== Virtual Computer Halted ===")
        print(f"Register A = {self.reg_A}")
        print(f"Register B = {self.reg_B}")
        print(f"Program Counter = {self.pc}")


# -----------------------------
# PROGRAM
# -----------------------------
#
# INPUT_A
# LOAD_B 10
# ADD
# OUTPUT_A
# HALT
#
# Example:
# Input: 7
# Output: 17
#

program = [
    0x04,      # INPUT_A
    0x02, 10,  # LOAD_B 10
    0x03,      # ADD
    0x05,      # OUTPUT_A
    0x00       # HALT
]

vm = VirtualComputer()
vm.load_program(program)
#vm.run()
