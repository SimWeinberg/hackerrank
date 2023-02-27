# Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

# Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.

# int[2]: An array with the numbers of times she broke her records. Index 0 is for breaking most points records, and index 1 is for breaking least points records.

def breakingRecords(scores):
    highScore = scores[0]
    lowScore = scores[0]
    recordWin = 0
    recordLoss = 0
    ans = []
    for i in scores:
        if i > highScore:
            highScore = i
            recordWin = recordWin + 1
        elif i < lowScore:
            lowScore = i
            recordLoss = recordLoss + 1
    ans.append(recordWin)
    ans.append(recordLoss)
    return(ans)