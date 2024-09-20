import socket
import base64


def decode_challenge(encoded_str, iterations):
    decoded_bytes = encoded_str
    for _ in range(iterations):
        decoded_bytes = base64.b64decode(decoded_bytes)
    return decoded_bytes.decode('utf-8')


def main():
    host = 'chal.pctf.competitivecyber.club'
    port = 9001
    total_challenges = 1000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s_file = s.makefile('rwb', buffering=0)

        challenge_count = 0

        while challenge_count < total_challenges:
            while True:
                line = s_file.readline().decode('utf-8').strip()
                if 'Challenge:' in line:
                    idx = line.find('Challenge:')
                    challenge_line = line[idx + len('Challenge:'):].strip()
                    break

            print(challenge_line)
            first_decode = base64.b64decode(challenge_line).decode('utf-8')
            encoded_part, n_str = first_decode.split('|')
            n = int(n_str)
            final_decode = decode_challenge(encoded_part, n)
            response = f"{final_decode}|{challenge_count}"
            s_file.write((response + '\n').encode('utf-8'))
            s_file.flush()

            challenge_count += 1

        final_message = s_file.read().decode('utf-8')
        print(final_message)


if __name__ == "__main__":
    main()
