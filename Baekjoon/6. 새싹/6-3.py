N = int(input())

num_star = [ value for value in range(1, N*2, 2) ]

for i in range(N):
    print((N-i+1) * " ", "*" * num_star[i])