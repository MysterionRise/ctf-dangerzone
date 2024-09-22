import re

# The provided keypress data
log = """
999F4F4[ESC][ESC]vF9[[[eeeF12F12222447000↓↓↓↓F5tttF7F7F7wwccF9yyyfF12F12F12;;;222iii5l[CAPSLOCK]o→F3
rF5     taF7=wdF10',"|g'3j.6m[CAPSLOCK][CAPSLOCK]9o←F3[ESC]rF6F6  bbF8F8F8xxxe##111''j7F1ppF4ssvvF9[eeF12#25k/88F2qq↓F5F5ttF7-ccF10z;366[CAPSLOCK]ooo→→F3F3F3

↑↑↑F6F6uuuaaF8F8F8=xxxdd',"|',"|11gg33jj.m9ppF4F4[ESC]  vvF8[[xF11F11##114444444444444444444444kkkkkkkkkkkkkkkkkkkkkkkkkk44444444444444444444kkkkkkkk44444444kk44h1#F11ex[F8F8bb  F6F6ss[ESC][ESC][ESC]F4F4F4←←←←←←←←←←←←←←←←F4F4F4F4F4F4[ESC][ESC][ESC][ESC]ssF6F6 vvbF8F8[xeeF11#1h4kk4h#F11exxF8bv  F6s[ESC]←p9F1m.j3'gg1',"|F10x=F8F8auu    F6F6↑↑↑F6       uuaF8==xdF10F10',"|',"|1g''3jj..6666mmmmmm66...j33'g1',"|F10dx==F8uuu           F6F6↑↑↑rr

F3F3→→→→ooo888888[CAPSLOCK][CAPSLOCK][CAPSLOCK][CAPSLOCK]ll666,,,,,,,,,,,,,,,6666666llllllllllllllllllllllllllllllllll[CAPSLOCK][CAPSLOCK][CAPSLOCK][CAPSLOCK]oooo→→→→→→→→→→F3F3


rrrr
F3→o8[CAPSLOCK]l66i3;fz]F10cw------------ccccccccccccccccccwwwww-------------F7F7F7F7F7F7F5F5↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓qqqqqqqqF2F2F2F2F2F2F2F2n8/kk5h2#F12ee[[F9F9[[eF12#225k//88nnF2F2
qq
F2n8/k5h2#F12eeeyy[[cvv-F4↓ppF1mmF4F4F4↓p00F1F1F10p↓F4↓pp000000pp↓↓F4ssF4F4↓pp0F1F1mm77..jj44''111###F11F11F11F11F11###11111hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh11##F11ex[F8F8bbuu F6F6F6rrrrrrrrF6F6 uubF8[xeF11#111hh1##F11ex[F8F8bb F6[ESC][ESC]F3←←o9[CAPSLOCK]m6.j3'gggzz',"|',"|',"|F10F10F10F10F10F10F10',"|',"|',"|',"|',"|',"|',"|',"|',"|',"|',"|',"|',"|',"|',"|',"|',"|',"|F10F10F10F10F10dw=F7F7aat    F5↑r
F3→o88[CAPSLOCK]88oo→→F3F3
rr↑↑F5F5                ttaaaF7===wdw=F7at    F5↑r
F3→oo8[CAPSLOCK]l55,5555llll555555,i2;F12fy]F9cw-F7F5↓q000F2F27777////////////777777777777777777777777777777//////////////////////////////7nnnnn777/k44hh2##F12F12eeeyyy[[[F9F9F9F9F9F9F9F9[yeF12#2hhh444kkk44h2#F12F12eeyyF9bvvss[ESC][ESC][ESC]←←←F4[ESC][ESC][ESC]sss[ESC][ESC]F4F4←p9F1F1F1999ppF1mm7.jjj4444444''''''''''''''''''''''''''''44jjjjjjjjjjjjjjjjjjjjjjjjjjjjjj44444444444'''''gg1111F11F11F11F11ddddxxxx======F8F8F8bbuuuuuu                                     F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6F6↑↑↑↑↑r[ESC]F3F3←o8[CAPSLOCK]lll555,,,,,,55555lllllllllll[CAPSLOCK][CAPSLOCK][CAPSLOCK][CAPSLOCK][CAPSLOCK][CAPSLOCK][CAPSLOCK]8888888888888888888888ooooo8[CAPSLOCK]l5,,i2;F12fffffzzzzz]]]]]]]]F9F9F9F9ccc----F7F7--wcF9]zzfffz]F9cw-F7F5↓qq000F2F2F2nnnnn7777///////kkkkk55555555hhhh22##########F12F12F12F12F12F12F12##22hh555kkkk5h2#F12eyyy[[[F9F9bbbvvv    sss[ESC][ESC][ESC]F4F4←←ppp00F1F1F1F100pp←←F4F4[ESC][ESC]ssss[ESC]F4←p0F1F1m777.jj44'''g11',"|F11dx=F8bbu  F6↑↑↑F6 ubF8=xddF11F11',"|',"|11ggg444444jjjjjjjjjjjjjjjjjjjjj44444444444''''''''g11',"|F11dx==F8F8F8bbbuu   F6F6F6↑↑↑↑rrr[ESC][ESC][ESC]F3F3←←←o99[CAPSLOCK][CAPSLOCK]6,,33;;;33,,66[CAPSLOCK][CAPSLOCK]9ooo9[CAPSLOCK][CAPSLOCK]ll666ii33;;ggz',"|F10F10dw=F7at        F5↑q
F2→n8/ll55,iii2222222;;;F12F12F12F12F12F12F12F12F12F12F12F12F12F12F12F12F12F12fffyyy]]]]F9F9F9ccvvvvvv-sF4F4F4↓↓↓qq0000F2F2F2nnn777kkk444h1#F11exxxeeeF11F11####111hhhh1#F11eex[[F8F8F8F8[eeeF11F11##11hhh1#F11ex[F8bvvv ss[ESC]F4F4←←pp9F1mm.jjjj333''''''''''33333jj...66mmmmmm66..j3''33j..66666mmmmmmm666..jjj333333333j..6mmF19p←F4[ESC]s vb[e#1k7nF20q↓F4F4svc]fF12;22,l/nF2
q↑F5ta=dF10',"|;3,[CAPSLOCK]o←F3rF6 bF8=dF11147mF1p←F4svF9yeF12#h5k/n0F5tF7wzF12F12;i5l8F3F6ubF8=dF11',"|g'j.77F19p←F4[ESC][ESC]s vv[yeF12#2hh4k/77nF2F2q↓tF7F7--cF9]y;;22ii,555l[CAPSLOCK][CAPSLOCK]8→→F3

F5F5            aaaF7===wdddF10F10zzgg'''j...669999oo←←←F3F3[ESC][ESC]F6F6  b[[[xxxeeF11F11##11hhhhhhh111111###F11F11F11F11F11F11F11F11##11h44kk/7nnF1F100qq↓↓↓↓↓↓↓↓↓F4F4F4F4F4F4F4F4F4F4F4F4F4F4F4F4F4F4qqqqqq00000000nnnnnn/////////////////////////77777nnnnnF1F1F1F10000000000000000000000000000F1F1F1F1F1F1nn77/k4h1#F11exx[F8F8F8[[xeF11##11h44k/7nnF10qq
"""


# Step 1: Split the log into tokens
tokens = re.findall(r'\[.*?\]|F\d+|.', log)

# Initialize variables
text = []
cursor = 0
capslock = False

# Function to handle insertion at the current cursor position
def insert_char(char, cursor, text, capslock):
    if capslock and char.isalpha():
        char = char.upper()
    elif not capslock and char.isalpha():
        char = char.lower()
    text.insert(cursor, char)
    return cursor + 1

# Step 2: Process each token
for token in tokens:
    if token == '[CAPSLOCK]':
        capslock = not capslock
    elif token == '[ESC]':
        continue  # Ignoring [ESC] as it's likely not part of the flag
    elif re.match(r'F\d+', token):
        continue  # Ignoring function keys unless needed
    elif token in ['←', '→', '↑', '↓']:
        if token == '←':
            cursor = max(cursor - 1, 0)
        elif token == '→':
            cursor = min(cursor + 1, len(text))
        # Ignoring up and down arrows for simplicity
    else:
        cursor = insert_char(token, cursor, text, capslock)

# Step 3: Reconstruct the final text
final_text = ''.join(text)
print("Reconstructed Text:")
print(final_text)

# Step 4: Search for the flag
flag_match = re.search(r'PCTF\{.*?\}', final_text)
if flag_match:
    print(f"\nFlag Found: {flag_match.group(0)}")
else:
    print("\nFlag not found in the reconstructed text.")