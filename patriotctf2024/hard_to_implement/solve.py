import socket
import sys
import re

HOST = 'chal.competitivecyber.club'
PORT = 6001
BLOCK_SIZE = 16
MAX_ATTEMPTS = 1500

PRINTABLE_ASCII = (
    b'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    b'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
)
ALLOWED_BYTES = list(PRINTABLE_ASCII)

KNOWN_PREFIX = b"pctf{"


class ECBDecryptor:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = None
        self.flag = b""
        self.block_size = BLOCK_SIZE
        self.max_attempts = MAX_ATTEMPTS
        self.response_pattern = re.compile(rb'Response > ([0-9a-fA-F]+)')

    def connect(self):
        """Establish a TCP connection to the server."""
        self.sock = socket.create_connection((self.host, self.port))
        self.sock.settimeout(5)  # Set a timeout for socket operations
        print(f"Connected to {self.host}:{self.port}")

    def close(self):
        """Close the TCP connection."""
        if self.sock:
            self.sock.close()
            print("Connection closed.")

    def recv_until(self, delimiter):
        """
        Receive data from the socket until the delimiter is found.
        Returns all data received up to and including the delimiter.
        """
        data = b""
        while delimiter not in data:
            try:
                chunk = self.sock.recv(4096)
                if not chunk:
                    break
                data += chunk
            except socket.timeout:
                break
        return data

    def send_challenge(self, challenge):
        """
        Send a challenge to the server and receive the ciphertext.
        Extracts only the hexadecimal ciphertext from the response and converts it to bytes.
        """
        self.sock.sendall(challenge + b'\n')
        response = self.recv_until(b'Response > ')

        match = self.response_pattern.search(response)
        if match:
            ciphertext_hex = match.group(1)
            try:
                ciphertext = bytes.fromhex(ciphertext_hex.decode('utf-8'))
                return ciphertext
            except ValueError:
                print("Failed to convert ciphertext from hex.")
                return None
        else:
            print("Ciphertext not found in response.")
            return None

    def determine_block_size(self):
        """Determine the block size used by the cipher."""
        print("Determining block size...")
        initial_ciphertext = self.send_challenge(b"")
        if initial_ciphertext is None:
            print("Failed to retrieve initial ciphertext.")
            return
        initial_length = len(initial_ciphertext)

        for i in range(1, 33):
            payload = b"A" * i
            ciphertext = self.send_challenge(payload)
            if ciphertext is None:
                continue
            length = len(ciphertext)
            if length > initial_length:
                self.block_size = length - initial_length
                print(f"Determined block size: {self.block_size} bytes")
                return
        print(f"Assuming block size: {self.block_size} bytes")

    def is_ecb(self):
        """Check if the encryption mode is ECB by looking for repeated blocks."""
        print("Checking if ECB mode is used...")
        payload = b"A" * self.block_size * 4  # Increase repetition for reliability
        ciphertext = self.send_challenge(payload)
        if ciphertext is None:
            print("Failed to retrieve ciphertext for ECB check.")
            return False
        # Split ciphertext into blocks
        blocks = [ciphertext[i:i + self.block_size] for i in
                  range(0, len(ciphertext), self.block_size)]
        unique_blocks = set(blocks)
        if len(unique_blocks) < len(blocks):
            print("ECB mode detected.")
            return True
        else:
            print("ECB mode not detected.")
            return False

    def byte_at_a_time_ecb_decrypt(self):
        """Perform the byte-at-a-time ECB decryption to recover the flag."""
        print("Starting byte-at-a-time ECB decryption...")
        known_bytes = KNOWN_PREFIX
        print(f"Starting with known prefix: {known_bytes.decode()}")

        # Calculate remaining attempts
        remaining_attempts = self.max_attempts

        for i in range(len(KNOWN_PREFIX), self.max_attempts):
            block_index = len(known_bytes) // self.block_size
            pad_length = self.block_size - (
                    len(known_bytes) % self.block_size) - 1
            padding = b"A" * pad_length
            ciphertext = self.send_challenge(padding)
            if ciphertext is None:
                print(
                    "\nCiphertext not found. Possibly reached the end of the flag.")
                break

            start = block_index * self.block_size
            end = (block_index + 1) * self.block_size
            target_block = ciphertext[start:end]

            dictionary = {}
            for b in ALLOWED_BYTES:
                test_input = padding + known_bytes + bytes([b])
                test_cipher = self.send_challenge(test_input)
                if test_cipher is None:
                    continue
                test_block = test_cipher[0:self.block_size]
                dictionary[test_block] = bytes([b])

            if target_block in dictionary:
                next_byte = dictionary[target_block]
                known_bytes += next_byte

                if known_bytes.endswith(b"}"):
                    print(f"\nFlag found: {known_bytes.decode()}")
                    return known_bytes.decode()

                sys.stdout.write(
                    f"\rRecovered so far: {known_bytes.decode(errors='ignore')}")
                sys.stdout.flush()
            else:
                print(
                    "\nNo matching block found. Possibly reached the end of the flag.")
                break

            remaining_attempts -= (len(ALLOWED_BYTES))
            if remaining_attempts <= 0:
                print("\nReached the maximum number of attempts.")
                break

        return known_bytes.decode(errors='ignore')


def main():
    decryptor = ECBDecryptor(HOST, PORT)
    try:
        decryptor.connect()
        initial_data = decryptor.recv_until(b'Send challenge > ')
        print(initial_data.decode())
        decryptor.determine_block_size()

        if not decryptor.is_ecb():
            print("Not ECB mode. Exiting.")
            return

        flag = decryptor.byte_at_a_time_ecb_decrypt()
        print(f"\nRecovered Flag: {flag}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        decryptor.close()


if __name__ == "__main__":
    main()
