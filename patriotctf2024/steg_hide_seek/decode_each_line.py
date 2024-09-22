from base64 import b64decode

with open("decode", "r") as f:
    for _ in range(0, 1000):
        line = f.readline()
        # print(line[0:12])
        try:
            print(b64decode(line[0:12]).decode("latin-1"))
        except:
            print("base64 error")

