import re

def decode_doublehelix(encoded):
    encoded = ''.join(encoded.split())

    decode_dict = {
        "AT": "00",
        "CG": "01",
        "GC": "10",
        "TA": "11"
    }

    def replace_pair(match):
        pair = match.group(0).replace('-', '')
        return decode_dict.get(pair, '')

    binary = re.sub(r'([ATCG]-*){2}', replace_pair, encoded)


    return binary

# Example usage
encoded_code = """
G--C
A---T
 -- -C
  ----T
  G---- 
   G--- 
    A--T
     AT
     GC
     - A
   T--- 
  G- --C
 G ---C
T- --A
A-- T
A--T
  C
 TA
A- T
T- - 
A----T
 A----T
  T----A
   A --T
    G--C
     A 
     TA
    A -T
    --- 
  G- --C
 T----A
T ---A
 - -C
C-- 
  T
 CG
A- T

"""

decoded = decode_doublehelix(encoded_code)
print(decoded)