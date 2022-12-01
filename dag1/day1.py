elfs = []
sums = []

with open("input.txt", "r") as f:
    for line in f.readlines():
        if line != "\n":
            elfs.append(int(line.strip("\n")))
        else:
            sums.append(sum(elfs))
            elfs.clear()
print(max(sums))
print(sum(sorted(sums, reverse=True)[:3]))
