# A simplifier et implémenter
# (c'est un compteur qui compte de bas en haut et de gauche à droite)

lvl = "00000:00000:00000:99999:99999"
count = 10

print(lvl)
print(count)

def add():
    global lvl, count

    split = lvl.split(":")
    output = []
    done = False
    # print(f"\033[94m{list(reversed(split))}\033[0m")
    for i in list(reversed(split)):
        if "0" in i and not done:
            # lvl = lvl.replace("0", "9", 1)
            output.append(i.replace("0", "9", 1))
            if count < 25:
                count += 1
            done = True
        else:
            output.append(i)

    lvl = ":".join(list(reversed(output)))

    print(lvl)
    print(count)

def remove():
    global lvl, count

    split = lvl.split(":")
    output = []
    done = False

    for i in list(split):
        if "9" in i and not done:
            # lvl = lvl.replace("9", "0", 1)
            output.append(i[::-1].replace("9", "0", 1)[::-1])
            if count > 0:
                count -= 1
            done = True
        else:
            output.append(i)

    lvl = ":".join(list(output))

    print(lvl)
    print(count)

add()
add()
add()
add()
add()
add()
add()
print("-----")
remove()
remove()
remove()
