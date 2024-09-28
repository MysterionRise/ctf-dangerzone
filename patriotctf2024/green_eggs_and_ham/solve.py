import pyshark
import re


def extract_post_requests(pcap_file):
    display_filter = 'http.request.method == "POST" && tcp.len < 600'
    capture = pyshark.FileCapture(pcap_file, display_filter=display_filter)

    post_requests = []
    binaries = []
    for packet in capture:
        try:
            http_layer = packet.http
            request_path = http_layer.request_uri
            print(request_path)
            match = re.search(r"POST /(.{2})", "POST " + request_path)
            if match:
                hex_pair = match.group(1)

                binary_path = bin(int(hex_pair, 16))[2:].zfill(
                    8)
                post_requests.append(hex_pair[::-1])

                binaries.append(binary_path)
        except AttributeError:
            continue

    capture.close()
    print("".join(post_requests[::-1]))
    return binaries


pcap_file_path = 'exfil.pcap'
binaries = extract_post_requests(pcap_file_path)

print(" ".join(binaries))
