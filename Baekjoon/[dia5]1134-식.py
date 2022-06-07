s = input()

temp = s.split("=")
a, b = temp[0].split("+")
c = temp[1]
for i in range(1, len(a)+1):
    index = len(a)-i
    if a[i-1] != "?":
        temp = int(a[i-1])* 10**index
        print(temp)

print(a, b, c)
