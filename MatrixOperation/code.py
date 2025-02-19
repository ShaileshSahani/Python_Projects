x = int(input("Rows: "))
y = int(input("Cols: "))
print(f"Enter {x * y} Elements")
s = "1234"
k = 0
S = []
for i in range(2):
    N = []
    for j in range(2):
        N.append(int(s[k]))
        k += 1
    S.append(N)
print(S)


n = list(map(int, input().split()))
A = []
k = 0
if len(n) != x * y:
    print("Invalid Element")
else:
    for i in range(x):
        B = []
        for j in range(y):
            B.append(n[k])
            k += 1
        A.append(B)

print(A)