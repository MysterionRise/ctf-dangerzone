z = '11 3 15 12 95 89 9 52 36 61 37 54 34 90 15 86 38 26 80 19 1 60 12 38 49 9 28 38 0 81 9 2 80 52 28 19'


def revert_to_valueA1(Z):
    def reverse_forensics(forensics_output):
        # Convert space-separated ASCII values back to characters
        return ''.join(chr(int(x)) for x in forensics_output.split())

    def reverse_doThing(encoded, key):
        return ''.join(chr(ord(a) ^ ord(b)) for a, b in
                       zip(encoded, key * (len(encoded) // len(key) + 1)))


    O = reverse_forensics(Z)
    print(O)

    S = "Mon"
    G = "key"
    D = "Ma"
    F = "gic"
    W = S + G + D + F

    Q = reverse_doThing(O, W)
    print(Q)

    valueA1 = Q[6:]

    return valueA1

result = revert_to_valueA1(z)
print(result)

# DUCTF{M4d3_W1th_AI_by_M0nk3ys}