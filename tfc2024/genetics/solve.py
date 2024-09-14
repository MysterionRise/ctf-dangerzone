def dna_to_ascii(dna_sequence):
    mapping = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}
    dna_sequence = dna_sequence.replace(" ", "").replace("\n", "")
    binary_sequence = ''.join(mapping[base] for base in dna_sequence)

    def binary_to_ascii(binary_str):
        return ''.join(chr(int(binary_str[i:i + 8], 2)) for i in
                       range(0, len(binary_str), 8))

    return binary_to_ascii(binary_sequence)


dna_sequence = """
CCCA CACG CAAT CAAT CCCA CACG CTGT ATAC CCTT CTCT ATAC CGTA CGTA CCTT CGCT ATAT CTCA CCTT CTCA CGGA ATAC CTAT CCTT ATCA CTAT CCTT ATCA CCTT CTCA ATCA CTCA CTCA ATAA ATAA CCTT CCCG ATAT CTAG CTGC CCTT CTAT ATAA ATAA CGTG CTTC
"""

decoded_message = dna_to_ascii(dna_sequence)
print(decoded_message)
