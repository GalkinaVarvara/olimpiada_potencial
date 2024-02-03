import csv
with open('game.csv',encoding='utf-8') as f:
    reader = csv.reader(f,delimiter='$')
    ans = list(reader)
    game_name = []
    count_bags = []
    for i in range(1,len(ans)):
        if ans[i][0] not in game_name:
            game_name.append(ans[i][0])
            count_bags.append(0)
        count_bags[game_name.index(ans[i][0])]+=1
    answer = []
    for i in range(0,len(game_name)):
        answer.append([game_name[i],count_bags[i]])
    answer.sort()
    k=1
    for i in range(len(answer)):
        print(f"Игра {k} - количество багов: {answer[i][-1]}")
        k+=1
