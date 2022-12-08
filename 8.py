def up(i,j,line):
    value = line[j]
    if i==0 or i ==len(line) or j ==0 or j == len(line):
        return 1
    while i !=0:
        if value > file[i-1][j]:
            i -= 1
        else:
            return 0
    return 1
def down(i,j,line):
    value = line[j]
    if i==0 or i ==len(line) or j ==0 or j == len(line):
        return 1
    while i !=(len(file)-1):
        if value > file[i+1][j]:
            i += 1
        else:
            return 0
    return 1
def left(i,j,line):
    value = line[j]
    if i==0 or i ==len(line) or j ==0 or j == len(line):
        return 1
    while j !=0:
        if value > file[i][j-1]:
            j -= 1
        else:
            return 0
    return 1
def right(i,j,line):
    value = line[j]
    if i==0 or i ==len(line) or j ==0 or j == len(line):
        return 1
    while j !=(len(line)-1):
        if value > file[i][j+1]:
            j += 1
        else:
            return 0
    return 1

def up_part2(i,j,line):
    distance =0
    value = line[j]
    if i==0 or i ==len(line) or j ==0 or j == len(line):
        return distance
    while i !=0:
        if value >file[i-1][j]:
            distance +=1
            i -= 1
        else:
            distance +=1
            return distance
    return distance
def down_part2(i,j,line):
    distance =0
    value = line[j]
    if i==0 or i ==len(line) or j ==0 or j == len(line):
        return distance
    while i !=(len(file)-1):
        if value > file[i+1][j]:
            distance += 1
            i += 1
        else:
            distance +=1
            return distance
    return distance
def left_part2(i,j,line):
    distance =0
    value = line[j]
    if i==0 or i ==len(line) or j ==0 or j == len(line):
        return distance
    while j !=0:
        if value > file[i][j-1]:
            distance += 1
            j -= 1
        else:
            distance +=1
            return distance
    return distance
def right_part2(i,j,line):
    distance =0
    value = line[j]
    if i==0 or i ==len(line) or j ==0 or j == len(line):
        return distance
    while j !=(len(line)-1):
        if value > file[i][j+1]:
            distance +=1
            j += 1
        else:
            distance +=1
            return distance
    return distance
max_scenic_score = 0    
file = open('input.txt','r').read()
file = [k for k in file.split("\n")]
visable=0
for i in range (len(file)):
    line = file[i]
    if i==0 or i == (len(file)-1):
        visable += len(line)
        continue
    else:
        visable +=2
    line = file[i]
    for j in range(1,len(line)-1):
        if up(i,j,line) or down(i,j,line) or left(i,j,line) or right(i,j,line) :
            visable +=1
        scenic_score = up_part2(i,j,line) * down_part2(i,j,line) * left_part2(i,j,line) * right_part2(i,j,line)
        if max_scenic_score < (scenic_score):
            print(line[j] +" " +str(i) +" "+ str(j) + " " + str(scenic_score))
            max_scenic_score = (scenic_score)
print(max_scenic_score)
print(visable) 
