import numpy as np
from PIL import Image

clock_emoji_to_digit = {
    '🕛': 0,
    '🕐': 1,
    '🕑': 2,
    '🕒': 3,
    '🕓': 4,
    '🕔': 5,
    '🕕': 6,
    '🕖': 7,
    '🕗': 8,
    '🕘': 9,
    '🕙': 10,
    '🕚': 11
}

commands = ['👉', '👈', '👆', '👇', '👍', '👎', '💬', '👂', '🫸', '🫷', '🔁']

image = Image.open('initial_state.png').convert('L')
image = image.resize((255, 255))
image = image.transpose(Image.FLIP_TOP_BOTTOM)
stack = np.array(image, dtype=np.uint8)

pointer_x = 0
pointer_y = 0
with open('program.txt', 'r', encoding='utf-8') as f:
    program = f.read()

instruction_list = []
instruction_positions = []
jump_stack = []
jump_map = {}

i = 0
program_length = len(program)
while i < program_length:
    char = program[i]
    if char in commands:
        if char == '🔁':
            i += 1
            number_digits = []
            while i < program_length and program[i] in clock_emoji_to_digit:
                number_digits.append(clock_emoji_to_digit[program[i]])
                i += 1
            # Convert digits to integer
            num = 0
            for digit in number_digits:
                num = num * 12 + digit
            # Append repeat instruction
            instruction_list.append(('REPEAT', num))
            instruction_positions.append(i)
        elif char == '🫸':
            instruction_list.append(char)
            instruction_positions.append(i)
            jump_stack.append(len(instruction_list) - 1)
            i += 1
        elif char == '🫷':
            if not jump_stack:
                print('Error: Unmatched 🫷 at position', i)
                exit(1)
            start = jump_stack.pop()
            end = len(instruction_list)
            instruction_list.append(char)
            instruction_positions.append(i)
            jump_map[start] = end
            jump_map[end] = start
            i += 1
        else:
            instruction_list.append(char)
            instruction_positions.append(i)
            i += 1
    else:
        i += 1

if jump_stack:
    print('Error: Unmatched 🫸 at positions',
          [instruction_positions[pos] for pos in jump_stack])
    exit(1)

pc = 0  # Program counter
output = ''
input_buffer = ''


def execute_instruction(instr):
    global pointer_x, pointer_y, stack, output, input_buffer
    if instr == '👉':
        pointer_x = (pointer_x + 1) % 255
    elif instr == '👈':
        pointer_x = (pointer_x - 1) % 255
    elif instr == '👆':
        pointer_y = (pointer_y - 1) % 255
    elif instr == '👇':
        pointer_y = (pointer_y + 1) % 255
    elif instr == '👍':
        stack[pointer_y, pointer_x] += 1  # In-place addition
    elif instr == '👎':
        stack[pointer_y, pointer_x] -= 1  # In-place subtraction
    elif instr == '💬':
        output += chr(stack[pointer_y, pointer_x])
    elif instr == '👂':
        if input_buffer == '':
            input_buffer = input('Input a character: ')
        if input_buffer:
            c = input_buffer[0]
            input_buffer = input_buffer[1:]
            stack[pointer_y, pointer_x] = ord(c)
        else:
            stack[pointer_y, pointer_x] = 0
    else:
        print(f'Error: Cannot execute instruction {instr}')


while pc < len(instruction_list):
    instr = instruction_list[pc]
    if instr in ['👉', '👈', '👆', '👇', '👍', '👎', '💬', '👂']:
        execute_instruction(instr)
        pc += 1
    elif instr == '🫸':
        if stack[pointer_y, pointer_x] == 0:
            pc = jump_map[pc] + 1
        else:
            pc += 1
    elif instr == '🫷':
        if stack[pointer_y, pointer_x] != 0:
            pc = jump_map[pc] + 1
        else:
            pc += 1
    elif isinstance(instr, tuple) and instr[0] == 'REPEAT':
        num = instr[1]
        if pc == 0:
            print('Error: REPEAT at the beginning of the program')
            pc += 1
        else:
            prev_instr = instruction_list[pc - 1]
            if isinstance(prev_instr, tuple) and prev_instr[0] == 'REPEAT':
                print('Error: Cannot repeat a REPEAT instruction')
                pc += 1
            else:
                for _ in range(num):
                    execute_instruction(prev_instr)
                pc += 1
    else:
        print(f'Error: Unknown instruction at pc={pc}: {instr}')
        pc += 1

print('Output:', output)

final_image = Image.fromarray(stack, mode='L')
final_image.save('final_stack.png')
print('Final stack state saved as final_stack.png')
