import copy
file = open('input.txt','r').read()
file = [k for k in file.split("\n")]
top_of_stacks =""
top_of_stacks_part2 = ""
stack ={
    "1" : "BVSNTCHQ",
    "2" : "WDBG",
    "3" : "FWRTSQB",
    "4" : "LGWSZJDN",
    "5" : "MPDVF",
    "6" : "FWJ",
    "7" : "LNQBJV",
    "8" : "GTRCJQSN",
    "9" : "JSQCWDM"
    }
stack2 = copy.deepcopy(stack)
for i in range (len(file)):
    from_stack_value =""
    to_stack_value=""
    line = file[i].split(" ")
    number_of_elements, from_stack, to_stack = line[1],line[3],line[5]
    number_of_elements = int(number_of_elements)    
    from_stack_value = stack[from_stack]
    to_stack_value = stack[to_stack]
    for i in range (int(number_of_elements)):
        from_stack_value, value = from_stack_value[0:-1],from_stack_value[-1]
        to_stack_value += value
    stack[from_stack] = from_stack_value
    stack[to_stack] = to_stack_value
for i in range (len(file)):
    from_stack_value =""
    to_stack_value=""
    value =""
    line = file[i].split(" ")
    number_of_elements, from_stack, to_stack = line[1],line[3],line[5]
    number_of_elements = int(number_of_elements)    
    from_stack_value = stack2[from_stack]
    to_stack_value = stack2[to_stack]
    for i in range (int(number_of_elements)):
        from_stack_value, x = from_stack_value[0:-1],from_stack_value[-1]
        value += x
    value = value[::-1]
    to_stack_value += value
    stack2[from_stack] = from_stack_value
    stack2[to_stack] = to_stack_value
for i in range (9):
    top_of_stacks += stack[str(i+1)][-1]
    top_of_stacks_part2 += stack2[str(i+1)][-1]
print(top_of_stacks)
print(top_of_stacks_part2)
