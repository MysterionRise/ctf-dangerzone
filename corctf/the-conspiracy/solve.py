from scapy.all import rdpcap, IP, TCP, Raw


def decrypt(encrypted_message, keys):
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        original_ascii = encrypted_message[i] // keys[i]
        decrypted_message += chr(original_ascii)
    return decrypted_message


packets = rdpcap('challenge.pcap')

encrypted_messages = []
keys_list = []

for packet in packets:
    if Raw in packet:
        data = packet[Raw].load
        try:
            data_list = eval(data.decode(errors='ignore'))
            if all(isinstance(x, int) for x in data_list):
                if len(data_list) > 0 and data_list[0] > 100:
                    encrypted_messages.append(data_list)
                else:
                    keys_list.append(data_list)
        except:
            continue

messages_and_keys = list(zip(encrypted_messages, keys_list))
decrypted_messages = [decrypt(message, keys) for message, keys in
                      messages_and_keys]

for decrypted_message in decrypted_messages:
    print(decrypted_message)
