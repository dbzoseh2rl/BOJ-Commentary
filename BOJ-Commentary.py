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


# 2869
a, b, v = map(int, input().split())
day = 0
if (v - b) % (a - b) != 0:
    day = ((v - b) // (a - b)) + 1
else:
    day = ((v - b) // (a - b))
print(day)

# 11382
A, B, C = map(int, input().split())
print(A + B + C)

# 3003
cp = [1, 1, 2, 2, 2, 8]
li = list(map(int, input().split()))
for i in range(6):
    print(cp[i]-li[i], end=' ')


# 10430
A, B, C = map(int, input().split())
print((A+B) % C)
print(((A % C) + (B % C)) % C)
print((A*B) % C)
print(((A % C) * (B % C)) % C)

#2420
n, m = map(int, input().split())
print(abs(n - m))

# 2475
n = list(map(int, input().split()))
sum = 0
for i in n:
    sum += i * i
print(sum % 10)

# 2743
n = input()
print(len(n))


# 1037
import sys
x = int(sys.stdin.readline())
y = list(map(int, sys.stdin.readline().split()))
a = max(y)
b = min(y)
print(a * b)


# 10699
import datetime
print(str(datetime.datetime.now())[:10])

from datetime import datetime
now = datetime.now()
print(now.date())

import datetime
now = datetime.datetime.now()
print(str(now)[:10])

# 2750
n = int(input())
s = []
for i in range(n):
    a = int(input())
    s.append(a)
s.sort()

for s in s:
    print(s)


# 2751
import sys
n = int(input())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
for l in sorted(l):
    print(l)

# 15552
import sys
t = int(input())
for i in range(t):
    x, y = map(int, sys.stdin.readline().split())
    s = x + y
    print(s)

# 2231
N = int(input())
for i in range(N):
    temp = sum(map(int, str(i)))
    result = i + temp
    if result == N:
        print(i)
        break
else:
    print(0)


# 17427
import sys
n = int(sys.stdin.readline())
s = 0
for i in range(1, n+1):
    s += (n//i) * i
print(s)

# 2884        //git 안함
import sys
n, m = map(int, sys.stdin.readline().split())
if m > 44:
    print(n, m-45)
elif m < 45 and n > 0:
    print(n - 1, m + 15)
else:
    print(23, m + 15)

# 2581
#시간초과
t = int(input())
for i in range(t + 1):
    a, b = map(int, input().split())
    h = a ** b
    print(h % 10)

# 통과된 코드
import sys
input = sys.stdin.readline
T = int(input())
value = []
for i in range(T):
    a, b = map(int, input().split())
    b = b % 4
    if b % 4 == 0:
        b = 4
    s = a ** b
    if s % 10 == 0:
        value.append(10)
    else:
        value.append(s % 10)

for i in value:
    print(i)