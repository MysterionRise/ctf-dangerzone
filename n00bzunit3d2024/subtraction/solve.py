from pwn import *

server = remote('challs.n00bzunit3d.xyz', 10512)

numbers = server.recvline().strip().decode()
numbers_list = list(map(int, numbers.split()))

high = max(numbers_list) // 2

for _ in range(20):

    server.sendline(str(high).encode())
    numbers_list = [abs(high - num) for num in numbers_list]
    print(f"Current len of set is {len(set(numbers_list))}")
    if len(set(numbers_list)) < 10:
        print(set(numbers_list))
    if len(set(numbers_list)) == 1:
        print("Uniform list found with value:", numbers_list[0])
        flag = server.recvline().strip().decode()
        print("Flag:", flag)
        break

    high = max(numbers_list) // 2

server.close()
