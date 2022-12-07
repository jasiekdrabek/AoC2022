file = open('input.txt','r').read()
file = [k for k in file.split("\n")]
priority_sum = 0
priority_sum_part2 = 0
for i in range (len(file)):
    priority = 0    
    line = file[i]
    compartments_1 = line[0: int(len(line)/2)]
    compartments_2 = line[int(len(line)/2): len(line)]
    for j in range (len(compartments_1)):
        if compartments_1[j] in compartments_2:
            priority = ord(compartments_1[j].swapcase()) - 64
            if priority > 26 :
                priority -= 6
    priority_sum += priority

for i in range (0,len(file),3):
    priority_part2 = 0
    common_letter = ""
    rucksack_1 = file[i]
    rucksack_2 = file[i+1]
    rucksack_3 = file[i+2]    
    for j in range(len(rucksack_1)):
        if  rucksack_1[j] in rucksack_2:            
            common_letter += rucksack_1[j]
             
    for j in range(len(common_letter)):
        if common_letter[j] in rucksack_3:
            priority_part2 = ord(common_letter[j].swapcase()) - 64
            if priority_part2 > 26 :
                priority_part2 -= 6
    priority_sum_part2 +=  priority_part2                
print(priority_sum)
print(priority_sum_part2) 
