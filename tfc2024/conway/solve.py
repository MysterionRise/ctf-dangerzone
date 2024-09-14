import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def generate_next_key(s):
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(str(count) + s[i - 1])
            count = 1
    result.append(str(count) + s[-1])
    return ''.join(result)

initial = '11131221131211131231121113112221121321132132211331222113112211'
first_pass = generate_next_key(initial)
second_pass = generate_next_key(first_pass)
print(second_pass)

h = hashlib.sha256()
h.update(second_pass.encode())
key = h.digest()

ciphertext = 'f143845f3c4d9ad024ac8f76592352127651ff4d8c35e48ca9337422a0d7f20ec0c2baf530695c150efff20bbc17ca4c'
cipher = AES.new(key, AES.MODE_ECB)
padded_plaintext = cipher.decrypt(bytes.fromhex(ciphertext))
plaintext = unpad(padded_plaintext, 16)

print("Decrypted flag:", plaintext.decode())
