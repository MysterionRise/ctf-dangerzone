import matplotlib.pyplot as plt

x_positions = []
y_positions = []

writing = False

uniq = set()

with open('output.txt', 'r') as file:
    for line in file:
        line = line.strip()
        click = int(bytearray.fromhex(line[0:4]).hex(), 16)
        uniq.add(click)
        # TODO didn't work for some reason
        if click == 256:
            writing = True
        elif click == 0:
            writing = False
        x = int(bytearray.fromhex(line[4:8])[::-1].hex(), 16)
        y = int(bytearray.fromhex(line[8:12])[::-1].hex(), 16)
        # if writing:
        x_positions.append(x)
        y_positions.append(y)

print(uniq)
plt.figure(figsize=(12, 10))
plt.plot(x_positions, y_positions, marker='o', linewidth=0.1,
         markersize=0.5)

plt.title('Mouse Absolute Position Plot')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.grid(True)
plt.gca().invert_yaxis()
plt.show()
