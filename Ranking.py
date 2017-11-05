from datetime import date

name = ""
def SetUsername():
    global name
    name = input("USERNAME: ")

def GetUsername():
    return name
    

def SetRank(score,level,name):
    with open("Ranking.txt", "a") as txt:
        day = date.today()
        txt.write("Date:   ")
        txt.write(str(day))
        txt.write("\tUsername:   ")
        txt.write(name)
        txt.write("\tLevel:   ")
        txt.write(str(level))
        txt.write("\tScore:   ")
        txt.write(str(score))
        txt.write("\n")    
        txt.close()

def ShowRanking():
    rank = open("Ranking.txt", 'r')
    rank_contents = rank.read()
    print(rank_contents)
        
    
