N = int(input())

nums = []
linha = []
col = []
for i in range(N):
    nums = input().split()
    linha.append(int(nums[0])) 
    col.append(int(nums[1])) 

for i in range(N):
    resp = (linha[i]//3) * (col[i]//3)
    print(resp)