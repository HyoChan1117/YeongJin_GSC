N, X = map(int, input().split())
A = input().split()

list_num = []
for index in range(N):
    if int(A[index]) < X:
        list_num.append(A[index])

txt = ""
for value in list_num:
    txt += value + " "
    
print(txt)