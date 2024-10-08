from scapy.all import rdpcap, TCP
import re

pcap_file = 'unusualexfil.pcapng'
packets = rdpcap(pcap_file)
tcp_data = ""

for packet in packets:
    if TCP in packet and packet.haslayer('Raw'):
        tcp_data += packet['Raw'].load.decode(errors='ignore')

pattern = r'[RQ]+'

matches = re.findall(pattern, tcp_data)
full_str = ""

for match in matches:
    print(match)
    full_str += match

print(full_str)
