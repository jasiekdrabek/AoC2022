file = open('input.txt','r').read()
for i in range(len(file)-3):
    three_letters1 = [file[i], file[i+1],file[i+2]]
    three_letters2 = [file[i+3], file[i+1],file[i+2]]
    three_letters3 = [file[i], file[i+3],file[i+2]]
    three_letters4 = [file[i], file[i+1],file[i+3]]
    if file[i+3] not in three_letters1 and file[i]  not in three_letters2 and file[i+1] not in three_letters3 and file[i+2] not in three_letters4:
        print(str(i+4))
        break
for i in range(len(file)-13):
    fourteen_letters = [file[i], file[i+1], file[i+2], file[i+3], file[i+4], file[i+5], file[i+6], file[i+7], file[i+8], file[i+9], file[i+10], file[i+11], file[i+12], file[i+13]]
    for j in range(len(fourteen_letters)):
        check_letter = fourteen_letters[j]
        fourteen_letters.remove(fourteen_letters[j])
        if check_letter in fourteen_letters:
            break
        else:            
            fourteen_letters.insert(0,check_letter)
        if j == 13:
            print(str(i+14))
            
    
