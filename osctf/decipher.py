from Crypto.Util.number import *
from sympy.ntheory.residue_ntheory import is_quad_residue

# Provided values
p = 96517490730367252566551196176049957092195411726055764912412605750547823858339
a = 1337

# Load the encrypted list
with open("cipher", "r") as f:
    encrypt = eval(f.read().strip())

# Decryption process
decrypted_bits = []

for value in encrypt:
    if is_quad_residue(value, p):
        decrypted_bits.append('0')
    else:
        decrypted_bits.append('1')

# Convert bits back to a string
flag_binary = ''.join(decrypted_bits)
flag_long = int(flag_binary, 2)
flag_bytes = long_to_bytes(flag_long)

print(flag_bytes)
