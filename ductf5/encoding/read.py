class CCIR476:
    def __init__(self):
        self.CCIR_MODE = True  # True for Letters, False for Figures
        self.OLD_MODE = True

    def Decode(self, CCIR, Mode=None):
        if Mode is None:
            Mode = self.CCIR_MODE

        if CCIR == 0x78: return chr(13)  # CR
        if CCIR == 0x6C: return chr(10)  # LF
        if CCIR == 0x5C: return chr(32)  # SP
        if CCIR in [0x0F, 0x33, 0x66]: return chr(0)  # ALPHA, BETA, REP
        if CCIR == 0x5A:
            self.CCIR_MODE = True
            return chr(0)  # Autoset Mode = Letters
        if CCIR == 0x36:
            self.CCIR_MODE = False
            return chr(0)  # Autoset Mode = Figures

        if Mode:
            letters = {
                0x47: 'A', 0x72: 'B', 0x1D: 'C', 0x53: 'D', 0x56: 'E',
                0x1B: 'F', 0x35: 'G', 0x69: 'H', 0x4D: 'I', 0x17: 'J',
                0x1E: 'K', 0x65: 'L', 0x39: 'M', 0x59: 'N', 0x71: 'O',
                0x2D: 'P', 0x2E: 'Q', 0x55: 'R', 0x4B: 'S', 0x74: 'T',
                0x4E: 'U', 0x3C: 'V', 0x27: 'W', 0x3A: 'X', 0x2B: 'Y',
                0x63: 'Z'
            }
            return letters.get(CCIR, chr(0))
        else:
            figures = {
                0x2D: '0', 0x2E: '1', 0x27: '2', 0x56: '3', 0x55: '4',
                0x74: '5', 0x2B: '6', 0x4E: '7', 0x4D: '8', 0x71: '9',
                0x4B: "'", 0x1B: '!', 0x1D: ':', 0x1E: '(', 0x35: '&',
                0x39: '.', 0x3A: '/', 0x3C: '=', 0x47: '-', 0x53: '$',
                0x59: ',', 0x63: '+', 0x65: ')', 0x69: '#', 0x72: '?'
            }
            return figures.get(CCIR, chr(0))

    def isLetter(self, c):
        if c not in [chr(10), chr(13), chr(32)]:
            return 65 <= ord(c) <= 90
        return False

    def getMode(self):
        return self.CCIR_MODE

    def setMode(self, NewMode):
        self.CCIR_MODE = NewMode
        return True

    def ModeChanged(self):
        if self.CCIR_MODE != self.OLD_MODE:
            self.OLD_MODE = self.CCIR_MODE
            return True
        return False


ccir = CCIR476()


def split_into_chunks(bin_str):
    return [bin_str[i:i + 7] for i in range(0, len(bin_str), 7)]

def binary_to_decimal(binary):
    return int(binary, 2)


encoded_string = "101101001101101101001110100110110101110100110100101101101010110101110010110100101110100111001101100101101101101000111100011110011011010101011001011101101010010111011100100011110101010110110101011010111001011010110100101101101010110101101011001011010011101110001101100101110101101010110011011100001101101101101010101101101000111010110110010111010110101100101100110111101000101011101110001101101101001010111001011101110001010111001011100011011"

chunks = split_into_chunks(encoded_string)

decoded_message = ""

for chunk in chunks:
    decimal = binary_to_decimal(chunk)
    decoded_char = ccir.Decode(decimal)
    if decoded_char != chr(0):
        decoded_message += decoded_char


print(decoded_message)

