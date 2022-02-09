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
