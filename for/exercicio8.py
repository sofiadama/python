n1 = int(input())
n2 = int(input())

soma = 0

if n1 > n2:
    n1, n2 = n2, n1
    
for i in range(n1+1, n2, 1):
    soma += i 

print(soma)
