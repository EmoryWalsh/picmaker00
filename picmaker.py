f = open("img.ppm", "w")

f.write("P3\n500 500\n255\n")


b = 0

for y in range(500):
    for x in range(500):
        #eyes
        if((y > 80 and y < 120) and ((x > 190 and x < 230) or (x > 270 and x < 310))):
            f.write("255 255 255 ")
        #mouth
        elif((y > 140 and y < 150) and (x > 200 and x < 300)):
            f.write("242 158 109 ")
        #head
        elif(y >= 40 and y <= 180) and (x >= 150 and x <= 350):
            f.write("141 145 142 ")
        #neck
        elif((y >= 180 and y <= 230) and (x > 210 and x < 290)):
            f.write("141 145 142 ")
        #body
        elif((y > 230 and y < 370) and (x > 170 and x < 320)):
            f.write("141 145 142 ")
        #arms
        elif((y > 250 and y < 290) and ((x > 120 and x <= 170) or (x >= 320 and x < 370))):
            f.write("141 145 142 ")
        elif((y > 250 and y < 340) and ((x > 80 and x <= 120) or (x >= 370 and x < 410))):
            f.write("141 145 142 ")
        #legs
        elif((y >= 370 and y < 460) and ((x > 190 and x < 230) or (x > 260 and x < 300))):
            f.write("141 145 142 ")
        else:
            f.write("0 0 " + str(int(b)) + " ")
    if(y < 250):
        b = b + 1
    else:
        b = b - 1
    f.write("\n")


f.close()
