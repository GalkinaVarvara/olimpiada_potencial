import csv
with open('game.csv',encoding='utf-8') as f:
    reader = csv.reader(f,delimiter='$')
    ans = list(reader)
    s=''
    name = []
    games = []
    for i in range(1,len(ans)):
        if ans[i][1] not in name:
            name.append(ans[i][1])
        games.append([])
        games[name.index(ans[i][1])].append(ans[i][0])
    s = ''
    while s != 'game':
        s=input()
        if s == 'game':
            break
        if s in name:
            if len(games[name.index(s)])>5:
                print(f'Персонаж {s} встречается в играх:')
                for i in range(5):
                    print(games[name.index(s)][i])
                print('и др.')
            if 0<len(games[name.index(s)])<=5:
                print(f'Персонаж {s} встречается в играх:')
                for i in range(len(games[name.index(s)])):
                    print(games[name.index(s)][i])
        if s not in name:
            print('Этого персонажа не существует')






