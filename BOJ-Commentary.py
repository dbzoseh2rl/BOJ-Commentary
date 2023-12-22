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
# 다시푼거
# import sys
# n = int(sys.stdin.readline())
# for i in range(1, n + 1):
#         print("*"*i)

# 2439
n = int(input())
for i in range(1, n + 1):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print('')
# 다시짠거
# import sys
# n = int(sys.stdin.readline())
# for i in range(1, n + 1):
#     print(" "*(n - i) + "*"*(i))

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


# 다른 풀이
a, b, v = map(int, input().split())
n = (v-b) // (a-b)
if (v-b) % (a-b):
    print(n+1)
else:
    print(n)

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

import datetime
d_today = datetime.date.today()
print(d_today)

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

# 2884
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


# 1546
import sys
n = int(input())
x = list(map(int, sys.stdin.readline().split()))
y = max(x)
sum = 0
for i in range(n):
    x[i] = x[i]/y * 100
    sum += x[i]
print(sum/n)

# 10926
a = str(input())
print(a + "??!")

# 8958
N = int(input())
for i in range(N):
    a = input()
    score = 0
    sum = 0
    for j in a:
        if j == 'O':
            score += 1
        else:
            score = 0
        sum += score
    print(sum)

# 2440
n = int(input())
for i in range(0, n + 1):
    for k in range(n - i):
        print("*", end="")
    print()

# import sys
# n = int(sys.stdin.readline())
# for i in range(0, n + 1):
#     print(" "*i + "*"*(n - i))

# 2441
n = int(input())
for i in range(0, n + 1):
    for j in range(i):
        print(" ", end="")
    for k in range(n - i):
        print("*", end="")
    print()

# 2442
n = int(input())
for i in range(1, n + 1):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(0, 2*i - 1):
        print("*", end="")
    print()

# 2433
n = int(input())
for i in range(0, n + 1):
    for j in range(i):
        print(" ", end="")
    for k in range(2*n - 2*i - 1):
        print("*", end="")
    print()
    # 다른 풀이
for l in range(5 - i):
        print(" ", end="")

# git test
# git test 2

# 2562
put = []
for i in range(9):
    put.append(int(input()))
print(max(put))
print(put.index(max(put)) + 1)

# 2577
a = int(input())
b = int(input())
c = int(input())
d = str(a * b * c)
for i in range(0, 10):
    print(d.count(str(i)))

x = int(input()) * int(input()) * int(input())
for i in range(0, 10):
    print(str(x).count(str(i)))

# 2739
n = int(input())
for i in range(1, 10):
    a = n * i
    print(n, "*", i, "=", a)

# 2754
n = str(input())
a = 0
if n == "A+":
    a = 4.3
elif n == "A0":
    a = 4.0
elif n == "A-":
    a = 3.7
elif n == "B+":
    a = 3.3
elif n == "B0":
    a = 3.0
elif n == "B-":
    a = 2.7
elif n == "C+":
    a = 2.3
elif n == "C0":
    a = 2.0
elif n == "C-":
    a = 1.7
elif n == "D+":
    a = 1.3
elif n == "D0":
    a = 1.0
elif n == "D-":
    a = 0.7
elif n == "F":
    a = 0.0
print(a)

# 24900
print('''                                                           :8DDDDDDDDDDDDDD$.                                           
                                                      DDDNNN8~~~~~~~~~~=~7DNNDNDDDNNI                                   
                                                  ?NNDD=~=~~~~~~~~~~~~~~~~~=~~==~=INNDNN7                               
                                               +NDDI~~~~~~~~~~~~~~~~~~~~~~~=~~========~ODND+                            
                                            :NND~~~~~~~~~~~~~~~~~~~~~~~~~~~=~~============7NDN                          
                                          $DD$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=~~==============~DNN                        
                                        $DD=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=~~=================NND                      
                                       ND7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=~~===================DD7                    
                                     ~DD=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=======================8DN.                  
                                    8DO~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=========================DD                  
                                   8N~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=~~=======================DN                 
                                  NN::::::::~~~~~~~~~~~=~~~~~~~~~~~~~~~~~~~=~~========================DDO               
                                 $D$:::::::::::::::~~~~DD~~~~~~~~~~~~~~~~~~=~~=========================DN.              
                                 D8:::::::::::::::::::DN=::~~~~~~~~~~~~~~~~=~~======================~~:~DN              
                                DN:::::::::::::::::::ONO::::::::::::::::::::~~~~~~~~~~~~:::::::::::::::::DN             
                               DN::::::::::::::::::::NN.:::::::::::::::::::::::::::DN::::::::::::::::::::$DO            
                               DD:::::::::::::::::::DNI:::::::::::::::::::::::::::::D=::::::::::::::::::::NN            
                              NN~~~~:::::$N?:::::::.NN::::::::::::::::::::::::::::::ND.:::::::::::::::::::+N8           
                              N7~~~~~~~~OD7::::::::~DD::::::::::::::::::::::::::::::~D$::::::::::::::::::::DN           
                             NN~~~~~~~~IDZ~~~~~::::DN~:::::::::::::::::::::::::::::::DN::::::::::::::::::::=N~          
                             DD~~~~~~~~NN~~~~~~~~~=NN::::::::::::::::::::::::::::::::DN:::::::::::::::~~====NN          
                            8D~~~~~~~~ND~~~~~~~~~~~ND~~~~~~~~:::::::::::::::::::::::::N7:::~~===============NN          
                            DD~~~~~~~ON+~~~~~~~~~~~ND~~~~~~~~~~~~~~~~~~~=+NZ==========NN====================~ND         
               :DD7   DNDD. N8~~~~~~~NN~~~~~~~~~~DDND~~~~~~~~~~~~~~~~~~~~ND~~=========DD=====================ND         
               N~:DDNNN .8NDN~~~~~~~$D=~~~~~~~~+ND.DD~~~~~~~~~~~~~~~~~~~=DD~~=========~D+====================DN         
              :D     .  ..~ND~~~~~~~NN~~~~~~~+NN$..ND~~~~~~~~~~~~~~~~~~~7N=~~=========~ND=======~============ON         
              NN       ...:N?~~~~~~~N=~~~~~NNNI.. .7D+~~~~~~~~~~~~~~~~~=8NN~~==========NN=======N============$N         
         N  ODN       ....DN~~~~~~~DD=8NNND$..     .DD~~~=~~~~~~~~~~~~~=NNDD=~=========8D~======NN===========~N$        
    N? =NN  ND      .....NND~~~~~~~DDNN:...        .ND=~DNN~~~~~~~~~~~~=DN.DN~=========?N+======NN============ND        
   $D? DN    DZ    ....ND8NN~~~~~~$D                .DD~NNDD~~~~~~~~~~~~D8..DN=========~DN======NN============DN        
   DN ~N~   NN    ..:~NN..NZ~~~~~~DN                  NNN8.ND~~~~NDN?~~~DZ...7DD=======~NN======NN============DN        
   ND DD    :DN.  ..ND$  .N?~~~~~=NNN                   . ..DDD$~N8OND8=N+   ..DDDZ~====NN======+D+===========ND        
   NO         DD  ZDN    8NO~~~~~~NNN..DDDNN7               ...NND...:DDD:     .:.NDND=~DD======~DO===========DN        
              DNDDN:.    DN~~~~~~=NNNN.ODNNNNDDNNO              ...     .         ...DNNNN=======ND===========DD        
       INDN7    DD.     .DD~~~~~=IDND:.:~.....?DNDNN.                        ...... ....$D=======ND===========ND        
       NN        ND.    8N=~~~~$ND::.:=~:.~=......=ND~                 .NNNNNNNNNNNNNNN.~N+======NN===========DN        
       $DD        DN:   DD~~~~7NO...~==.:~~:.....                      NNNND? ..::..7NZ.:N?======8D~==========ZN        
       DN?     ~D: DND.?D~~~~~DD....~:.~=~.......                            ....~=:.:~..ND======~N$==========~DO       
       ND    ..DD.  .DNDN=~~~~DI.......:.........                           ....=~..~~~..DN======~DD===========NN       
       DDD  :.:DD.  . DDI~~~~~ND................        .DNNNNNNNNNN7      ....=~:.:~~...NN=======ND===========?D~      
       8D. ...OD..    DD~~~~~~+ND ............          NN:~::::~~~8N      ........~~...:ND=======DN============NN      
       DDI:...ND     .D7~~~~~~~7NN ..........           ID8::::::::8D      .............:DN=======ON============NN      
        ~NNND.N=.   .NN~~~~~~~~~NDN8                       ~::::::~N8       .............DN========D=============NI     
               DDNNN.ND~~~~~~~~DD =DND                                       ............DN========N+~===========NN     
                   ~:N=~~~~~~~~DD   .DDDD                                       ........ NN========DD============8D     
                    8N~~~~~~~~~ND    . .7NDDD? .                                      .8DDN========NN=============D:    
                    DD~~~~~~~~~DND:         IDNNND$.                           .+DNNNNDNIDN========DD=============DD    
                    ND~~~~~~~~ZN 7DD .. .:DDNDDNNDNNNNDDNDND8$?===+$8DDNNNDDDDDN8I~DN====8N========NN=============NN    
                    DD~~~~~~~~8N   DD.  .NN~~~~.~~=DNDNO.:7ODDDDNNDD8DDDND=~~~ =~~~ON====8N========DN=============DN    
                    ND~~~~~~~~DN    ZDD  DN~~~ ~~~~~=.7DDD+.......8NNN==~~~~~ ~~~~~ONN$==DN========8N=============ON    
                    ND~8N~=~~~ZN      DDODN=~.~~~~~=.~~~~INDNNNNDNN~~~~~~~~:~~~~~~~DN~ND=DN========DD=========~ND=8N    
                    IN=NDDI~~~~D8       DNN::~~~~~.~~~~~=.~~ND~~ND~~~~~~~~.~~~~~~~~NN  NDNN====ND==ND~D?======DNN=ND    
                     DNNI8ND=~~DN:       ZN=~~~~~ ~~~~~.~~~~DD~=DD~~~~~~~ ~~~~~~~=.ND. . ND===DNDD=NDDNN=====8NZDDDN    
                      NND  IDNDNNN+       D+~~~:~~~~~~ ~~~~~DDNNN+~~~~~~~~~~~~~~:=?N7   .ND=~ND  DNNN~ID====ND7 NNN     
                       ID                 ND~~ ~~~~~:.~~~7DDN7IDNN==~~ ~~~~~~~~ ~~DN   .:N?DDDDD NND  8N~=DDD  ZNN      
                                          NN~:~~~~~ =7DDDD+8N  :N8DDZ.~~~~~~~~.~~~DD.   NDD+ . DN=     OND+             
                                          DND~~~=8DNDDZ=~~ ND   NN~INND~~~~~.~~~~ND .    .    ..IDD                     
                                         DDNNNDNNN+~~~~~~.7N.    ND~~~NDDI~ ~~~~=NNN             .DDI                   
                                        DN=~~~~.=~~~~~~ ~~DN     +N+~~~~+DNDD~~~NNNND.            ..ND                  
                                         DDI~~ ~~~~~~~ ~~~ND..  ..ND~~~~:~~~DNDNNNN+            ..7O8ND+                
                                          .DND=~~~~=::~~=NN.   . . 8D~~.~~~~~~=DN$ODNDNDNNNDNNNNND8+~..                 
                                             8DNNI=.~~~~=NDDNNNNDDNDNN.~~~~~IDDNDND7:.                                  
                                                ?DNNDD?~DD          ~NN~~=NDD$                                          
                                                     :DDD.            NNNN=                                             ''')

# 2338
a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)

# 5338
print('''       _.-;;-._
'-..-'|   ||   |
'-..-'|_.-;;-._|
'-..-'|   ||   |
'-..-'|_.-''-._|''')

# 2884
import sys
n, m = map(int, sys.stdin.readline().split())
if m > 44:
    print(n, m-45)
elif m < 45 and n > 0:
    print(n - 1, m + 15)
else:
    print(23, m + 15)

#10807
n = int(input())
data = list(map(int, input().split()))
v = int(input())
print(data.count(v))

# 3052               ************
# set은 수학에서 집합과 비슷하다.(중복된 값은 자동으로 중복이 제거)
d = []
for i in range(10):
    d.append(int(input()) % 42)
d = set(d)
print(len(d))

d = []
for i in range(10):
    n = int(input()) % 42
    d.append(n)
d = set(d)
print(len(d))

# 15596
def solve(a):
    ans = 0
    for i in a:
        ans += i
    return ans

# 11654
n = input()
print(ord(n))

# 11720
a = int(input())
b = list(input())
sum = 0
for i in range(a):
    sum += int(b[i])
print(sum)

# 10809
word = input()
alphabet = list(range(97, 123))  # 아스키코드 숫자 범위
for x in alphabet:
    print(word.find(chr(x)), end=' ')

# 10870
def factorial(n):
    if (n <= 1):
        return n
    return factorial(n - 1) + factorial(n - 2)
n = int(input())
print(factorial(n))

# 10871  *************
n, x = map(int, input().split())
c = list(map(int, input().split()))
for i in range(n):
    if c[i] < x:
        print(c[i], end=" ")

# 10872 재귀 코드  BLOG
def factorial(n):
    result = 1
    if n > 0:
        result = n * factorial(n - 1)
    return result

n = int(input())
print(factorial(n))

# 2675
t = int(input())
for i in range(t):
    a, b = input().split()
    print()
    for j in b:
        print(j*int(a), end='')
    print()

# 1193
n = int(input())
line = 1
while n > line:
    n -= line
    line += 1
if line % 2 == 0:
    up = n
    down = line - n + 1
else:
    up = line - n + 1
    down = n
print(f'{up}/{down}')

# 재귀 예제 1
graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}
# 재귀 예제 1
def recursive_dfs(v, discovered = [] ):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
            return discovered

# 재귀 예제 2
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
       result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n - 1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n - 1)

# 각각의 방식으로 구현한 n! 출력(n = 5)
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))

# 10828
import sys
stack = []
def push(x):
    stack.append(x)
def pop():
    if not bool(stack):
        print(-1)
    else:
        print(stack.pop())
def size():
    print(len(stack))
def empty():
    if bool(stack):
        print(0)
    else:
        print(1)
def top():
    if not bool(stack):
        print(-1)
    else:
        print(stack[-1])
a = sys.stdin.readline()
for i in range(int(a)):
    b = sys.stdin.readline().split()
    if b[0] == "push":
        push(b[1])
    elif b[0] == "pop":
        pop()
    elif b[0] == "size":
        size()
    elif b[0] == "empty":
        empty()
    elif b[0] == "top":
        top()

a, b = map(int, input().split())
print(a + b)

# 1330
A, B = map(int, input().split())
#print('>') if A > B else print('<') if A < B else print('==')

if A > B:
    print('>')
elif A < B:
    print('<')
elif A == B:
    print('==')

# 9498
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

#  10773
n = int(input())
z = []
for i in range(n):
    num = int(input())
    if num == 0:
        z.pop()
    else:
        z.append(num)
print(sum(z))

# 9012
T = int(input())
for i in range(T):
    d = str(input())
    ch = 0

    for j in d:
        if j == '(':
            ch += 1
        elif j == ')':
            ch -= 1
        if ch == -1:
            break

    if ch == 0:
        print('YES')
    else:
        print('NO')

# 10818
N = int(input())
a = list(map(int, input().split()))
a.sort()
print(a[0], a[-1])

# 2869
a, b, v = map(int, input().split())
day = 0
if (v - b) % (a - b) != 0:   # 나누기 했을때 나머지 가 0이 아니면
    day = ((v - b) // (a - b)) + 1
else:
    day = ((v - b) // (a - b))
print(day)

# 2292
n = int(input())    # 반복문 갯수 입력
nums = 1            # 벌집 갯수 1부터 시작
cn = 1
while n > nums:
      nums += 6 * cn  # 벌집이 6 배로 증가
     cn += 1
print(cn)

# 10828
import sys
input=sys.stdin.readline

n = int(input()) #명령의 수
stack=[]

def push(x):
    #리스트의 마지막에 추가
    stack.append(x) #딱히 int(x)할 필요는 없을 듯

def pop():
    if(len(stack)==0):
        print(-1)
    else:
        print(stack.pop())

def size():
    print(len(stack))

def empty():
    if(len(stack)==0): #비면
        print(1)
    else: #안 비면
        print(0)

def top():
    if(len(stack)==0):
        print(-1)
    else:
        print(stack[-1])

for i in range(n):
    command=input().split() #push 1 같은 애들 분리
    if(command[0] == 'push'):
        push(command[1])
    if (command[0] == 'pop'):
        pop()
    if (command[0] == 'size'):
        size()
    if (command[0] == 'empty'):
        empty()
    if (command[0] == 'top'):
        top()

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
print((A+B) % C);print(((A % C) + (B % C)) % C);print((A*B) % C);print(((A % C) * (B % C)) % C)

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

# 2750
n = int(input())
s = []
for i in range(n):
    a = int(input())
    s.append(a)
s.sort()

for s in s:
    print(s)

import sys
n = int(sys.stdin.readline())
s = [int(sys.stdin.readline()) for _ in range(n)]
s.sort()
print('\n'.join(str(s) for s in s))

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

# # 1236
# # arr = [[0]* 열의개수 for i in range(행의개수)]
n, m = map(int, input().split())
arr = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        print(arr[i][j], end="")
    print(".")

# 2010
import sys
num = int(sys.stdin.readline())
sum = 1
for i in range(num):
    tempnum = int(sys.stdin.readline())
    sum += tempnum
print(sum-num)

import sys
# for i in range(int(sys.stdin.readline())//4):
#     print("long", end=" ")
# print("int")

# 간단하게
print(int(sys.stdin.readline())//4 * "long " + "int")

# 1094
import sys
x = int(sys.stdin.readline())
stick = [64, 32, 16, 8, 4, 2, 1]
cnt = 0
for i in range(len(stick)):
    if x == 0:
        break
    if stick[i] <= x:
        x -= stick[i]
        cnt += 1
print(cnt)

# 막대기 길이 전부 이진수로 표현 가능하기때문에
# print(bin(int(input())).count("1"))

# 9654
print("SHIP NAME      CLASS          DEPLOYMENT IN SERVICE")
print("N2 Bomber      Heavy Fighter  Limited    21        ")
print("J-Type 327     Light Combat   Unlimited  1         ")
print("NX Cruiser     Medium Fighter Limited    18        ")
print("N1 Starfighter Medium Fighter Unlimited  25        ")
print("Royal Cruiser  Light Combat   Limited    4         ")

# 재귀 예제 1
graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

def recursive_dfs(v, discovered = [] ):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
            return discovered

# 재귀 예제 2
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
       result *= i
    return result

stack = [1, 2, 3, 4]
print(stack)
print(*stack)

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n - 1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n - 1)

# 각각의 방식으로 구현한 n! 출력(n = 5)
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))

stack = [1, 2, 3, 4]
print(stack)
print(*stack)

# 1297
import sys
n = int(sys.stdin.readline())
li=[]
for i in range(n):
    [a, b] = map(int, sys.stdin.readline().split())
    li.append([a, b])
li.sort()       # li리스트 정렬
for i in li:
    print(i[0], i[1])   # 리스트 인덱싱으로 출력

# 7287
print("65\n")
print("ehrud25\n")

# 10807
n = int(input())
data = list(map(int, input().split()))
v = int(input())
print(data.count(v))

# input();print(input().split().count(input()))

# 5597
li = []                     # 런타임 에러
check = range(29)
for i in check:
    li.append(int(input()))
    if i not in li:
        print(i)

s = [i for i in range(1, 31)]
for _ in range(28):
    s.remove(int(input()))
print(*s, sep="\n")

# 2744
str1 = str(input())
str1.swapcase()
print(str1.swapcase())

# 10809
s = input()
alphabet = list(range(97, 123))
for x in alphabet:
    print(s.find(chr(x)), end=" ")

# 11718
while True:
    try:
        print(input())
    except EOFError:
        break

# 9086
li = []
for i in range(int(input())):
    d = str(input())
    li.append(d[0]+d[-1])
    print(li[i])

# 15964
a, b = map(int, input().split())
n1 = a + b
n2 = a - b
num = n1 * n2
print(num)

# 2920
s = input().replace(" ", "")
s = input().replace(" ", "")
if s == "12345678":
   print("ascending")
elif s == "87654321":
   print("descending")
else:
   print("mixed")

# 1152
n = input().strip()
print(len(n.split()))

# 18108
n = int(input())
x = n - 543
print(x)

# 1157
word = input().upper()
s_word = list(set(word))
v = []
for x in s_word:
    cnt = word.count(x)
    v.append(cnt)
if v.count(max(v)) > 1:
    print("?")
else:
    print(s_word[(v.index(max(v)))])

# 2908
num1, num2 = input().split()
num1 = int(num1[::-1])    # [::-1] : 역순
num2 = int(num2[::-1])
if num1 > num2:
    print(num1)
else:
    print(num2)

# 2525
h, m = map(int, input().split())
x = int(input())
h += x //60
m += x % 60
if m >= 60:
    h += 1
    m -= 60
if h >= 24:
    h -= 24
print(h, m)

# 2480
a, b, c = map(int, input().split())
if a == b == c:
    print(10000 + a * 1000)
elif a == b or a == c:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
else:
    print(max(a, b, c) * 100)

# 4344              ?????????????
C = int(input())
for _ in range(C):
    case = list(map(int, input().split()))
    avg = sum(case[1:]) / case[0]
    cnt = 0

    for i in case[1:]:
        if i > avg:
            cnt += 1

    r = cnt/case[0]*100
    print(f"{r:.3f}%")

# 11943
A, B = map(int, input().split())
C, D = map(int, input().split())
print(min(A+D,B+C))

# 25372
for _ in range(int(input())):
    password = len(input())
    print("yes") if 6 <= password and password <= 9 else print("no")

# 27323
a=int(input())
b=int(input())
print(a*b)

# 1546
import sys
n = int(input())
x = list(map(int, sys.stdin.readline().split()))
y = max(x)
sum = 0
for i in range(n):
    x[i] = x[i]/y * 100
    sum += x[i]
print(sum/n)

# 10988
word = list(str(input()))
if list(reversed(word)) == word:
    print(1)
else:
    print(0)

# 16486
d1 = int(input())
d2 = int(input())
pi = 3.141592
ans = d1*2 + 2*d2*pi
print(ans)

# 25640
a = input()
mbti = [input() for _ in range(int(input()))]
print(mbti.count(a))

# 1978
n = int(input())
data = map(int, input().split())
cnt = 0
for i in data:
    check = 0
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            check += 1
    if check == 0:
        cnt += 1
print(cnt)

# 2712
for _ in range(int(input())):
    n, s = input().split()
    if s == "kg":
        print("%.4f %s" % (float(n)*2.2046, "lb"))
    elif s == "lb":
        print("%.4f %s" % (float(n)*0.4536, "kg"))
    elif s == "l":
        print("%.4f %s" % (float(n)*0.2642, "g"))
    elif s == "g":
        print("%.4f %s" % (float(n)*3.7854, "l"))

# 19944
N, M = map(int, input().split())
if M <= 2:
    print("NEWBIE!")
elif M > 2 and M <= N:
    print("OLDBIE!")
else:
    print("TLE!")

# 1809
"(___)
(o o)____/
 @@      \\
  \\ ____,/
  //   //
 ^^   ^^"

# 25494
T = int(input())
while T > 0 :
    a, b, c = map(int, input().split())
    print(min(a, min(b, c)))
    T -= 1


# 16170
import datetime
data = datetime.datetime.now() + datetime.timedelta(hours=9)
print(data.year)
print(data.month)
print(data.day)

# 25304
x = int(input())
n = int(input())
for i in range(n):
    a, b = input().split()
    a, b = int(a), int(b)
    x -= (a * b)
print("Yes" if x == 0 else "No")


# 10170
print("""NFC West       W   L  T
-----------------------
Seattle        13  3  0
San Francisco  12  4  0
Arizona        10  6  0
St. Louis      7   9  0

NFC North      W   L  T
-----------------------
Green Bay      8   7  1
Chicago        8   8  0
Detroit        7   9  0
Minnesota      5  10  1""")


# 1834
a = int(input())
for i in range(a):
    x = []
    z = list(map(int, input().split()))
    # print(z)
    for i in z:
        if i % 2 == 0:
            x.append(i)
    print(sum(x), min(x))


# 2935
a = int(input())
b = input()
c = int(input())
if b == "*":
    print(a * c)
else:
    print(a + c)


# 10950
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
print(sum)

# 15962
print("파이팅!!")

# 5554
a = int(input()); b=int(input()); c= int(input());d = int(input())
z = a + b + c + d
print(z//60)
print(z%60)

# 2953
total = []
for _ in range(5):
    score = list(map(int, input().split()))
    total.append(sum(score))
print(total.index(max(total)) + 1, max(total))


# 11021
t = int(input())
for i in range(1, t + 1):
    a, b = map(int, input().split())
    x = a + b
    print(f"Case #{i}: {x}")


# 11022
t = int(input())
for i in range(1, t + 1):
    a, b = map(int, input().split())
    x = a + b
    print(f"Case #{i}: {a} + {b} = {x}")

# 1789
n = int(input())
sum = 0
result = 0
for i in range(1, n + 1):
    sum += i
    result += 1
    if sum > n:
        result -= 1
        break
    # print(sum)
    # print("______")
    # print(result)
print(result)

# 27433
N = int(input())

if N == 0 :
    print(1)
else :
    result = 1
    for i in range(2, N+1) :
        result *= i
    print(result)

# 10952
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a + b)

# 27959
N, M = map(int, input().split())
if N*100 >= M:
    print("Yes")
else:
    print("No")


# 1920
# 시간 초과
# import sys
# n = int(sys.stdin.readline())
# arr1 = list(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# arr2 = list(map(int, sys.stdin.readline().split()))
#
# for i in arr2:
#     if i in arr1:
#         print("1")
#     else:
#         print("0")


n = int(input())
A = set(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
for i in B:
    print(1 if i in A else 0)


# 2576
import sys
li = []
for i in range(7):
    x = int(sys.stdin.readline())
    if x % 2 == 1:
        li.append(x)
if len(li) == 0: print("-1")
else:
    print(sum(li))
    print(min(li))

# 10951
while True:
    try:
        a, b = map(int, input().split())
    except:
        break
    print(a + b)

# 1568
n = int(input())  # 현재 앉아 있는 새의 수
count = 0
k = 1  # 1부터 노래하기 시작
while n > 0:
    if k > n:  # 만약 불러야 하는 음계가 남아있는 새의 수보다 많다면
        k = 1  # 음계를 1로 초기화
    n -= k  # 부른 음계만큼 새의 수가 감소
    k += 1  # 새가 떠난 뒤 음계를 1씩 올려줌
    count += 1
print(count)


# 1110
n = int(input())
num = 0
cnt = 0

while 1:
    if len(num) == 1:
        num = "0" + num
    plus = str(int(num[0]) + int(num[1]))  # "2" + "6" = "8"
    num = num[-1] + plus[-1]                # "6" + "8" = "68"
    cnt += 1
    if num == n:
        print(cnt)
        break

# 1251
import sys
word = sys.stdin.readline().strip()
new_word_list = []
for i in range(1,len(word)):
    for j in range(i+1,len(word)):
        first_word = word[:i][::-1]
        second_word = word[i:j][::-1]
        third_word = word[j:][::-1]
        new_word_list.append(first_word+second_word+third_word)
sort_new_word=sorted(new_word_list)
print(sort_new_word[0])

# 10757
a, b = map(int, input().split())
x = a + b
print(x)

# 2752
print(*sorted(map(int, input().split())))
a = list(map(int, input().split()))
a.sort()
print(a[0], a[1], a[2])

# 13277
a, b = map(int, input().split())
print(a * b)

# 1264
while True:
    x = input()
    if x == '#':
        break
    value = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    cnt = 0
    for i in range(len(x)):
        if x[i] in value:
            cnt += 1
    print(cnt)

# 2752
print(*sorted(map(int, input().split())))
a = list(map(int, input().split()))
a.sort()
print(a[0], a[1], a[2])

# 5622     ???????
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

text = input()
sum = 0
for i in text:
    for j in dial:
        if i in j:
            sum += dial.index(j) + 3
print(sum)


# 3046
R1, S = map(int, input().split())
print(S * 2 - R1)


# 2845
L, P = map(int, input().split())
news = list(map(int, input().split()))
for i in news:
    print(i - L * P, end = ' ')

# 7287
print("65\n")
print("ehrud25\n")

# 10807
n = int(input())
data = list(map(int, input().split()))
v = int(input())
print(data.count(v))
# input();print(input().split().count(input()))
# input()
# print(input().split().count(input()))

# 5597
li = []                     #런타임 에러
check = range(29)
for i in check:
    li.append(int(input()))
    if i not in li:
        print(i)

# 5532
l = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
x = (A / C)
y = (B / D)
print(int(l - max(x, y)))

# 1181
n = int(input())
s = []
for _ in range(n):
    s.append(input())
s = list(set(s))
s.sort()
s.sort(key=len)

for i in s:
    print(i)

# 4470
n = int(input())
for i in range(n):
    l = input()
    print(f"{i+1}. {l}")

# 1085
x, y, w, h = map(int, input().split())
print(min(x, y, w - x, h - y))

# 1312
a, b, n = map(int, input().split())
for i in range(n):
    a = (a % b) * 10
    result = a // b
print(result)

# 10989
import sys
n = int(sys.stdin.readline())
b = [0] * 10001
for i in range(n):
    b[int(sys.stdin.readline())] += 1   #입력값과 같은 인덱스에 +1
for i in range(10001):
    if b[i] != 0:
        for j in range(b[i]):
            print(i)

# 2587
lis = [int(input()) for _ in range(5)]
lis.sort()
print(sum(lis)//5)
print(lis[2])

# 13752
for _ in range(int(input())):
    print('=' * int(input()))

# 25305
import sys
a, b = map(int, sys.stdin.readline().split())
x = list(map(int, sys.stdin.readline().split()))
z = sorted(x, reverse=True)
print(z[b-1])

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
print(temp, i)

# # 1236
# arr = [[0]* 열의개수 for i in range(행의개수)]
n, m = map(int, input().split())
arr = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        print(arr[i][j], end="")
    print(".")

# 1417
import sys
n = int(sys.stdin.readline())  # 후보의 수
dasom = int( )  # 1번 다솜의 수
other = []       # 다른사람 뽑을려는수
cnt = 0        # 매수해야하는 사람수
for i in range(n - 1):
    other.append(int(sys.stdin.readline()))
other.sort(reverse=True)
if n == 1:
  print(0)
else:
  while other[0] >= dasom:
    dasom += 1
    other[0] -= 1
    cnt += 1
    other.sort(reverse=True)
  print(cnt)

import sys
h, m, s = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())
s += t
m += s//60
h += m//60
print(h % 24, m % 60, s % 60)

# 1343
import sys
x = sys.stdin.readline()
x = x.replace("XXXX", "AAAA")
x = x.replace("XX", "BB")
if "X" in x:
    print(-1)
else:
    print(x)

# 1193      ***********
X = int(input())
line = 1
while X > line:
    X -= line
    line += 1
if line % 2 == 0:
    a = X
    b = line - X + 1
else:
    a = line - X + 1
    b = X
print(a, '/', b, sep='')