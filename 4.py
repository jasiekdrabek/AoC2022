file = open('input.txt','r').read()
file = [k for k in file.split("\n")]
overlap = 0
overlap_part2 = 0
for i in range(len(file)):
    elf1_range , elf2_range = file[i].split(",")
    elf1_low, elf1_high = elf1_range.split("-")
    elf2_low, elf2_high = elf2_range.split("-")
    elf1_low = int(elf1_low)
    elf2_low = int(elf2_low)
    elf1_high = int(elf1_high)
    elf2_high = int(elf2_high)
    if elf1_low <= elf2_low and elf1_high >= elf2_high:
        overlap += 1
    elif elf1_low >= elf2_low and elf1_high <= elf2_high:
        overlap += 1
    if elf1_low <= elf2_low and elf1_high >= elf2_low:
        overlap_part2 +=1
    elif elf2_low <= elf1_low and elf2_high >= elf1_low:
        overlap_part2 +=1
print(overlap)        
print(overlap_part2)
