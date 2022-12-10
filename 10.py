def cycle_change_check(cycle):
    signals_strength = 0
    global cycle_check
    if cycle == cycle_check:
        signals_strength = x * cycle
        if cycle_check < 220:
            cycle_check += 40
    return signals_strength
def draw(cycle,sprite,image):
    cycle = cycle % 40
    cycle = cycle - 1
    if cycle in sprite:
        image.append("#")
    else:    
        image.append(".")
    return image    
file = open('input.txt','r').read()
file = [k for k in file.split("\n")]
cycle = 0
x = 1
signals_strength = 0
cycle_check =20
sprite = [0,1,2]
image = []
for i in range (len(file)):
    if file[i] == "noop":
        cycle += 1
        signals_strength += cycle_change_check(cycle)
        image = draw(cycle,sprite,image)
    else:
        cycle += 1
        signals_strength += cycle_change_check(cycle)
        image = draw(cycle,sprite,image)
        cycle += 1
        signals_strength += cycle_change_check(cycle)
        image = draw(cycle,sprite,image)
        line = file[i].split(" ")        
        x += int(line[1])
        for j in range(len(sprite)):
            sprite[j]+= int(line[1])
    
print(signals_strength)
print(image)
for i in range (6):
    row =""
    for j in range(40):
        row += str(image[(40 *i +j)])
    print(row)
