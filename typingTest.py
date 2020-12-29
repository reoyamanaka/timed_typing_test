import time, random, csv, datetime, pandas
import matplotlib.pyplot as plt





if excerpt == 0:
    with open("excerpt0.txt", "r") as rf:
        words = rf.readline()
elif excerpt == 1:
    with open("excerpt1.txt", "r") as rf:
        words = rf.readline()
elif excerpt == 2:
    with open("excerpt2.txt", "r") as rf:
        words = rf.readline()
        
print("\nWhen you hit ENTER, the excerpt to type will display and the timer will start. Type the exceprt as fast and as accurately as you can. When you are done typing, hit ENTER again. Note: Only hit ENTER the second time when you have completed the typing test.")
input()
print(words + "\n")
start = time.time()
inputExcerpt = input()
end = time.time()
elapsed = end-start

correctWords = words.split(" ")
inputWords = inputExcerpt.split(" ")
typos = []
rawscore = 0

for word in inputWords:
    if word in correctWords:
        rawscore += 1
    else:
        if len(word) > 0:
            typos.append(word)

score = rawscore / len(correctWords)*100
print("\nYour accuracy score is " + '%.2f' % score + " %.")
wordsPerMin = rawscore/elapsed*60
print("Your raw typing speed is " + '%0.2f' % wordsPerMin + " words per minute.")
if score < 100:
    print("Typo(s):")
    print(typos)
print("Your typos-adjusted typing speed is " + "%0.2f" % (wordsPerMin - len(typos)) + " words per minute.")


while True:
    saveOption = input("Do you want to save your score? [Y / N]: ")
    if saveOption == "y" or saveOption == "Y":
        currentDate = datetime.date.today()
        currentDate = currentDate.strftime("%d-%m-%Y")

        with open("progress.csv", "r") as f:
            reader = csv.reader(f)
            progress = {}
            for row in reader:
                progress[row[0]] = {"raw_wpm":row[1], "accuracy":row[2], "wpm":row[3]}
        print(progress)
        progress[currentDate] = {"raw_wpm":'%0.2f' % wordsPerMin, "accuracy":'%0.2f' % score, "wpm":'%0.2f' % (wordsPerMin - len(typos))}
        break
    elif saveOption == "n" or saveOption == "N":
        print("Progress not saved.")
        break
    else:
        print("Invalid selection.")

visualize = input("Do you want to see your progress? [Y / N] ")

    





