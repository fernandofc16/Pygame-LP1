from datetime import date
import getpass

def SetRank(score):
    with open("Ranking.txt", "a") as txt:
        day = date.today()
        txt.write(str(day))    
        txt.write("\t||\t")
        txt.write(getpass.getuser())
        txt.write("\t||\t")
        txt.write(str(score))
        txt.write("\n")    
        txt.close()

