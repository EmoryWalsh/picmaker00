f = open("img.ppm", "w")

f.write("P3\n500 500\n255")
r = 0
g = 0
b = 0
for x in range(500):
    f.write("\n")
    r = r +1
    for y in range(500):
        f.write(str(r % 255) + " " + str(g % 255) + " " + str(b % 255) + " ")

f.close()
