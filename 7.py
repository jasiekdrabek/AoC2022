import copy
import itertools
from collections import defaultdict
def sum_all_int_values(dic):
    int_sum = {}
    for key in dic:
        if isinstance(dic[key], list):
            int_sum[key] = get_sum_from_list(dic[key], dic)
        elif isinstance(dic[key], int):
            int_sum[key] = dic[key]
        else:
            int_sum[key] = get_sum_from_list([dic[key]], dic)
    return int_sum


def get_sum_from_list(list_in, dic):
    int_sum = 0
    for val in list_in:
        if isinstance(val, int):
            int_sum += val
        else:
            if isinstance(val,list):
                int_sum += get_sum_from_list(val,dic)
            else:    
                int_sum += get_sum_from_list([dic[val]], dic)
    return int_sum
def get_name(name, dirs,i):
    name1 = name + str(i)
    while name1 in dirs:
        i+=1
        name1 = name + str(i)
    return name1    
def get_name_if_few_dir_in_row(dirs,dirs_with_the_same_name):
    lista = copy.deepcopy(dirs_with_the_same_name)
    for key, values in dirs.items():
        if key in lista:
            lista.remove(key)
    return lista[-1]        
file = open('input.txt','r').read()
file = [k for k in file.split("\n")]
dirs = {}
current_dir =""
dirs_with_the_same_name = []
for i in range (len(file)):
    file[i] = file[i].replace("$ ","")
    line = file[i].split(" ")
    
    size_or_command =line[0]
    if size_or_command == "ls":
        continue
    name = line[1]
    if name == "..":
        continue
    if size_or_command == "cd":
        if name not in dirs.keys():
            dirs[name] = []
        else:
            if name in dirs_with_the_same_name:
                name = get_name_if_few_dir_in_row(dirs,dirs_with_the_same_name)
            else:    
                name = get_name(name,dirs,0)
            dirs[name] =[]
        current_dir = name    
    if size_or_command == "dir":
        if name in dirs_with_the_same_name:
            name = get_name(name,dirs_with_the_same_name,0)
        dirs[current_dir].append(name)
        dirs_with_the_same_name.append(name)

    if size_or_command.isnumeric():
        dirs[current_dir].append(int(size_or_command))
dirs = sum_all_int_values(dirs)
'''
while any(isinstance(v,list) for k,v in dirs.items()):       
    for key, values in dirs.items(): 
          if not isinstance(values,list):
              continue
          if all(isinstance(item, int) for item in values):
              dirs[key] = sum(values)
          else:
              lista=[]
              suma = 0
              for item in values:
                  if isinstance(item,str):
                      lista.append(dirs[item])
                  if isinstance(item,int):
                      suma += item      
              integers = [x for x in lista if isinstance(x, int)]
              suma += sum(integers)
              no_integers = [x for x in lista if not isinstance(x, int)]
              lista = list(itertools.chain.from_iterable(no_integers))
              lista.append(suma)
              dirs[key] = lista
'''
print(dirs)

sum1 = 0
lista1 = []
for key, values in dirs.items():
    lista1.append(values)
    if dirs[key] <= 100000:
        sum1 += dirs[key]
lista1.sort()
print(sum1)
available = 70000000 - lista1[-1]
needed = 30000000 - available
print(min([x for x in lista1 if x >= needed]))
       
        
        
    
