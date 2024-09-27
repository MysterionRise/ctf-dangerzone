from scapy.all import rdpcap, TCP

packets = rdpcap('./abnormal_illegal.pcapng')

rst_count = 0
psh_count = 0
ack_count = 0

def is_fin_syn(tcp_layer):
    flags = tcp_layer.flags
    # SYN + FIN (illegal combination)
    if flags & 0x03 == 0x03:
        return True
    return False

for packet in packets:
    if TCP in packet:
        tcp_layer = packet[TCP]
        if is_fin_syn(tcp_layer):
            if tcp_layer.flags & 0x04:  # RST flag
                rst_count += 1
            if tcp_layer.flags & 0x08:  # PSH flag
                psh_count += 1
            if tcp_layer.flags & 0x10:  # ACK flag
                ack_count += 1

print(f"Packets with FIN, SYN, RST flags: {rst_count}")
print(f"Packets with FIN, SYN, PSH flags: {psh_count}")
print(f"Packets with FIN, SYN, ACK flags: {ack_count}")