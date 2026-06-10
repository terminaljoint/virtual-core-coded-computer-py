class VirtualComputer:
    def __init__(self):
        # 1. Initialize Memory (256 bytes of RAM initialized to 0)
        self.memory = [0] * 256

        # 2. Initialize Registers
        self.reg_A = 0  # General purpose register (Accumulator)
        self.reg_B = 0  # Second general purpose register
        self.pc = 0  # Program Counter (points to current instruction)

        self.running = True

    def load_program(self, instructions):
        """Loads a list of instructions into memory starting at address 0"""
        for i, bytecode in enumerate(instructions):
            self.memory[i] = bytecode

    def step(self):
        """The core Fetch-Decode-Execute cycle"""
        if not self.running:
            return

        # ---- FETCH ----
        instruction = self.memory[self.pc]
        self.pc += 1

        # ---- DECODE & EXECUTE ----
        if instruction == 0x01:  # LOAD_A (Load next value into Register A)
            value = self.memory[self.pc]
            self.reg_A = value
            self.pc += 1

        elif instruction == 0x02:  # LOAD_B (Load next value into Register B)
            value = self.memory[self.pc]
            self.reg_B = value
            self.pc += 1

        elif instruction == 0x03:  # ADD (Add Reg B to Reg A, store in Reg A)
            self.reg_A = self.reg_A + self.reg_B

        elif instruction == 0x00:  # HALT (Stop the computer)
            self.running = False

        else:
            print(f"Unknown instruction: {instruction}")
            self.running = False

    def run(self):
        """Keep executing instructions until the computer halts"""
        print("--- Computer Starting ---")
        while self.running:
            self.step()
        print("--- Computer Halted ---")
        print(f"Final State -> Register A: {self.reg_A}, Register B: {self.reg_B}, PC: {self.pc}")


# --- TEST OUR COMPUTER ---
if __name__ == "__main__":
    vm = VirtualComputer()

    # The global variable remains 'program'
    program = [
        0x01, 5,  # LOAD_A 5
        0x02, 10,  # LOAD_B 10
        0x03,  # ADD
        0x00  # HALT
    ]

    vm.load_program(program)
    vm.run()
