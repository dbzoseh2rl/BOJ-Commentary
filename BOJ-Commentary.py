# 10718
print("강한친구 대한육군")
print("강한친구 대한육군")

# 1000
A, B = map(int, input().split())
print(A + B)

# 1001
A, B = map(int, input().split())
print(A - B)

# 10998
A, B = map(int, input().split())
print(A * B)

# 1008
A, B = map(int, input().split())
print(A / B)

10869
A, B = map(int, input().split())
print(A + B)
print(A - B)
print(A * B)
print(int(A / B))
print(A % B)

2588
num1 = int(input())
num2 = int(input())

print(num1 * (num2%10))
print(num1 * ((num2%100)//10))
print(num1 * (num2//100))
print(num1 * num2)

9498
a = int(input())
if a >= 90:
    print('A')
elif a >= 80:
    print('B')
elif a >= 70:
    print('C')
elif a >= 60:
    print('D')
else:
    print('F')

2753
n = int(input())
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print(1)
else:
    print(0)

14681
a = int(input())
b = int(input())
if a > 0 and b > 0:
    print(1)
elif a > 0 and b < 0:
    print(4)
elif a < 0 and b > 0:
    print(2)
else:
    print(3)

1330
A, B = map(int, input().split())
# print('>') if A > B else print('<') if A < B else print('==')

if A > B:
    print('>')
elif A < B:
    print('<')
elif A == B:
    print('==')


# 2438
n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

# 2439
n = int(input())
for i in range(1, n + 1):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print('')

# 2440
n = int(input())
for i in range(n):
    for j in range(n - i):
        print('*', end="")
    print()

# 2441
n = int(input())
for i in range(0, n + 1):
    for j in range(i):
        print(" ", end="")
    for k in range(n - i):
        print("*", end="")
    print()

# 25083
print("         ,r'\"7")
print("r`-_   ,'  ,/")
print(" \. \". L_r'")
print("   `~\/")
print("      |")
print("      |")


# 1712
a, b, c = map(int, input().split())
if b >= c:   # =하나 차이로 런타임 에러 뜨고 안뜨고
    print(-1)
else:
    print(a//(c - b) + 1)