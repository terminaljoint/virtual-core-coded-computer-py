class VirtualCPU:
    def __init__(self):
        # 1. Memory (RAM): 256 bytes of space initialized to 0
        self.memory = [0] * 256
        
        # 2. Registers: Internal CPU storage
        self.reg_A = 0      # Accumulator (used for math)
        self.reg_B = 0      # General purpose register
        
        # 3. Pointers
        self.pc = 0         # Program Counter (points to current instruction)
        
        # 4. Flags
        self.zero_flag = False  # Set to True if a math result is 0

    def load_program(self, program):
        """Loads a list of byte instructions into memory starting at address 0"""
        for i, byte in enumerate(program):
            self.memory[i] = byte

    def execute_instruction(self):
        """The Fetch-Decode-Execute Cycle"""
        # FETCH: Get the instruction code from memory
        opcode = self.memory[self.pc]
        
        # DECODE & EXECUTE
        if opcode == 0x00:    # HALT
            print("CPU Halted.")
            return False
            
        elif opcode == 0x01:  # LOAD_A [value] -> Loads a direct value into Register A
            self.reg_A = self.memory[self.pc + 1]
            self.pc += 2
            
        elif opcode == 0x02:  # LOAD_B [value] -> Loads a direct value into Register B
            self.reg_B = self.memory[self.pc + 1]
            self.pc += 2
            
        elif opcode == 0x03:  # ADD -> Adds Reg B to Reg A (ALU Operation)
            self.reg_A = self.reg_A + self.reg_B
            # Update flags
            self.zero_flag = (self.reg_A == 0)
            self.pc += 1
            
        elif opcode == 0x04:  # SUB -> Subtracts Reg B from Reg A (ALU Operation)
            self.reg_A = self.reg_A - self.reg_B
            self.zero_flag = (self.reg_A == 0)
            self.pc += 1
            
        elif opcode == 0x05:  # STORE_A [address] -> Saves Reg A value to RAM
            address = self.memory[self.pc + 1]
            self.memory[address] = self.reg_A
            self.pc += 2
            
        else:
            print(f"Unknown Opcode: {opcode}. Crashing.")
            return False
            
        return True

    def run(self):
        """Keep running instructions until a HALT command is found"""
        running = True
        while running:
            running = self.execute_instruction()
