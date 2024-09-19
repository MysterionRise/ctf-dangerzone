import base64

ciphertext_b64 = 'QRVWUFdWEUpdXEVGCF8DVEoYEEIBBlEAE0dQAURFD1I='
encrypted_data = base64.b64decode(ciphertext_b64)

srt_key = 'secretkey'
key_length = len(srt_key)

half_length = len(encrypted_data) // 2
usr_input_chars = [''] * half_length
rsv_input_chars = [''] * half_length

for i in range(half_length):
    enc_p1 = encrypted_data[2 * i]
    enc_p2 = encrypted_data[2 * i + 1]
    key_char = ord(srt_key[i % key_length])

    c1 = enc_p1 ^ key_char
    c2 = enc_p2 ^ key_char

    usr_input_chars[i] = chr(c1)
    rsv_input_chars[i] = chr(c2)

usr_input = ''.join(usr_input_chars + rsv_input_chars[::-1])

print(f"pctf{{{usr_input}}}")
