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
d = list(d)
# print(d)
for i in range(0, 10):
    print(d.count(str(i)))

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