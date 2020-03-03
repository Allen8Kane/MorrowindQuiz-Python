import sqlite3

conn = sqlite3.connect("questions.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
cursor.execute("SELECT * FROM Classes")
myClass = cursor.fetchall()
cursor.execute("SELECT * FROM Questions")
myQuestions = cursor.fetchall()
finalPlayerClass = ''
conn.close()
playerAnswer = {'Combat' : 0,'Magic' : 0,'Stealth' : 0}

for item in myQuestions:
    while True:
        print(item[1] + "\n")
        print('1. ' + item[2] + "\n")
        print('2. ' + item[3] + "\n")
        print('3. ' + item[4] + "\n")
        tmpAnswer = input()
        print()
        if tmpAnswer == '1':
            playerAnswer['Combat'] += 1
            break;
        elif tmpAnswer == '2':
            playerAnswer['Magic'] += 1
            break;
        elif tmpAnswer == '3':
            playerAnswer['Stealth'] += 1 
            break;
        else:
            print('error')

if playerAnswer['Combat'] > 6:
    playerAnswer['Combat'] = 7
if playerAnswer['Magic'] > 6:
    playerAnswer['Magic'] = 7
if playerAnswer['Stealth'] > 6:
    playerAnswer['Stealth'] = 7


for item in myClass:
    if playerAnswer['Combat'] == 7 and item[2] == '7':
        finalPlayerClass = item[1]
    if playerAnswer['Magic'] == 7 and item[3] == '7':
        finalPlayerClass = item[1]
    if playerAnswer['Stealth'] == 7 and item[4] == '7':
        finalPlayerClass = item[1]
    if playerAnswer['Combat'] == 4 and item[4] == '0-6':
        finalPlayerClass = item[1]
    
    try:
        if str(playerAnswer['Combat']) == item[2] and str(playerAnswer['Magic']) == item[3] and str(playerAnswer['Stealth']) == item[4]:
            finalPlayerClass = item[1]
    except:
        print()
print('Answer:' + finalPlayerClass)
print('Combat: ' + str(playerAnswer['Combat']) + ' Magic: ' + str(playerAnswer['Magic']) + ' Stealth: ' + str(playerAnswer['Stealth']))
