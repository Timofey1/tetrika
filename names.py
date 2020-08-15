with open("names.txt") as f:
    names = f.read()
names = names.replace('"','').split(",")
names.sort()
res=0
for i in range(len(names)):
    alphSumm = 0
    for j in names[i]:
        alphSumm+=ord(j)-64
    res += alphSumm*(i+1)
print(res) # Output: 871853874
