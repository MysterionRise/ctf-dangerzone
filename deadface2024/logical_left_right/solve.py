content = r'''\/\\/\/\ \///\/\/ \///\\// \///\/\\ \\/\\\\\ \//\\\\/ \\/\\\\\ \//\//\\ \//\/\\/ \///\/\\ \///\/\\ \//\//\\ \//\\/\/ \\/\\\\\ \///\\// \//\//// \//\//\/ \//\\/\/ \///\/\\ \//\/\\\ \//\/\\/ \//\///\ \//\\/// \\/\\\\\ \///\/\\ \//\//// \\/\\\\\ \//\\/// \//\\/\/ \///\/\\ \\/\\\\\ \///\\// \///\/\\ \//\\\\/ \///\\/\ \///\/\\ \//\\/\/ \//\\/\\ \\/\//\\ \\/\\\\\ \//\/\\\ \//\//// \///\\\\ \//\\/\/ \\/\\\\\ \////\\/ \//\//// \///\/\/ \\/\\\\\ \//\/\\\ \//\\\\/ \///\//\ \//\\/\/ \\/\\\\\ \//\\//\ \///\/\/ \//\///\ \\/\\\\\ \///\/\\ \//\/\\\ \//\/\\/ \///\\// \\/\\\\\ \////\\/ \//\\/\/ \//\\\\/ \///\\/\ \\/\\\\\ \/\/\/\\ \///\/\/ \///\\/\ \//\\\/\ \//\//// \\/\\\\\ \/\/\/\\ \//\\\\/ \//\\\// \//\/\// \////\\/ \\/\\\\/ \\/\\\\/ \\/\\\\/ \\/\\\\/ \\/\\\\\ \//\\//\ \//\//\\ \//\\\\/ \//\\/// \////\// \/\\/\\\ \\//\\// \/\//\\/ \/\//\\/ \\//\\\\ \/\/\/\/ \///\\/\ \/\\\//\ \\//\\\/ \/\\///\ \\//\/\\ \\//\\\/ \\//\\\/ \/\//\\/ \\//\/\\ \/\/\/// \\//\/\\ \/\\/\// \\//\\// \/////\/'''

strings = content.split()
message = ''
for s in strings:
    bits = ''
    for c in s:
        if c == '/':
            bits += '1'
        elif c == '\\':
            bits += '0'
    bits = bits.zfill(8)
    ascii_code = int(bits, 2)
    message += chr(ascii_code)

print(message)
