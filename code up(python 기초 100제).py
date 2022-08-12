# 6001
print("Hello")

# 6002
print("Hello World")

# 6003
print("Hello \nWorld")

# 6004
print("'Hello'")

# 6005
print('"Hello World"')

# 6006
print('"!@#$%^&*()\'')

# 6007
print("\"C:\Download\\'hello'.py\"")

# 6008
print('print("Hello\\nWorld")')

# 6009
n = input()
print(n)

# 6010
z = int(input())
print(z)

# 6011
z = float(input())
print(z)

# 6012
a = input()
b = input()
print(a, b, sep='\n')

# 6013
a = input()
b = input()
print(b)
print(a)

# 6014
n = float(input())
print(n)
print(n)
print(n)

# 6015
a, b = map(int, input().split())
print(a)
print(b)

# 6016
a, b = input().split()
print(b, end=' ')
print(a)

# 6017
s = input()
print(s, s, s)

# 6018
h, m = map(int, input().split(':'))
print(h, m, sep=':')

# 6019
y, m, d = input().split('.')
print(d, m, y, sep='-')

# 6020
f, e = input().split('-')
print(f + e)

# 6021
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

# 6022
s = input()
print(s[0:2], s[2:4], s[4:6])

# 6023
h, m, s = input().split(':')
print(m)

# 6024
w1, w2 = input().split()
print(w1 + w2)

# 6025
a, b = input().split()
c = int(a) + int(b)
print(c)

# 6026
a = input()
b = input()
c = float(a) + float(b)
print(c)

# 2진수      bin( 정수 )
# 8진수      oct( 정수 )
# 16진수    hex( 정수 )

# 6027
a = input()
n = int(a)
print("%x" % n)

# 6028
a = input()
n = int(a)
print("%X" % n)

# 6029
a = input()
n = int(a, 16)
print("%o" % n)

# 6030
n = ord(input())
print(n)

# 6031
c = int(input())
print(chr(c))

# 6032
n = int(input())
print(-n)

# 6033
n = ord(input()) + 1
print(chr(n))

# 6034
a, b = map(int, input().split())
c = int(a) - int(b)
print(c)

# 6035
a, b = map(float, input().split())
m = float(a) * float(b)
print(m)

# 6036
a, b = input().split()
print(a * int(b))

#6037
n = input()
s = input()
print(int(n) * s)

# 6038
a, b = map(int, input().split())
c = int(a)**int(b)
print(c)

# 6039
a, b = map(float, input().split())
c = float(a)**float(b)
print(c)

# 6040
a, b = map(int, input().split())
c = int(a) // int(b)
print(c)

# 6041
a, b = map(int, input().split())
c = int(a) % int(b)
print(c)

# 6042
a = float(input())
print(format(a, ".2f"))

# 6043
a, b = map(float, input().split())
c = float(a) / float(b)
print(format(c, ".3f"))

# 6044
a, b = map(int, input().split())
first = int(a) + int(b)
second = int(a) - int(b)
third = int(a) * int(b)
forth = int(a) // int(b)
fifth = int(a) % int(b)
sixth = int(a) / int(b)

print(first)
print(second)
print(third)
print(forth)
print(fifth)
print(format(sixth, ".2f"))

# 6045
a, b, c = map(int, input().split())
x = [a, b, c]
print(sum(x), round(sum(x) / len(x), 2))

# 6046      # 비트 쉬프트 연산 <<, >> #
n = int(input())
print(n << 1)
# print(n >> 1)  #10을 반으로 나눈 값인 5출력
# print(n << 2)  #10을 4배 한 값인 40 이 출력
# print(n >> 2)  #10을 반으로 나눈 후 다시 반으로 나눈 값인 2 출력

# 6047
a, b = map(int, input().split())
print(int(a) << int(b))
# print(a << b)

# 6048
a, b = map(int, input().split())
if a < b:
    print(True)
elif a >= b:
    print(False)

# 6049
a, b = map(int, input().split())
if a == b:
    print(True)
else:
    print(False)

# 6050
a, b = map(int, input().split())
if a <= b:
    print('True')
elif a != b:
    print('False')

# 6051
a, b = map(int, input().split())
if a != b:
    print('True')
elif a == b:
    print('False')

# 6052
n = int(input())
print(bool(n))

# 6053
a = bool(int(input()))
print(not a)

# 6054
a, b = input().split()
print(bool(int(a)) and bool(int(b)))

# 6055
a, b = input().split()
print(bool(int(a)) or bool(int(b)))

# 6056
a, b = map(int, input().split())
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))

# 6057
a, b = map(int, input().split())
a = int(a)
b = int(b)
print(bool(a) == bool(b))

# 6058
a, b = map(int, input().split())
print(not a and not b)

# 6059
a = int(input())
print(~a)

# 6060
a, b = map(int, input().split())
x = a & b
print(x)

# 6061
a, b = map(int, input().split())
x = a | b
print(x)

# 6062
a, b = map(int, input().split())
x = a ^ b
print(x)

# 6063
a, b = map(int, input().split())
c = (a if (a >= b) else b)
print(c)


# 6064
a, b, c = map(int, input().split())
f = (a if a < b else b) if ((a if a < b else b) < c)else c
print(f)
# 3개중 큰거 구하는 삼항식
#(a if a > b else b) if ((a if a > b else b) > c) else c

# 6065
a, b, c = map(int, input().split())
if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)

# 6066
a, b, c = map(int, input().split())
if a % 2 == 0:
    print("even")
else:
    print("odd")
if b % 2 == 0:
    print("even")
else:
    print("odd")
if c % 2 == 0:
    print("even")
else:
    print("odd")


# 6067
n = int(input())
if n < 0:
  if n % 2 == 0:
    print('A')
  else:
    print('B')
else:
  if n % 2== 0:
    print('C')
  else:
    print('D')

# 6068
n = int(input())
if n >= 90:
  print('A')
else:
  if n >= 70:
    print('B')
  else:
    if n >= 40:
      print('C')
    else:
        print('D')

# 6069
n = input()
if n == 'A':
    print("best!!!")
elif n == 'B':
    print("good!!")
elif n == 'C':
    print("run!")
elif n == 'D':
    print("slowly~")
else:
    print("what?")

# 6070
n = int(input())
if n//3 == 1:
    print("spring")
elif n//3 == 2:
    print("summer")
elif n//3 == 3:
    print("fall")
else:
    print("winter")

# 6071
n = 1
while n != 0:
  n = int(input())
  if n != 0:
    print(n)

# 6072
n = int(input())
while n != 0:
  print(n)
  n = n - 1

# 6073
n = int(input())
while n != 0:
  print(n - 1)
  n = n - 1

# 6074
c = ord(input())
t = ord('a')
while t <= c:
  print(chr(t), end=' ')
  t += 1

# 6075
n = int(input())
for i in range(n + 1):
    print(i, sep=' ')

# 6076
n = int(input())
for i in range(n + 1):
  print(i)

# 6077
n = int(input())
s = 0
for i in range(1, n + 1):
  if i % 2 == 0:
    s += i
print(s)

# 6078
while True:
    n = input()
    print(n)
    if n == 'q':
        break

# 6080
n, m = map(int, input().split())
for i in range(1, n + 1):
  for j in range(1, m + 1):
    print(i, j)

# 6081
n = int(input(), 16)
for i in range(1, 16):
    print('%X*%X=%X' % (n, i, n * i))

# 6082
n = int(input())
for i in range(1, n + 1):
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print("X", end=' ')
    else:
        print(i, end=' ')

# 6083
r, g, b = map(int, input().split())   # r,g,b를 입력받는다
n = 0       # 개수를 보여줄 n선언
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            n += 1

# 6086
n = int(input())
s = 0
c = 0
while True:
  s += c
  c += 1
  if s >= n:
    break
print(s);
