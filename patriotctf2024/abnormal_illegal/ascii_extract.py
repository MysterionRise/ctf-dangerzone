from scapy.all import rdpcap, TCP

pcap_file = 'abnormal_illegal.pcapng'
packets = rdpcap(pcap_file)


def is_fin_syn(tcp_layer):
    flags = tcp_layer.flags
    # SYN + FIN (illegal combination)
    if flags & 0x03 == 0x03:
        return True
    return False


def extract_flags(tcp_layer):
    flags = tcp_layer.flags
    rst = 1 if flags & 0x04 else 0
    psh = 1 if flags & 0x08 else 0
    return f"{psh}{rst}"


combined_binary_string = ''

for packet in packets:
    if TCP in packet:
        tcp_layer = packet[TCP]
        if is_fin_syn(tcp_layer):
            combined_binary_string += extract_flags(tcp_layer)


def binary_to_ascii(binary_string):
    ascii_text = ''
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i + 8]
        if len(byte) == 8:
            ascii_text += chr(int(byte, 2))
    return ascii_text


decoded_message = binary_to_ascii(combined_binary_string)

print(f"Combined Binary String: {combined_binary_string}")
print(f"Decoded Message: {decoded_message}")
