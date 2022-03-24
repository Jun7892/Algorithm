A, B, C = map(int, input().split())

# A, B, C = input().split()
# A, B, C = int(A, B, C)



print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)