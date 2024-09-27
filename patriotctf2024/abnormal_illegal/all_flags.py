from scapy.all import rdpcap, TCP

packets = rdpcap('./abnormal_illegal.pcapng')

fin_count = 0
syn_count = 0
rst_count = 0
psh_count = 0
ack_count = 0
urg_count = 0
ece_count = 0
cwr_count = 0


def count_tcp_flags(tcp_layer):
    global fin_count, syn_count, rst_count, psh_count, ack_count, urg_count, ece_count, cwr_count

    flags = tcp_layer.flags

    if flags & 0x01:  # FIN
        fin_count += 1
    if flags & 0x02:  # SYN
        syn_count += 1
    if flags & 0x04:  # RST
        rst_count += 1
    if flags & 0x08:  # PSH
        psh_count += 1
    if flags & 0x10:  # ACK
        ack_count += 1
    if flags & 0x20:  # URG
        urg_count += 1
    if flags & 0x40:  # ECE
        ece_count += 1
    if flags & 0x80:  # CWR
        cwr_count += 1


for packet in packets:
    if TCP in packet:
        tcp_layer = packet[TCP]
        count_tcp_flags(tcp_layer)

print(f"Number of packets with FIN flag: {fin_count}")
print(f"Number of packets with SYN flag: {syn_count}")
print(f"Number of packets with RST flag: {rst_count}")
print(f"Number of packets with PSH flag: {psh_count}")
print(f"Number of packets with ACK flag: {ack_count}")
print(f"Number of packets with URG flag: {urg_count}")
print(f"Number of packets with ECE flag: {ece_count}")
print(f"Number of packets with CWR flag: {cwr_count}")
