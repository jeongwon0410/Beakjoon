N, S = map(int, input().split())
A = list(map(int, input().split()))

stack = list()

def GCD(a,b):
    while b > 0:
        a , b = b, a % b 
    return a

for i in A:
    X = abs(i-S)
    stack.append(X)


dap = stack[0]
for s_1 in range(1,len(stack)):
    dap = GCD(stack[s_1],dap)
    

print(dap)