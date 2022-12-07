def resoult(oponent_play, my_response):
    if oponent_play == my_response:
        return 3
    if my_response == "rock" and oponent_play == "scissors":
        return 6
    if my_response == "rock" and oponent_play == "paper":
        return 0
    if my_response == "paper" and oponent_play == "rock":
        return 6
    if my_response == "paper" and oponent_play == "scissors":
        return 0
    if my_response =="scissors" and oponent_play == "paper":
        return 6
    if my_response =="scissors" and oponent_play == "rock":
        return 0

def resoult_part2(oponent_play, resoult):
    if oponent_play == "rock" and resoult == "X":
        return 3
    if oponent_play == "rock" and resoult == "Y":
        return 1
    if oponent_play == "rock" and resoult == "Z":
        return 2
    if oponent_play == "paper" and resoult == "X":
        return 1
    if oponent_play == "paper" and resoult == "Y":
        return 2
    if oponent_play == "paper" and resoult == "Z":
        return 3
    if oponent_play == "scissors" and resoult == "X":
        return 2
    if oponent_play == "scissors" and resoult == "Y":
        return 3
    if oponent_play == "scissors" and resoult == "Z":
        return 1
    
file = open('input.txt','r').read()
file = [k for k in file.split("\n")]
score = 0
score_part2 = 0
for i in range(len(file)):
    oponent_play, my_response = file[i].split(" ")
    if oponent_play == "A":
        oponent_play = "rock"
    if oponent_play == "B":
        oponent_play ="paper"
    if oponent_play == "C":
        oponent_play = "scissors"
    score_part2 += resoult_part2(oponent_play, my_response)    
    if my_response == "X":        
        my_response = "rock"
        score +=1
    if my_response == "Y":
        my_response = "paper"
        score_part2 +=3
        score +=2
    if my_response == "Z":
        my_response = "scissors"
        score_part2 +=6
        score +=3
    score += resoult(oponent_play, my_response)

print(score)
print(score_part2)

        
    
