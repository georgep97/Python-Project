import random
counter=0
rounds=0

def filling():
    #filling the list with nums(1-80)
        for i in range(1,81):
            numbers80.insert(i,i+1)
        return numbers80

   
for allgames in range(1000):
    indicator=0
    rounds +=1
    numbers80=[]
    filling()
    players=[]
    copyplayers=[]
    for i in range (100):
        numbers80=[]
        filling()
        fivenum=[]
        for j in range(5):
            pick=(random.choice(numbers80))
            numbers80.remove(pick)
            fivenum.insert(j,pick)
        players.insert(i,fivenum)
        copyplayers.insert(i,str(fivenum))

    numbers80=[]
    filling()
    countlen=0
    for i in range(1,81):
        if (indicator==1):
            break
        lucknum=(random.choice(numbers80))
        numbers80.remove(lucknum)
        counter += 1

        for j in range(100):
            if (indicator==1):
                break
            countlen=len(players[j])
            checker=countlen
            for k in range(checker):
                if (indicator==1):
                    break
                take=players[j][k]
                
                if (take==lucknum):
                    players[j].remove(take)
                    players[j].insert(k,0)

                    if (players[j][0]==0):  #winner check
                        if (players[j][1]==0):
                            if (players[j][2]==0):
                                if (players[j][3]==0):
                                    if (players[j][4]==0):
                                        indicator=1
                                        winner=copyplayers[j]

average=counter/1000
print "Average Numbers for a win: ", average
