import csv
from pathlib import Path

home = str(Path.home())  # get working directory path for writing

with open(f"{home}/test.csv") as inf:
    reader = csv.reader(inf.readlines())

with open(f"{home}/test2.csv", mode="w", newline="", encoding="utf-8") as outf:
    writer = csv.writer(outf)
    for line in reader:
        line = [i.replace("\n", " ") for i in line]
        writer.writerow(line)
