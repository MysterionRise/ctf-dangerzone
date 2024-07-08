from pwn import *
import binascii

conn = remote('2024.ductf.dev', 30020)

def send_ct(ct):
    conn.sendlineafter(b'ct: ', ct.encode())
    return conn.recvline().strip().decode()


known_plaintext = "print('test')"
ct_known = binascii.hexlify(known_plaintext.encode()).decode()
response = send_ct(ct_known)

if response == 'test':
    print("Successfully connected and executed test command.")
else:
    print("Error: Unexpected response for test command.")
    print(response)
    exit(1)


payload = "print(FLAG)"


xored = bytes(a ^ b for a, b in zip(payload.encode(), known_plaintext.encode()))


new_ct = binascii.hexlify(xored).decode()


flag = send_ct(new_ct)

print(f"Flag: {flag}")

conn.close()