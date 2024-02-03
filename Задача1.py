import csv
with open('game.csv',encoding='utf-8') as f:
    reader = csv.reader(f,delimiter='$')
    ans = list(reader)
    for i in range(len(ans)):
        if '55'in ans[i][-2]:
           print(f'У персонажа {ans[i][1]} в игре {ans[i][0]} нашлась ошибка с кодом: {ans[i][2]}. Дата фиксации: {ans[i][3]}')
           ans[i][-2] = 'Done'
           ans[i][-1] = '0000-00-00'
with open('game_new.csv', 'w', encoding='utf8', newline='') as f:
    w = csv.writer(f,delimiter='$')
    w.writerows(ans)
