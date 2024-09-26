import glob
import json

maps = {}

for file in glob.glob("*.json"):
    print(file)
    j = json.load(open(file))
    maps[file] = j

data = "PCTF{d)zn+d$+zqbb!t+h)!#+if+y)u+zi!l}."
output = ""

for map_from_name, map_from in maps.items():
    for map_to_name, map_to in maps.items():
        print(f"From: {map_from_name}, To: {map_to_name}")

        for c in data:
            scancode = map_from[c]

            for k, v in map_to.items():
                if v == scancode:
                    print(k, end="")

        print("\n")
