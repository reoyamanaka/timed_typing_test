import csv
f = open("progress.csv", "r+")
reader = csv.reader(f)
progress = {}
for row in reader:
    progress[row[0]] = {"wpm":row[1], "accuracy":row[2]}

