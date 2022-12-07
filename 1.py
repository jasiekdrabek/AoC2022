file = open('input.txt','r').read()
file = [k for k in file.split("\n")]
max_value = 0
max_list = [0,0,0]
one_inventory_value = 0
for i in range (len(file)):
    if file[i] == '' :
        if min(max_list) < one_inventory_value:
            max_list[max_list.index(min(max_list))] = one_inventory_value
        if max_value < one_inventory_value:
            max_value = one_inventory_value
        one_inventory_value = 0
    else:    
        one_inventory_value += int(file[i])
print(max_value)
print(max_list)
print(sum(max_list))
    
