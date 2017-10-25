from datetime import date
import getpass

def SetRank(score):
    day = date.today()
    RankingFile = open("Ranking.txt","w")
    RankingFile.write(str(day))    
    RankingFile.write("\t||\t")
    RankingFile.write(getpass.getuser())
    RankingFile.write("\t||\t")
    RankingFile.write("Pontuação:")
    RankingFile.write(str(score))
    RankingFile.write("\n")    
    RankingFile.close()

