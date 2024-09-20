import base64

message = (
    "Mwahahaha you will nOcmu{9gtufever crack into my passMmQg8G0eCXWi3MY9QfZ0NjCrXhzJEj50fumttU0ympword, "
    "i'll even give you the key and the executable:::: Zfo5ibyl6t7WYtr2voUEZ0nSAJeWMcN3Qe3/+MLXoKL/p59K3jgV"
)


def extract_fourth(msg):
    pos_n = msg.find('n', msg.find('you will') + len('you will'))
    pos_ever = msg.find('ever', pos_n)
    part1 = msg[pos_n + 1: pos_ever]

    pos_pass = msg.find('pass')
    pos_word = msg.find('word', pos_pass)
    part2 = msg[pos_pass + len('pass'): pos_word]

    return part1 + part2


def reverse_flipflops(fourth):
    return ''.join(chr(ord(c) - 1) for c in fourth)


def solve_challenge():
    fourth = extract_fourth(message)
    print(f"Extracted 'fourth': {fourth}")
    third = reverse_flipflops(fourth)
    print(f"Reversed 'third': {third}")
    second = base64.b64decode(third)
    print(f"Decoded 'second': {second}")
    bittys_enc = message.split(':::: ')[1]
    print(f"Extracted 'bittysEnc': {bittys_enc}")
    bittys = base64.b64decode(bittys_enc)
    print(f"Decoded 'bittys': {bittys}")
    first = bytes(a ^ b for a, b in zip(second, bittys))
    print(f"Recovered 'first': {first.decode('utf-8')}")


solve_challenge()
