from datetime import date

#def GetUsername():
    

def SetRank(score):
    name = input("USERNAME:")
    with open("Ranking.txt", "a") as txt:
        day = date.today()
        txt.write(str(day))    
        txt.write("\t||\t")
        txt.write(name)
        txt.write("\t||\t")
        txt.write(str(score))
        txt.write("\n")    
        txt.close()

