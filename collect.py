import os
import random
import player

roomTemplate = [
        [' ','▲','▲','▲','▲','▲','▲','▲',' '],
        ['◄','.','.','.','.','.','.','.','►'],
        ['◄','.','.','.','.','.','.','.','►'],
        ['◄','.','.','.','.','.','.','.','►'],
        ['◄','.','.','.','.','.','.','.','►'],
        ['◄','.','.','.','.','.','.','.','►'],
        ['◄','.','.','.','.','.','.','.','►'],
        ['◄','.','.','.','.','.','.','.','►'],
        [' ','▼','▼','▼','▼','▼','▼','▼',' ']
        ]

p = player.playerObj(4,4)
collect = ["W","I","N","N","E","R"]
savePoint = "$"
touchables = ["W","I","N","E","R","$"]
nabbed = []

# implement getChar
# clicking game button over and over again overflows hud
 
 
# handling saves and save files.
def load(pl, user):
    f = open("playerSaves/"+user+"_collect.txt", "r")
    hm = f.read(1)
    try:
        int(hm)
    except:
        hm = 0
        
    hm = int(hm)
    if hm in range(6):
        pl.prog = hm
        p.prog = hm

    i=0
    for item in range(int(pl.prog)):
        nabbed.append(str(collect[i]))
        i+=1
    f.close()
    return nabbed
    

def save(pl, user):
    o = open("playerSaves/"+user+"_collect.txt", "w")
    o.write(str(pl.prog))
    o.close()
    print("\t\tCOLLECTION SAVED")


def exclude(n):
    r = None
    while r == n or r == None:
        r = random.randint(1,7)
    return r

def chooseTile(pl):
    r = random.randint(0,1)
    xSave = random.randint(1,7)
    ySave = random.randint(1,7)

    if r == 0:
        xColl = random.randint(1,7)
        yColl = random.randint(1,7)
        if xColl == xSave and yColl == ySave:
            axis = random.randint(0,1)
            if axis == 0:
                xColl = exclude(xSave)
            if axis == 1:
                yColl = exclude(ySave)
    else:
        xColl = None
        yColl = None
    
    return xSave, ySave, xColl, yColl


def randomizeRoom(pl, room, newS):
    if  newS == True:
        rchoom = [i[:] for i in room]
    else:
        rchoom = [i[:] for i in roomTemplate]

    posx = 0
    posy = 0
    checkCollect = False
    checkSave = False

    saveX, saveY, colX, colY = chooseTile(pl)
    for y in rchoom:
        for x in y:
            if x == ".":
                
                rchoom[posy][posx] = " "
                if posy == saveY and posx == saveX and checkSave == False:
                    rchoom[posy][posx] = savePoint
                    posS = rchoom[posy][posx]
                    checkSave = True
                else:
                    rchoom[posy][posx] = " "
                if posy == colY and posx == colX and checkCollect == False:
                    rchoom[posy][posx] = collect[int(pl.prog)]
                    posC = rchoom[posy][posx]
                    checkCollect = True
            else:
                rchoom[posy][posx] = x
            posx+=1
        posy+=1
        posx=0
    return rchoom

def makeBounds(way, pl):

    bounds = [i[:] for i in roomTemplate]
    
    if way == "▲":
        block = "▼"
        pl.x = 4
        pl.y = 7
        
    if way == "◄":
        block = "►"
        pl.x = 7
        pl.y = 4
        
    if way == "▼":
        block = "▲"
        pl.x = 4
        pl.y = 1
        
    if way == "►":
        block = "◄"
        pl.x = 1
        pl.y = 4

    posx = 0
    posy = 0
    for y in bounds:
        for x in y:
            if x == block:
                bounds[posy][posx] = "X"
            posx+=1
        posy+=1
        posx=0
    bounds = randomizeRoom(pl, bounds, True)
    return bounds

def movement(pl):
    pl.prevX = pl.x
    pl.prevY = pl.y
    running = True
    
    move = input("").lower()
    if move == "w":
        pl.y -= 1
    if move == "a":
        pl.x -= 1
    if move == "s":
        pl.y += 1
    if move == "d":
        pl.x += 1
    if move == "q":
        running = False
        
    return running

def checkSpot(pl, room, user):
    newScr = room

    if room[pl.y][pl.x] == collect[pl.prog]:
        room[pl.y][pl.x] = " "
        colStr = "YOU COLLECTED "+str(collect[pl.prog])
        colStr = colStr.center(43)
        print(colStr)
        nabbed.append(collect[pl.prog])
        pl.prog+=1
        
    if room[pl.y][pl.x] ==  "$":
        save(pl, user)
        #save the data to a file and store based on name of user
    
    if room[pl.y][pl.x] == "X":
        pl.x = pl.prevX
        pl.y = pl.prevY
    
    if room[pl.y][pl.x] == "▲":
        newScr = makeBounds("▲", pl)
        
    if room[pl.y][pl.x] == "◄":
        newScr = makeBounds("◄", pl)
        
    if room[pl.y][pl.x] == "▼":
        newScr = makeBounds("▼", pl)
        
    if room[pl.y][pl.x] == "►":
        newScr = makeBounds("►", pl)

    return newScr

def roomPrint(pl, room):

    os.system("cls")
    # the hud keeps printing when the game is clicked
    lets = ""
    hud = "COLLECTION: < "
    print()

    for i in nabbed:
        lets+=i+" "
        
    print(hud+lets+">")
    print()
    posx = 0
    posy = 0
    for y in room:
        for x in y:
            if pl.x == posx and pl.y == posy:
                print("P",end="    ")
            else:
                print(x,end="    ")
            posx+=1
        posy+=1
        posx=0
        print("\n")
    #print("x = "+str(pl.x)+"y = "+str(pl.y))
    #print("collect = "+str(pl.prog))
    
def main(arg, user):
    os.system("cls")
    if arg == 1:
        load(p,user)
    random.seed()
    room = randomizeRoom(p, roomTemplate, False)

    running = True
    while running:
        roomPrint(p, room)
        running = movement(p)
        room = checkSpot(p, room, user)
        if running == False:
            break
        if p.prog == 6:
            break
        
    os.system("cls")
    if p.prog == 6:
        print("You Win!!!".center(43))
    else:
        print("Thanks for Playing!!!".center(43))
            
        

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main(1,"Chason")



