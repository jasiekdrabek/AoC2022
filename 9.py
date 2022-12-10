def is_adjacent(head,tail):
    posible_adjacent_position = [tail]
    for i in range(-1,2):
        for j in range(-1,2):
            posible_adjacent_position.append([tail[0] + i, tail[1] + j])
    if head in posible_adjacent_position:
        return True
    else:
        return False
                                             
def go_in_direction(element):
        if direction == "U":
            element[1] +=1
        if direction == "D":
            element[1] -=1    
        if direction == "R":
            element[0] +=1
        if direction == "L":
            element[0] -=1
        return element   
def check_which_diagonal(head,tail):
    for i in range(-1,2,2):
            for j in range(-1,2,2):
                t = [tail[0] + i, tail[1] + j]
                if is_adjacent(head,t):
                       return t
file = open('input.txt','r').read()
file = [k for k in file.split("\n")]
head = [0,0]
tail = [0,0]
knots = [[0,0] for i in range(10)]
visited = [[0,0]]
visited_part2 = [[0,0]]
for j in range (len(file)):
    direction, number = file[j].split(" ")
    for k in range (int(number)):
        #part1
        head = go_in_direction(head)
        if  is_adjacent(head,tail):
            continue
        if (head[0] == tail[0] and abs(head[1] - tail[1]) == 2) or (head[1] == tail[1] and abs(head[0] - tail[0]) == 2):
            tail = go_in_direction(tail)
        else:
            tail = check_which_diagonal(head,tail)
        if not (tail in visited):
            visited.append([tail[0],tail[1]])
for j in range (len(file)):
    direction, number = file[j].split(" ")
    for k in range (int(number)):            
        #part2   
        knots[0] = go_in_direction(knots[0])
        for i in range(len(knots)-1):
            #head = knots[i]
            #tail = knots[i + 1]
            if  is_adjacent(knots[i],knots[i + 1]):
                continue
            if (knots[i][0] == knots[i + 1][0] and abs(knots[i][1] - knots[i + 1][1]) == 2) or (knots[i][1] == knots[i + 1][1] and abs(knots[i][0] - knots[i + 1][0]) == 2):
                change = [(knots[i][0] - knots[i + 1][0])/2, (knots[i][1] - knots[i + 1][1])/2]
                knots[i + 1] = [knots[i + 1][0] + change[0],knots[i + 1][1] + change[1]]
            else:
                knots[i + 1] = check_which_diagonal(knots[i],knots[i + 1])
            if (not (knots[i + 1] in visited_part2)) and (i+1) == 9:
                visited_part2.append([knots[i + 1][0],knots[i + 1][1]])   
print(len(visited))
print(len(visited_part2))
